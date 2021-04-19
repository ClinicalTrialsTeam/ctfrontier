from aws_cdk import (
    core,
    aws_ecs as ecs,
    aws_ec2 as ec2,
)
from . import names

FRONTEND_PORT = 80
BACKEND_PORT = 8000


class CtfFrontendService(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        cluster,
        task_definition,
        sg,
        preferred_az,
        port,
    ):
        super().__init__(scope, id)

        self.service = ecs.FargateService(
            self,
            id=id,
            service_name=names.FRONTEND_SERVICE,
            security_groups=[sg],
            vpc_subnets=ec2.SubnetSelection(availability_zones=[preferred_az]),
            cluster=cluster,
            # cloud_map_options=ecs.CloudMapOptions(name="frontend"),
            desired_count=1,
            task_definition=task_definition,
            circuit_breaker=ecs.DeploymentCircuitBreaker(rollback=True),
        )

        self.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(port), "react inbound"
        )

        self.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(443), "react inbound https"
        )


class CtfBackendService(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        cluster,
        task_definition,
        sg,
        preferred_az,
        frontend_service,
        port,
    ):
        super().__init__(scope, id)

        self.service = ecs.Ec2Service(
            self,
            id=id,
            service_name=names.BACKEND_SERVICE,
            security_groups=[sg],
            vpc_subnets=ec2.SubnetSelection(availability_zones=[preferred_az]),
            cluster=cluster,
            task_definition=task_definition,
            desired_count=1,
            circuit_breaker=ecs.DeploymentCircuitBreaker(rollback=True),
        )

        self.service.connections.allow_from(
            frontend_service.service, ec2.Port.tcp(port)
        )
