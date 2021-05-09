from aws_cdk import (
    core,
    aws_lambda,
    aws_logs as logs,
)
from . import names


class CtfFunction(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        name,
        lambda_code_bucket,
        vpc,
        vpc_subnets,
        sg,
        timeout_seconds=30,
        memory_size_mb=128,
        env={},
    ):
        super().__init__(scope, id)

        self.stack_name = core.Stack.of(self).stack_name

        self.function = aws_lambda.Function(
            self,
            "function",
            function_name=f"{self.stack_name}-{name}",
            handler="app.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.from_bucket(
                bucket=lambda_code_bucket,
                key=f"{self.stack_name}/{name}.zip",
            ),
            environment=env,
            log_retention=logs.RetentionDays.ONE_WEEK,
            memory_size=memory_size_mb,
            timeout=core.Duration.seconds(timeout_seconds),
            retry_attempts=0,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            security_group=sg,
        )

        self.alias = aws_lambda.Alias(
            self,
            "alias",
            version=self.function.add_version("$LATEST"),
            description="initial release",
            alias_name=names.LAMBDA_RELEASE_ALIAS,
        )
