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
        load_balancer_target,
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

        target_group = elb.ApplicationTargetGroup(
            self,
            "TargetGroup",
            port=80,
            protocol=elb.ApplicationProtocol.HTTP,
            targets=[load_balancer_target],
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

        lb.add_listener(
            "CtfHttpsListener",
            port=443,
            certificates=[certificate],
            protocol=elb.Protocol.HTTPS,
            default_target_groups=[target_group],
        )

        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
        )

        sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
        )
