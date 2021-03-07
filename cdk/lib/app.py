#!/usr/bin/env python3

from aws_cdk import core

from .stack import CtStack


app = core.App()
CtStack(app, "cdk-project")

app.synth()
