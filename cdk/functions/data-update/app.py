import logging
import aws_lambda_logging
from os import getenv

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

    logger.info(f"Sample lambda function log. DB_HOST={getenv('DB_HOST')}")

    response = {
        "statusCode": 200,
        "body": "Success",
    }
    return response
