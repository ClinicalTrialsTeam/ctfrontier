import json
import logging
import aws_lambda_logging


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
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
    }
    logger.info(body)
    response = {
        "statusCode": 200,
        "body": json.dumps(body),
    }
    return response
