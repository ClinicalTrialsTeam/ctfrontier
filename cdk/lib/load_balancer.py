from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elb,
    aws_certificatemanager as acm,
)


class CtfLoadBalancer(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        site_domain,
        vpc,
        sg,
        frontend_target,
        backend_target,
    ):
        super().__init__(scope, id)

        certificate = acm.Certificate(
            self,
            "CtfCertificate",
            domain_name=f"*.{site_domain}",
        )

        lb = elb.ApplicationLoadBalancer(
            self,
            "CtfNetworkLoadBalancer",
            vpc=vpc,
            security_group=sg,
            internet_facing=True,
            load_balancer_name="ctf-load-balancer",
        )

        lb.apply_removal_policy(core.RemovalPolicy.DESTROY)

        frontend_target_group = elb.ApplicationTargetGroup(
            self,
            "FrontendTargetGroup",
            port=80,
            protocol=elb.ApplicationProtocol.HTTP,
            targets=[frontend_target],
            vpc=vpc,
        )

        backend_target_group = elb.ApplicationTargetGroup(
            self,
            "BackendTargetGroup",
            port=80,
            protocol=elb.ApplicationProtocol.HTTP,
            health_check=elb.HealthCheck(path="/ctgov/api/healthz", port="80"),
            targets=[backend_target],
            vpc=vpc,
        )

        lb.add_listener(
            "CtfHttpRedirect",
            port=80,
            protocol=elb.Protocol.HTTP,
            default_action=elb.ListenerAction.redirect(
                permanent=True,
                port="443",
                protocol="HTTPS",
            ),
        )

        https_listener = lb.add_listener(
            "CtfHttpsListener",
            port=443,
            certificates=[certificate],
            protocol=elb.Protocol.HTTPS,
            default_target_groups=[
                frontend_target_group,
                backend_target_group,
            ],
        )

        https_listener.add_action(
            "CtfFrontendRule",
            action=elb.ListenerAction.forward(
                target_groups=[frontend_target_group]
            ),
        )

        https_listener.add_action(
            "CtfApiRule",
            priority=10,
            action=elb.ListenerAction.forward(
                target_groups=[backend_target_group]
            ),
            conditions=[
                elb.ListenerCondition.path_patterns(
                    values=["/ctgov/api/*", "/logger"]
                )
            ],
        )

        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
        )

        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
        )
