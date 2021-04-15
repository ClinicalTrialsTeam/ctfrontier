from aws_cdk import (
    core,
    aws_ecs_patterns as ecs_patterns,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elb,
    aws_certificatemanager as acm,
)
from . import names


class CtfFrontendService(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        cluster,
        task_definition,
        vpc,
    ):
        super().__init__(scope, id)

        acm.Certificate(self, "CtfCertificate", "ctfrontier.com")

        lb = elb.NetworkLoadBalancer(
            self,
            "CtfNetworkLoadBalancer",
            vpc=vpc,
            internet_facing=True,
            load_balancer_name="ctf-load-balancer",
        )

        lb.add_listener(
            "CtfLoadBalancerListener",
            443,
            certificates=[],
            protocol=elb.Protocol.TLS,
        )

        # http redirect listener?

        frontend_service = ecs_patterns.NetworkLoadBalancedFargateService(
            self,
            id="CtfFrontendService",
            service_name=names.FRONTEND_SERVICE,
            cluster=cluster,  # Required
            load_balancer=lb,
            cloud_map_options=ecs.CloudMapOptions(name="frontend"),
            cpu=256,  # Default is 256
            desired_count=1,  # Default is 1
            task_definition=task_definition,
            memory_limit_mib=256,  # Default is 512
            listener_port=80,
            public_load_balancer=True,
            circuit_breaker=ecs.DeploymentCircuitBreaker(rollback=True),
        )

        # TODO: add 443, SSL, and redirect 80 to 443

        frontend_service.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "react inbound"
        )
