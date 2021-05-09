from aws_cdk import (
    core,
    aws_rds as rds,
    aws_ec2 as ec2,
    aws_secretsmanager as secretsmanager,
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
        backend_service,
        db_port,
    ):
        super().__init__(scope, id)

        self.database = rds.DatabaseInstance(
            self,
            id,
            database_name=names.DATABASE,
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            instance_type=ec2.InstanceType("t3.small"),
            credentials=rds.Credentials.from_secret(
                secret=secretsmanager.Secret.from_secret_name(
                    self,
                    "CtfDatabaseSecret",
                    secret_name=names.DATABASE_SECRET,
                ),
            ),
            vpc=vpc,
            vpc_subnets={"subnet_type": ec2.SubnetType.PRIVATE},
            security_groups=[sg],
            availability_zone=preferred_az,
            storage_encrypted=False,  # db.t2.micro does not support encryption at rest
            enable_performance_insights=True,
            allocated_storage=30,
            backup_retention=core.Duration.days(1),
            delete_automated_backups=True,
            removal_policy=core.RemovalPolicy.SNAPSHOT,
        )

        self.database.connections.allow_from(
            backend_service.service, ec2.Port.tcp(db_port)
        )

        core.CfnOutput(
            self,
            "CfnDatabaseEndpoint",
            export_name="cfn-database-endpoint",
            value=self.database.db_instance_endpoint_address,
        )

        core.CfnOutput(
            self,
            "CfnDatabasePort",
            export_name="cfn-database-port",
            value=self.database.db_instance_endpoint_port,
        )

        core.CfnOutput(
            self,
            "CfnDatabaseInstanceIdentifier",
            export_name="cfn-database-identifier",
            value=self.database.instance_identifier,
        )
