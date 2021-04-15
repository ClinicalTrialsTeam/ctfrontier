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

        certificate = acm.Certificate(self, "CtfCertificate", names.DOMAIN)

        lb = elb.ApplicationLoadBalancer(
            self,
            "CtfNetworkLoadBalancer",
            vpc=vpc,
            internet_facing=True,
            load_balancer_name="ctf-load-balancer",
        )

        lb.apply_removal_policy(core.RemovalPolicy.DELETE)

        lb.add_listener(
            "CtfHttpRedirect",
            port=80,
            certificates=[certificate.certificate_arn],
            protocol=elb.Protocol.HTTP,
            default_action=elb.ListenerAction().redirect(
                permanent=True,
                port=443,
                protocol=elb.Protocol.HTTPS,
            ),
        )

        lb.add_listner(
            "CtfHttpsListener",
            port=443,
            certificates=[certificate.certificate_arn],
            protocol=elb.Protocol.HTTPS,
        )

        frontend_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            id="CtfFrontendService",
            domain_name=names.DOMAIN,
            service_name=names.FRONTEND_SERVICE,
            cluster=cluster,  # Required
            load_balancer=lb,
            cloud_map_options=ecs.CloudMapOptions(name="frontend"),
            desired_count=1,  # Default is 1
            task_definition=task_definition,
            circuit_breaker=ecs.DeploymentCircuitBreaker(rollback=True),
        )

        frontend_service.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "react inbound"
        )

        frontend_service.service.connections.allow_from_any_ipv4(
            ec2.Port.tcp(443), "react inbound tls"
        )
