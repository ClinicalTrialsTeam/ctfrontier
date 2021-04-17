from aws_cdk import (
    core,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_ecs as ecs,
)
from .monitoring import CtfMonitoring
from .function import CtfFunction
from .bucket import CtfBucket
from .task import CtfFrontendTaskDefinition
from .service import CtfFrontendService
from .load_balancer import CtfLoadBalancer

# from .database import CtfDatabase
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

        vpc = ec2.Vpc(self, "CtfVPC", max_azs=2)
        sg = ec2.SecurityGroup(
            self,
            "CtfSecurityGroup",
            allow_all_outbound=True,
            vpc=vpc,
        )

        cluster = ecs.Cluster(
            self,
            "CtfCluster",
            cluster_name=names.CLUSTER,
            vpc=vpc,
        )
        cluster.add_default_cloud_map_namespace(name="service.local")

        frontend_task = CtfFrontendTaskDefinition(self, "FrontendTask")

        frontend_service = CtfFrontendService(
            self,
            "CtfFrontendService",
            cluster,
            frontend_task.task,
            sg,
        )

        CtfLoadBalancer(
            self,
            "CtfLoadBalancer",
            vpc,
            sg,
            load_balancer_target=frontend_service.service,
        )

        # CtfDatabase(self, vpc)
