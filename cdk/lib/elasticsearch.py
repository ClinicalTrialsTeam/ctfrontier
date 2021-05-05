from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_elasticsearch as es,
)


class CtfElasticsearch(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        vpc,
        preferred_az,
        database_sg,
    ):
        super().__init__(scope, id)

        es.Domain(
            self,
            "Domain",
            version=es.ElasticsearchVersion.V7_9,
            enable_version_upgrade=True,
            capacity=es.CapacityConfig(
                data_node_instance_type="t2.small.elasticsearch",  # free tier
            ),
            ebs=es.EbsOptions(
                volume_size=10,  # free tier allowance 10GB
                volume_type=ec2.EbsDeviceVolumeType.GP2,
            ),
            logging=es.LoggingOptions(
                app_log_enabled=True,
                slow_index_log_enabled=True,
                slow_search_log_enabled=True,
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
            security_groups=[database_sg],
            vpc=vpc,
            vpc_subnets=[
                ec2.SubnetSelection(
                    availability_zones=[preferred_az],
                    subnet_type=ec2.SubnetType.PRIVATE,
                )
            ],
        )
