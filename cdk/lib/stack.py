from aws_cdk import (
    core,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_logs as logs,
    aws_ecs_patterns as ecs_patterns,
)
from .monitoring import CtfMonitoring
from .function import CtfFunction
from .bucket import CtfBucket
from . import names, environment


class CtStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        notification_email,
        **kwargs,
    ) -> None:

        super().__init__(scope, id, **kwargs)

        # Email notification for errors
        monitoring = CtfMonitoring(
            self,
            "CtfMonitoring",
            notification_email=notification_email,
        )

        # S3 bucket to store raw data at beginning of ETL pipeline
        raw_files_bucket = CtfBucket(
            self,
            "RawDataFilesBucket",
            name=names.RAW_DATA_FILES_BUCKET,
        )

        lambda_code_bucket = s3.Bucket.from_bucket_name(
            self, "LambdaCodeBucket", names.LAMBDA_CODE_BUCKET
        )

        # Function to download files and save in S3
        data_download = CtfFunction(
            self,
            "ETLDownloadFunction",
            names.ETL_DOWNLOAD_FUNCTION,
            lambda_code_bucket,
            monitoring,
            memory_size=500,
            timeout_seconds=900,
            env={
                "SSM_BASE_PATH": environment.SSM_BASE_PATH,
                "RAW_DATA_FILES_BUCKET": f"{self.stack_name}-{names.RAW_DATA_FILES_BUCKET}",
            },
        )
        raw_files_bucket.bucket.grant_write(data_download.function)
        data_download.function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ssm:GetParameter"],
                resources=["*"],
            )
        )

        vpc = ec2.Vpc(self, "CtfVPC", max_azs=3)

        cluster = ecs.Cluster(self, "CtfCluster", vpc=vpc)
        cluster.add_default_cloud_map_namespace(name="service.local")

        frontend_task = ecs.FargateTaskDefinition(
            self,
            "frontend-task",
            cpu=512,
            memory_limit_mib=2048,
        )

        frontend_task.add_container(
            "frontend",
            image=ecs.ContainerImage.from_ecr_respository(
                repository=ecr.Repository.from_repository_name(
                    self,
                    "LambdaRepository",
                    repository_name=names.LAMBDA_REPOSITORY,
                )
            ),
            essential=True,
            environment={"LOCALDOMAIN": "service.local"},
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix="FrontendContainer",
                log_retention=logs.RetentionDays.ONE_WEEK,
            ),
            port_mappings=ecs.PortMapping(container_port=3000, host_port=3000),
        )

        frontend_service = ecs_patterns.NetworkLoadBalancedFargateService(
            self,
            id="frontend-service",
            service_name="frontend",
            cluster=cluster,  # Required
            cloud_map_options=ecs.CloudMapOptions(name="frontend"),
            cpu=512,  # Default is 256
            desired_count=2,  # Default is 1
            task_definition=frontend_task,
            memory_limit_mib=2048,  # Default is 512
            listener_port=80,
            public_load_balancer=True,
        )

        frontend_service.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(3000), "react inbound"
        )
