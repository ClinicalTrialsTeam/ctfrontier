import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import names
import click
from .common import deploy_docker_image


@click.group()
def container():
    pass


@container.command("deploy.frontend")
def deploy_frontend():
    deploy_docker_image(names.FRONTEND_REPOSITORY, "../../frontend")
