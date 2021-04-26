from aws_cdk import core, aws_ec2 as ec2
from .task import CtfFrontendTaskDefinition, CtfBackendTaskDefinition
from .service import CtfBackendService, CtfFrontendService
from .load_balancer import CtfLoadBalancer
from .cluster import CtfCluster
from .database import CtfDatabase
from . import names, aws


DB_PORT = 5432


class CtStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        site_domain,
        notification_email,
        django_secret,
        db_host,
        db_password,
        **kwargs,
    ) -> None:

        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "CtfVPC", max_azs=2)
        site_sg = ec2.SecurityGroup(
            self,
            "CtfFrontendSecurityGroup",
            allow_all_outbound=True,
            vpc=vpc,
        )
        database_sg = ec2.SecurityGroup(
            self,
            "CtfDatabaseSecurityGroup",
            allow_all_outbound=False,
            vpc=vpc,
        )
        preferred_az = f"{aws.AWS_REGION}a"

        ecs_cluster = CtfCluster(
            self,
            "CtfCluster",
            names.CLUSTER,
            vpc,
            site_sg,
            preferred_az,
        )

        frontend_port = 80
        frontend_task = CtfFrontendTaskDefinition(
            self,
            "FrontendTask",
            frontend_port,
        )
        frontend_service = CtfFrontendService(
            self,
            "CtfFrontendService",
            ecs_cluster.cluster,
            frontend_task.task,
            site_sg,
            preferred_az,
            port=frontend_port,
        )

        backend_task = CtfBackendTaskDefinition(
            self,
            "BackendTask",
            {
                "MODE": "prod",
                "DJANGO_SECRET": django_secret,
                "DB_HOST": db_host,
                "DB_PORT": "5432",
                "DB_PASSWORD": db_password,
                "SITE_DOMAIN": site_domain,
            },
        )
        backend_service = CtfBackendService(
            self,
            "CtfBackendService",
            ecs_cluster.cluster,
            backend_task.task,
            site_sg,
            preferred_az,
            frontend_service,
        )

        CtfLoadBalancer(
            self,
            "CtfLoadBalancer",
            site_domain,
            vpc,
            site_sg,
            frontend_target=frontend_service.service,
            backend_target=backend_service.service,
        )

        CtfDatabase(
            self,
            "PostgresDatabase",
            vpc,
            database_sg,
            preferred_az,
            backend_service,
            DB_PORT,
        )
