import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

import json
import click
import subprocess
from lib import aws, names, environment
from .docker_commands import docker_login
from .common import profile_arg, run_command


FRONTEND_PATH = join(dirname(__file__), "../../frontend")
BACKEND_PATH = join(dirname(__file__), "../../backend")
ETL_PATH = join(dirname(__file__), "../../etl")


@click.group()
def container():
    pass


@container.command("build.frontend")
def build_frontend():
    build_docker_image(
        names.FRONTEND_REPOSITORY,
        FRONTEND_PATH,
        additional_args=f"--build-arg REACT_APP_API_BASE_URL={environment.Param('site_domain').get_value()}",
    )


@container.command("build.backend")
def build_backend():
    build_docker_image(names.BACKEND_REPOSITORY, BACKEND_PATH)


@container.command("build.etl")
def build_etl():
    build_docker_image(names.ETL_REPOSITORY, ETL_PATH)


@container.command("deploy.frontend")
@click.pass_context
def deploy_frontend(ctx):
    ctx.invoke(docker_login)
    build_docker_image(names.FRONTEND_REPOSITORY, FRONTEND_PATH)
    push_docker_image(names.FRONTEND_REPOSITORY)
    deploy_docker_image(names.FRONTEND_SERVICE, names.FRONTEND_TASK_FAMILY)


@container.command("deploy.etl")
@click.pass_context
def deploy_etl(ctx):
    ctx.invoke(docker_login)
    build_docker_image(names.ETL_REPOSITORY, ETL_PATH)
    push_docker_image(names.ETL_REPOSITORY)
    deploy_docker_image(names.ETL_SERVICE, names.ETL_TASK_FAMILY)


@container.command("deploy.backend")
@click.pass_context
def deploy_backend(ctx):
    ctx.invoke(docker_login)
    build_docker_image(names.BACKEND_REPOSITORY, BACKEND_PATH)
    push_docker_image(names.BACKEND_REPOSITORY)
    deploy_docker_image(names.BACKEND_SERVICE, names.BACKEND_TASK_FAMILY)


def __get_image_uri(repository):
    return (
        f"{aws.AWS_ACCOUNT_ID}.dkr.ecr.{aws.AWS_REGION}"
        f".amazonaws.com/{repository}:latest"
    )


def __get_image_id(image_uri, running=False):
    if running:
        docker_command = "ps"
        filter_by = "ancestor"
    else:
        docker_command = "images"
        filter_by = "reference"
    cmd = f"docker {docker_command} -q --filter={filter_by}='{image_uri}'"
    click.echo(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if p.wait() != 0:
        click.secho("Error getting docker image id", fg="red")
        raise click.Abort()
    return p.communicate()[0].decode()


def build_docker_image(repository, dockerfile_folder, additional_args=""):
    image_uri = __get_image_uri(repository)
    # Build docker image
    cmd = f"docker build -t {image_uri} {dockerfile_folder} {additional_args}"
    click.echo(cmd)
    r = subprocess.run(cmd.split())
    if r.returncode != 0:
        raise click.Abort()


def push_docker_image(repository):
    image_uri = __get_image_uri(repository)

    # Tag docker image
    cmd = f"docker tag {__get_image_id(image_uri)} {image_uri}"
    click.echo(cmd)
    r = subprocess.run(cmd.split(), capture_output=True)
    if r.returncode != 0:
        click.secho(
            f"Error tagging docker image: {r.stderr.decode()}", fg="red"
        )
        raise click.Abort()

    # Push docker image to repository
    cmd = f"docker push {image_uri}"
    click.echo(cmd)
    r = subprocess.run(cmd.split())
    if r.returncode != 0:
        raise click.Abort()


def deploy_docker_image(ecs_service, ecs_task_family):
    cmd = (
        f"aws ecs {profile_arg()} list-task-definitions "
        f"--family-prefix {ecs_task_family}"
    )
    r = run_command(cmd, capture_output=True)
    task_def = json.loads(r.stdout)["taskDefinitionArns"][0].split("/")[-1]

    cmd = (
        f"aws {profile_arg()} ecs update-service --cluster {names.CLUSTER} "
        f"--service {ecs_service} --task-definition {task_def} "
        f"--force-new-deployment"
    )
    run_command(cmd, capture_output=True)
