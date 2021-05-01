import click
import subprocess
from lib import aws
from .common import profile_arg


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
    res = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = res.communicate()[0]
    click.echo(output)
