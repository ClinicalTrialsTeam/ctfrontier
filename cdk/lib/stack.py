from aws_cdk import core, aws_iam as iam


class CtStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:

        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
