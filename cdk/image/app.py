import json
import logging
import aws_lambda_logging

aws_lambda_logging.setup(level="DEBUG", boto_level="CRITICAL")

logger = logging.getLogger()


def handler(event, context):
    logger.debug({"event": event, "context": context.__dict__})
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
