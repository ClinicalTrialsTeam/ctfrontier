import logging
import aws_lambda_logging
import boto3
from os import getenv as env


SSM_BASE_PATH = env("SSM_BASE_PATH")

logger = logging.getLogger()


def setup_logging(event, context):
    aws_lambda_logging.setup(
        level="DEBUG",
        boto_level="CRITICAL",
        aws_request_id=context.aws_request_id,
    )
    logger.debug({"event": event, "context": context.__dict__})


def handler(event, context):
    setup_logging(event, context)
    param_name = "/ctfrontier/clinicaltrials_data_url"
    logger.debug(f"getting ssm param {param_name}")

    # get ssm param
    ssm = boto3.client("ssm", region_name="us-east-1")
    r = ssm.get_parameter(Name=param_name)
    logger.info(r)
    url = r["Parameter"]["Value"]

    response = {
        "statusCode": 200,
        "body": url,
    }
    return response
