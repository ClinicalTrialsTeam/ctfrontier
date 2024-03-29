#!/usr/bin/env python3

from aws_cdk import core
import click
from .environment import Param
from .stack import CtStack
from . import names, aws


stack_props = {
    "site_domain": Param("site_domain").get_value(),
    "django_secret": Param("django_secret").get_value(decrypt=True),
    "db_host": Param("db_host").get_value(),
    "db_password": Param("db_password").get_value(decrypt=True),
    "es_host": Param("es_host").get_value(),
    "elasticsearch_enabled": Param("elasticsearch_enabled").get_value(),
}

app = core.App()

# warn if cdk is directly invoked
if app.node.try_get_context("CTF_CLI") != "true":
    click.secho(
        "WARNING: executing `cdk` commands directly is not recommended",
        fg="yellow",
    )

tags = {d["Key"]: d["Value"] for d in aws.STACK_TAGS}

CtStack(
    app,
    names.PROJECT_NAME,
    **stack_props,
    env=core.Environment(account=aws.AWS_ACCOUNT_ID, region=aws.AWS_REGION),
    tags=tags,
    synthesizer=core.DefaultStackSynthesizer(
        qualifier=names.PROJECT_NAME,
        file_assets_bucket_name=names.CDK_BOOTSTRAP_BUCKET,
    )
)

app.synth()
