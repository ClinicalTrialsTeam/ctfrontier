from aws_cdk import (
    core,
    aws_rds as rds,
    aws_ec2 as ec2,
)
from . import names


class CtfDatabase(core.Construct):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        vpc,
        sg,
        preferred_az,
    ):
        super().__init__(scope, id)

        # credentials - let secrets manager generate a password?
        # s3 import buckets...
        # postgres data dump is only 1.24 GB... load via ssh?
        # set backup retention to 0
        rds.DatabaseInstance(
            self,
            id,
            database_name=names.DATABASE,
            instance_identifier=names.DATABASE_INSTANCE,
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            instance_type=ec2.InstanceType("t2.micro"),
            vpc=vpc,
            vpc_subnets={"subnet_type": ec2.SubnetType.PRIVATE},
            security_groups=[sg],
            availability_zone=preferred_az,
            storage_encrypted=False,  # db.t2.micro does not support encryption at rest
            allocated_storage=20,
            backup_retention=core.Duration.days(1),
            delete_automated_backups=True,
            removal_policy=core.RemovalPolicy.SNAPSHOT,
        )
