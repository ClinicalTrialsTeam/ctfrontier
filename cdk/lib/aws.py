import boto3
from os import getenv, putenv
from os.path import join, dirname
from dotenv import load_dotenv


# load dotenv
dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

AWS_PROFILE = getenv("AWS_PROFILE")
AWS_REGION = "us-east-1"
AWS_ACCOUNT_ID = boto3.client("sts").get_caller_identity()["Account"]

STACK_TAGS = {
    "Key": "project",
    "Value": "CTF",
}

putenv("CDK_NEW_BOOTSTRAP", "1")
