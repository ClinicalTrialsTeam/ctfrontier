from aws_cdk import (
    core,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_logs as logs,
)
from . import names


class CtfFrontendTaskDefinition(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
    ):

        super().__init__(scope, id)

        self.task = ecs.FargateTaskDefinition(
            self,
            "FrontendTask",
            family=names.FRONTEND_TASK_FAMILY,
            cpu=256,
            memory_limit_mib=1024,
        )

        self.task.add_container(
            "FrontendContainer",
            image=ecs.ContainerImage.from_ecr_repository(
                repository=ecr.Repository.from_repository_name(
                    self,
                    "FrontendRepository",
                    repository_name=names.FRONTEND_REPOSITORY,
                )
            ),
            essential=True,
            environment={"LOCALDOMAIN": "service.local"},
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix="FrontendContainer",
                log_retention=logs.RetentionDays.ONE_WEEK,
            ),
            port_mappings=[ecs.PortMapping(container_port=80)],
        )
