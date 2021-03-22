from aws_cdk import (
    core,
    aws_ecr as ecr,
)
from . import names


class CtfImage(core.Construct):
    def __init__(self, scope: core.Construct, id: str, monitoring):
        repository = ecr.Repository()
