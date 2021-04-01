"""
Download clinicaltrials.gov data and stream to S3.
Multithreaded streaming code from:
https://github.com/harvard-dce/zoom-recording-ingester
"""


import logging
import aws_lambda_logging
import boto3
import requests
import concurrent.futures
from os import getenv as env

MIN_CHUNK_SIZE = 5242880
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

    # get ssm param
    url = get_param("clinicaltrials_data_url")
    logger.info(f"Get file from url: {url}")

    stream_file_to_s3(url)

    logger.info(f"Completed upload to {RAW_DATA_FILES_BUCKET}")

    response = {
        "statusCode": 200,
        "body": url,
    }
    return response


def stream_file_to_s3(url):
    s3 = boto3.client("s3")
    s3_filename = url.split("/")[-1]

    logger.info(
        f"Stream {s3_filename} from {url} to bucket: {RAW_DATA_FILES_BUCKET}"
    )
    parts = []
    mpu = s3.create_multipart_upload(
        Bucket=RAW_DATA_FILES_BUCKET,
        Key=s3_filename,
    )

    stream = requests.get(url, stream=True)

    try:
        chunks = enumerate(stream.iter_content(chunk_size=MIN_CHUNK_SIZE), 1)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_map = {}
            for part_number, chunk in chunks:
                f = executor.submit(
                    upload_part,
                    s3,
                    s3_filename,
                    mpu["UploadId"],
                    part_number,
                    chunk,
                )
                future_map[f] = part_number

            for future in concurrent.futures.as_completed(future_map):
                part_number = future_map[future]
                part = future.result()
                parts.append({"PartNumber": part_number, "ETag": part["ETag"]})

        # complete_multipart_upload requires parts in order by part number
        parts = sorted(parts, key=lambda i: i["PartNumber"])

        s3.complete_multipart_upload(
            Bucket=RAW_DATA_FILES_BUCKET,
            Key=s3_filename,
            UploadId=mpu["UploadId"],
            MultipartUpload={"Parts": parts},
        )
        print(f"Completed multipart upload of {s3_filename}.")
    except Exception as e:
        logger.exception(
            f"Something went wrong with upload of {s3_filename}:{e}"
        )
        s3.abort_multipart_upload(
            Bucket=RAW_DATA_FILES_BUCKET,
            Key=s3_filename,
            UploadId=mpu["UploadId"],
        )
        raise


def upload_part(s3, s3_filename, upload_id, part_number, chunk):
    part = s3.upload_part(
        Body=chunk,
        Bucket=RAW_DATA_FILES_BUCKET,
        Key=s3_filename,
        PartNumber=part_number,
        UploadId=upload_id,
    )
    return part
