from aws_cdk import (
    core,
    aws_lambda,
    aws_cloudwatch as cloudwatch,
    aws_logs as logs,
    aws_ecr as ecr,
)
from . import names


class RawDataDownloadFunction(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        monitoring,
        env,
    ):
        super().__init__(scope, id)

        self.stack_name = core.Stack.of(self).stack_name

        self.function = aws_lambda.Function(
            self,
            "function",
            function_name=f"{self.stack_name}-{names.RAW_DATA_DOWNLOAD_FUNCTION}",
            handler=aws_lambda.Handler.FROM_IMAGE,
            runtime=aws_lambda.Runtime.FROM_IMAGE,
            code=aws_lambda.Code.from_ecr_image(
                repository=ecr.Repository.from_repository_name(
                    self,
                    "LambdaRepository",
                    repository_name=names.LAMBDA_REPOSITORY,
                )
            ),
            environment=env,
            log_retention=logs.RetentionDays.ONE_WEEK,
            memory_size=128,
            timeout=core.Duration.seconds(30),
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
