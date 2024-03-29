from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_s3 as s3,
)
from .task import CtfFargateTaskDefinition, CtfBackendTaskDefinition
from .service import CtfBackendService, CtfFrontendService
from .load_balancer import CtfLoadBalancer
from .cluster import CtfCluster
from .database import CtfDatabase
from .elasticsearch import CtfElasticsearch
from .function import CtfFunction
from . import names, aws

POSTGRES_PORT = 5432
ES_PORT = 443


class CtStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        site_domain,
        django_secret,
        db_host,
        db_password,
        es_host,
        elasticsearch_enabled,
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
            "FrontendRepository",
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
            vpc_subnets=ec2.SubnetSelection(availability_zones=[preferred_az]),
        )

        backend_task = CtfBackendTaskDefinition(
            self,
            "BackendTask",
            {
                "MODE": "prod",
                "DJANGO_SECRET": django_secret,
                "DB_HOST": db_host,
                "DB_PORT": str(POSTGRES_PORT),
                "DB_PASSWORD": db_password,
                "SITE_DOMAIN": site_domain,
                "ES_HOST": es_host,
                "ES_PORT": str(ES_PORT),
                "ELASTICSEARCH_ENABLED": elasticsearch_enabled,
            },
            port=80,
        )
        backend_service = CtfBackendService(
            self,
            "CtfBackendService",
            ecs_cluster.cluster,
            backend_task.task,
            site_sg,
            vpc_subnets=ec2.SubnetSelection(availability_zones=[preferred_az]),
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
                "DB_PORT": str(POSTGRES_PORT),
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

        postgres_database = CtfDatabase(
            self,
            "PostgresDatabase",
            vpc,
            database_sg,
            preferred_az,
            backend_service,
            db_port=POSTGRES_PORT,
        )

        ctf_elasticsearch = CtfElasticsearch(
            self,
            "Elasticsearch",
            vpc,
            preferred_az,
            database_sg,
            backend_service,
            es_port=ES_PORT,
        )

        # Give backend task permission to read/write elasticsearch
        ctf_elasticsearch.domain.grant_read_write(backend_task.task.task_role)

        lambda_code_bucket = s3.Bucket.from_bucket_name(
            self,
            "LambdaCodeBucket",
            names.LAMBDA_CODE_BUCKET,
        )

        # Function to download files and save in S3
        data_update = CtfFunction(
            self,
            "DataUpdateFunction",
            names.DATA_UPDATE_FUNCTION,
            lambda_code_bucket,
            vpc,
            ec2.SubnetSelection(availability_zones=[preferred_az]),
            database_sg,
            memory_size_mb=10240,  # max allowed
            timeout_seconds=900,  # max allowed
            env={
                "DB_HOST": db_host,
                "DB_PORT": str(POSTGRES_PORT),
                "DB_PASSWORD": db_password,
            },
        )

        # Give the lambda permission to connect to the database
        postgres_database.database.grant_connect(data_update.function)
