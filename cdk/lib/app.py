#!/usr/bin/env python3

from aws_cdk import core
import click
from .environment import Param
from .stack import CtStack
from . import names, aws


stack_props = {
    "notification_email": Param("notification_email").getvalue(decrypt=True)
}

app = core.App()

# warn if cdk is directly invoked
if app.node.try_get_context("CTF_CLI") != "true":
    click.secho(
        "WARNING: executing `cdk` commands directly is not recommended",
        fg="yellow",
    )

CtStack(
    app,
    names.PROJECT_NAME,
    **stack_props,
    env=core.Environment(account=aws.AWS_ACCOUNT_ID, region=aws.AWS_REGION),
    tags=aws.STACK_TAGS,
    synthesizer=core.DefaultStackSynthesizer(
        qualifier=names.PROJECT_NAME,
        file_assets_bucket_name=names.CDK_BOOTSTRAP_BUCKET,
    )
)

app.synth()
