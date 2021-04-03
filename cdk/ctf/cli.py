import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import aws
import click
from .stack_commands import stack
from .config_commands import config
from .function_commands import function
from .common import profile_arg, run_command


@click.group()
def cli():
    pass


cli.add_command(stack)
cli.add_command(config)
cli.add_command(function)


@cli.group()
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
