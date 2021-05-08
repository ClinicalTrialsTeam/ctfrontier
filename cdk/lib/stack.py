from aws_cdk import core, aws_ec2 as ec2
from .task import CtfFargateTaskDefinition, CtfBackendTaskDefinition
from .service import CtfBackendService, CtfFrontendService
from .load_balancer import CtfLoadBalancer
from .cluster import CtfCluster
from .database import CtfDatabase
from .elasticsearch import CtfElasticsearch
from . import names, aws


class CtStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        site_domain,
        django_secret,
        db_host,
        db_password,
        **kwargs,
    ) -> None:

        super().__init__(scope, id, **kwargs)

        preferred_az = f"{aws.AWS_REGION}a"

        vpc = ec2.Vpc(
            self,
            "CtfVPC",
            max_azs=2,
            nat_gateways=1,
            nat_gateway_subnets=ec2.SubnetSelection(
                availability_zones=[preferred_az],
                subnet_type=ec2.SubnetType.PUBLIC,
            ),
        )
        site_sg = ec2.SecurityGroup(
            self,
            "CtfSiteSecurityGroup",
            allow_all_outbound=True,
            vpc=vpc,
        )
        database_sg = ec2.SecurityGroup(
            self,
            "CtfDatabaseSecurityGroup",
            allow_all_outbound=False,
            vpc=vpc,
        )

        ecs_cluster = CtfCluster(
            self,
            "CtfCluster",
            names.CLUSTER,
            vpc,
            site_sg,
            preferred_az,
        )

        frontend_task = CtfFargateTaskDefinition(
            self,
            "FrontendTask",
            names.FRONTEND_TASK_FAMILY,
            "FrontendContainer",
            "FrontendRespository",
            names.FRONTEND_REPOSITORY,
            mapped_port=80,
        )
        frontend_service = CtfFrontendService(
            self,
            "CtfFrontendService",
            names.FRONTEND_SERVICE,
            ecs_cluster.cluster,
            frontend_task.task,
            site_sg,
            preferred_az,
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
            port=80,
        )
        backend_service = CtfBackendService(
            self,
            "CtfBackendService",
            ecs_cluster.cluster,
            backend_task.task,
            site_sg,
            preferred_az,
            port=80,
        )

        CtfFargateTaskDefinition(
            self,
            "EtlTask",
            names.ETL_TASK_FAMILY,
            "EtlContainer",
            "EtlRepository",
            names.ETL_REPOSITORY,
            environment={
                "DB_HOST": db_host,
                "DB_PORT": "5432",
                "DB_PASSWORD": db_password,
            },
            cpu=2048,
            memory_limit=4096,
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
            db_port=5432,
        )

        CtfElasticsearch(self, "Elasticsearch", vpc, preferred_az, database_sg)
