#!/usr/bin/env python3

from aws_cdk import core

from .stack import CtStack

app = core.App()
CtStack(
    app,
    "ct-frontier",
    # **stack_props,
    # env=core.Environment(account=aws_account_id(), region=AWS_REGION)
)

app.synth()
