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
        vpc,
    ):
        super().__init__(scope, id)

        # subnets?
        # s3 import buckets?
        rds.DatabaseInstance(
            self,
            "PostgresDatabase",
            database_name=names.DATABASE,
            instance_identifier=names.DATABASE_INSTANCE,
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2,
                ec2.InstanceSize.MICRO,
            ),
            vpc=vpc,
            vpc_subnets={"subnet_type": ec2.SubnetType.PRIVATE},
            storage_encrypted=True,
            allocated_storage=20,
            backup_retention=core.Duration.days(1),
            removal_policy=core.RemovalPolicy.SNAPSHOT,
        )


##         new DatabaseInstance(this, 'mysql-rds-instance', {
##     engine: DatabaseInstanceEngine.MYSQL,
##     instanceClass: InstanceType.of(InstanceClass.T2, InstanceSize.SMALL),
##     vpc: props.vpc,
# #    vpcPlacement: {subnetType: SubnetType.ISOLATED},
#     storageEncrypted: true,
#     multiAz: false,
#     autoMinorVersionUpgrade: false,
#     allocatedStorage: 25,
#     storageType: StorageType.GP2,
#     backupRetention: Duration.days(3),
#     deletionProtection: false,
#     masterUsername: 'Admin',
#     databaseName: 'Reporting',
#     masterUserPassword: this.secret.secretValue,
#     port: 3306
# });
