# from os.path import join, dirname
# from aws_cdk import (
#     core,
#     aws_ecr as ecr,
#     aws_ecr_assets as ecr_assets,
#     aws_ecs as ecs,
# )
# from . import names


# class CtfRepository(core.Construct):
#     def __init__(self, scope: core.Construct, id: str, name):
#         self.repository = ecr.Repository(
#             self,
#             "repository",
#             image_scan_on_push=True,
#             image_tag_mutability=ecr.TagMutability.MUTABLE,
#             removal_policy=core.RemovalPolicy.DESTROY,
#             repository_name=name,
#         )

#         asset = ecr_assets.DockerImageAsset(
#             self,
#             "MyBuildImage",
#             directory=join(dirname(__file__), "../images"),
#         )

#         ecs.ContainerImage.from_docker_image_asset(asset=asset)
