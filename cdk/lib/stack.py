from aws_cdk import (
    core,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as ec2,
)
from .monitoring import CtfMonitoring
from .function import CtfFunction
from .bucket import CtfBucket
from .task import CtfFrontendTaskDefinition, CtfBackendTaskDefinition
from .service import CtfBackendService, CtfFrontendService
from .load_balancer import CtfLoadBalancer
from .cluster import CtfCluster
from .database import CtfDatabase
from . import names, environment, aws


DB_PORT = 5432


class CtStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        site_domain,
        notification_email,
        django_secret,
        db_host,
        db_password,
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

        vpc = ec2.Vpc(self, "CtfVPC", max_azs=2)
        site_sg = ec2.SecurityGroup(
            self,
            "CtfFrontendSecurityGroup",
            allow_all_outbound=True,
            vpc=vpc,
        )
        database_sg = ec2.SecurityGroup(
            self,
            "CtfDatabaseSecurityGroup",
            allow_all_outbound=False,
            vpc=vpc,
        )
        preferred_az = f"{aws.AWS_REGION}a"

        ecs_cluster = CtfCluster(
            self,
            "CtfCluster",
            names.CLUSTER,
            vpc,
            site_sg,
            preferred_az,
        )

        frontend_port = 80
        frontend_task = CtfFrontendTaskDefinition(
            self,
            "FrontendTask",
            frontend_port,
        )
        frontend_service = CtfFrontendService(
            self,
            "CtfFrontendService",
            ecs_cluster.cluster,
            frontend_task.task,
            site_sg,
            preferred_az,
            port=frontend_port,
        )

        backend_task = CtfBackendTaskDefinition(
            self,
            "BackendTask",
            {
                "MODE": "prod",
                "DJANGO_SECRET": django_secret,
                "DB_HOST": db_host,
                "DB_PORT": "5432",
                "DB_PASSWORD": db_password,
                "SITE_DOMAIN": site_domain,
            },
        )
        backend_service = CtfBackendService(
            self,
            "CtfBackendService",
            ecs_cluster.cluster,
            backend_task.task,
            site_sg,
            preferred_az,
            frontend_service,
        )

        CtfLoadBalancer(
            self,
            "CtfLoadBalancer",
            site_domain,
            vpc,
            site_sg,
            frontend_target=frontend_service.service,
            backend_target=backend_service.service,
        )

        CtfDatabase(
            self,
            "PostgresDatabase",
            vpc,
            database_sg,
            preferred_az,
            backend_service,
            DB_PORT,
        )
