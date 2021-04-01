from aws_cdk import (
    core,
    aws_lambda,
    aws_cloudwatch as cloudwatch,
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
        monitoring,
        timeout_seconds=30,
        memory_size=128,
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
            memory_size=memory_size,
            timeout=core.Duration.seconds(timeout_seconds),
            retry_attempts=0,
        )

        self.alias = aws_lambda.Alias(
            self,
            "alias",
            version=self.function.add_version("$LATEST"),
            description="initial release",
            alias_name=names.LAMBDA_RELEASE_ALIAS,
        )

        errors_alarm = cloudwatch.Alarm(
            self,
            "ErrorsAlarm",
            metric=self.function.metric_errors(),
            alarm_name=f"{self.function.function_name}-errors",
            statistic="sum",
            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            threshold=1,
            period=core.Duration.minutes(1),
            evaluation_periods=1,
        )
        monitoring.add_alarm_action(errors_alarm)
