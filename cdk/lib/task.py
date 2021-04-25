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
        id: str,
        port,
    ):

        super().__init__(scope, id)

        self.task = ecs.FargateTaskDefinition(
            self,
            id,
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
            port_mappings=[ecs.PortMapping(container_port=port)],
        )


class CtfBackendTaskDefinition(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        environment,
    ):

        super().__init__(scope, id)

        self.task = ecs.Ec2TaskDefinition(
            self,
            id,
            network_mode=ecs.NetworkMode.AWS_VPC,
            family=names.BACKEND_TASK_FAMILY,
        )

        container_id = "BackendContainer"
        environment["LOCALDOMAIN"] = "service.local"
        self.task.add_container(
            container_id,
            memory_reservation_mib=512,
            image=ecs.ContainerImage.from_ecr_repository(
                repository=ecr.Repository.from_repository_name(
                    self,
                    "BackendRepository",
                    repository_name=names.BACKEND_REPOSITORY,
                )
            ),
            essential=True,
            environment=environment,
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix=container_id,
                log_retention=logs.RetentionDays.ONE_WEEK,
            ),
            port_mappings=[ecs.PortMapping(container_port=80)],
        )
