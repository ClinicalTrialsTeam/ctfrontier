from aws_cdk import (
    core,
    aws_ecs as ecs,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
)
from . import names


class CtfCluster(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        cluster_name,
        vpc,
        backend_sg,
        preferred_az,
    ):
        super().__init__(scope, id)

        self.cluster = ecs.Cluster(
            self,
            "CtfCluster",
            cluster_name=cluster_name,
            vpc=vpc,
        )
        self.cluster.add_default_cloud_map_namespace(name="service.local")
        self.cluster.apply_removal_policy(core.RemovalPolicy.DESTROY)

        auto_scaling_group = self.cluster.add_capacity(
            "CtfAutoScaling",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image_type=ecs.MachineImageType.AMAZON_LINUX_2,
            instance_monitoring=autoscaling.Monitoring.BASIC,
            task_drain_time=core.Duration.minutes(0),
            key_name=names.BACKEND_KEY_PAIR,
            max_capacity=1,
            vpc_subnets=ec2.SubnetSelection(
                availability_zones=[preferred_az],
                subnet_type=ec2.SubnetType.PUBLIC,
            ),
        )

        auto_scaling_group.add_security_group(backend_sg)

        core.CfnOutput(
            self,
            "CfnECSClusterName",
            export_name="cfn-ecs-cluster-name",
            value=self.cluster.cluster_name,
        )
