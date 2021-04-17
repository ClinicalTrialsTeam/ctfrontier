from aws_cdk import (
    core,
    aws_ecs as ecs,
    aws_ec2 as ec2,
)
from . import names


class CtfFrontendService(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        cluster,
        task_definition,
        sg,
    ):
        super().__init__(scope, id)

        self.service = ecs.FargateService(
            self,
            id=id,
            service_name=names.FRONTEND_SERVICE,
            security_groups=[sg],
            cluster=cluster,
            cloud_map_options=ecs.CloudMapOptions(name="frontend"),
            desired_count=1,
            task_definition=task_definition,
            circuit_breaker=ecs.DeploymentCircuitBreaker(rollback=True),
        )

        self.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "react inbound"
        )

        self.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(443), "react inbound https"
        )
