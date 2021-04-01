import click
from lib import aws
from .common import profile_arg, run_command


@click.group()
def docker():
    pass


@docker.command("login")
def docker_login():
    """
    Get ECR password and login via docker
    """
    cmd = (
        f"aws {profile_arg()} ecr get-login-password --region {aws.AWS_REGION}"
        f" | docker login --username AWS --password-stdin {aws.AWS_ACCOUNT_ID}"
        f".dkr.ecr.{aws.AWS_REGION}.amazonaws.com"
    )
    run_command(cmd)
