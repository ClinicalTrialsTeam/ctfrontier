import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

import json
import click
from lib import names
from .common import profile_arg, deploy_docker_image, run_command


@click.group()
def container():
    pass


@container.command("frontend.update")
def update_frontend():
    deploy_docker_image(names.FRONTEND_REPOSITORY, "../frontend")


@container.command("frontend.deploy")
def deploy_frontend():
    cmd = (
        f"aws ecs {profile_arg()} list-task-definitions "
        f"--family-prefix {names.FRONTEND_TASK_FAMILY}"
    )
    r = run_command(cmd, capture_output=True)
    task_def = json.loads(r.stdout)["taskDefinitionArns"][0].split("/")[-1]

    cmd = (
        f"aws {profile_arg()} ecs update-service --cluster {names.CLUSTER} "
        f"--service {names.FRONTEND_SERVICE} --task-definition {task_def} "
        f"--force-new-deployment"
    )
    run_command(cmd, capture_output=True)
