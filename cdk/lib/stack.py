from aws_cdk import core, aws_s3 as s3
from .monitoring import CtfMonitoring
from .function import RawDataDownloadFunction
from .bucket import CtfBucket
from . import names


class CtStack(core.Stack):
    def __init__(
        self, scope: core.Construct, id: str, notification_email, **kwargs
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

        # S3 bucket to store the lambda deployment package in
        lambda_code_bucket = CtfBucket(
            self, "LambdaCodeBucket", name=names.LAMBDA_CODE_BUCKET
        )

        # Function to download files and save in S3
        RawDataDownloadFunction(lambda_code_bucket, monitoring)
