from aws_cdk import (
    core,
    aws_iam as iam,
)
from .monitoring import CtfMonitoring
from .function import RawDataDownloadFunction
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
        CtfBucket(self, "RawDataFilesBucket", name=names.RAW_DATA_FILES_BUCKET)

        # Function to download files and save in S3
        data_download = RawDataDownloadFunction(
            self,
            "RawDataDownloadFunction",
            monitoring,
            env={"SSM_BASE_PATH": environment.SSM_BASE_PATH},
        )
        data_download.function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ssm:GetParameter"],
                resources=["*"],
            )
        )
