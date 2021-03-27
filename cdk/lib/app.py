#!/usr/bin/env python3

from aws_cdk import core
import boto3
import json
from .config import Param, STACK_TAGS
from .stack import CtStack

AWS_REGION = "us-east-1"
AWS_ACCOUNT = boto3.client("sts").get_caller_identity()["Account"]

stack_props = {
    "notification_email": Param("notification_email").getvalue(decrypt=True)
}

app = core.App()
CtStack(
    app,
    "ct-frontier",
    **stack_props,
    env=core.Environment(account=AWS_ACCOUNT, region=AWS_REGION),
    tags=STACK_TAGS
)

app.synth()
