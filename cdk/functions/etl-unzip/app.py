"""
Download clinicaltrials.gov data and stream to S3.
Multithreaded streaming code from:
https://github.com/harvard-dce/zoom-recording-ingester
"""


import logging
import aws_lambda_logging
import boto3
from io import BytesIO
import zipfile
from os import getenv as env


SSM_BASE_PATH = env("SSM_BASE_PATH")
RAW_DATA_FILES_BUCKET = env("RAW_DATA_FILES_BUCKET")

logger = logging.getLogger()


def setup_logging(event, context):
    aws_lambda_logging.setup(
        level="DEBUG",
        boto_level="CRITICAL",
        aws_request_id=context.aws_request_id,
    )
    logger.debug({"event": event, "context": context.__dict__})


def get_param(key):
    ssm = boto3.client("ssm", region_name="us-east-1")
    r = ssm.get_parameter(Name=f"{SSM_BASE_PATH}/{key}")
    return r["Parameter"]["Value"]


def handler(event, context):
    setup_logging(event, context)

    unzip_files_to_s3(url)

    logger.info(f"Completed upload to {RAW_DATA_FILES_BUCKET}")

    response = {
        "statusCode": 200,
        "body": "Completed unzip",
    }
    return response


def unzip_files_to_s3():
    # Source: https://medium.com/@johnpaulhayes/how-extract-a-huge-zip-file-in-an-amazon-s3-bucket-by-using-aws-lambda-and-python-e32c6cf58f06

    s3_resource = boto3.resource("s3")
    zip_obj = s3_resource.Object(bucket_name="bucket_name_here", key=zip_key)
    buffer = BytesIO(zip_obj.get()["Body"].read())

    z = zipfile.ZipFile(buffer)
    for filename in z.namelist():
        file_info = z.getinfo(filename)
        s3_resource.meta.client.upload_fileobj(
            z.open(filename), Bucket=bucket, Key=f"{filename}"
        )
