from aws_cdk import (
    core,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_logs as logs,
)
from . import names


class CtfFargateTaskDefinition(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        task_family_name,
        container_identifier,
        ecr_repository_identifier,
        ecr_repository_name,
        cpu=256,
        memory_limit=1024,
        environment={},
        mapped_port=None,
    ):

        super().__init__(scope, id)

        self.task = ecs.FargateTaskDefinition(
            self,
            id,
            family=task_family_name,
            cpu=cpu,
            memory_limit_mib=memory_limit,
        )

        port_mappings = None
        if mapped_port:
            port_mappings = [ecs.PortMapping(container_port=mapped_port)]

        self.task.add_container(
            container_identifier,
            image=ecs.ContainerImage.from_ecr_repository(
                repository=ecr.Repository.from_repository_name(
                    self,
                    ecr_repository_identifier,
                    repository_name=ecr_repository_name,
                )
            ),
            essential=True,
            environment=environment,
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix=container_identifier,
                log_retention=logs.RetentionDays.ONE_WEEK,
            ),
            port_mappings=port_mappings,
        )


class CtfFrontendTaskDefinition(CtfFargateTaskDefinition):
    pass


class CtfBackendTaskDefinition(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        environment,
        port,
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
            port_mappings=[ecs.PortMapping(container_port=port)],
        )
