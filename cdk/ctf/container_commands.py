import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import names
import click
from .common import profile_arg, deploy_docker_image, run_command


@click.group()
def container():
    pass


@container.command("frontend.update")
def update_frontend():
    deploy_docker_image(names.FRONTEND_REPOSITORY, "../frontend")


@container.command("frontend.deploy")
def deploy_frontend():
    # TODO: get the right version here
    cmd = (
        f"aws {profile_arg()} ecs update-service --cluster {names.CLUSTER} "
        f"--service {names.FRONTEND_SERVICE} "
        f"--task-definition {names.FRONTEND_TASK_FAMILY}:2 "
        f"--force-new-deployment"
    )
    run_command(cmd)
