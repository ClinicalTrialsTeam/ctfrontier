import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import aws
import click
import subprocess
import base64
import json


def profile_arg():
    if aws.AWS_PROFILE is not None:
        return f"--profile {aws.AWS_PROFILE}"
    return ""


def run_cdk_command(cmd):
    full_cmd = f"cdk {cmd} -c CTF_CLI=true {profile_arg()}"
    return run_command(full_cmd)


def run_command(cmd, capture_output=False, text=False):
    click.echo(cmd)
    r = subprocess.run(cmd.split(), capture_output=capture_output, text=text)
    if r.returncode != 0:
        raise click.Abort()
    return r


def base64_encode_dict(d):
    return base64.b64encode(json.dumps(d).encode()).decode()


def get_image_uri(repository):
    return (
        f"{aws.AWS_ACCOUNT_ID}.dkr.ecr.{aws.AWS_REGION}"
        f".amazonaws.com/{repository}:latest"
    )


def get_image_id(image_uri, running=False):
    # Get image id
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


def build_docker_image(image_uri, dockerfile_folder):
    # Build docker image
    cmd = f"docker build -t {image_uri} image"
    click.echo(cmd)
    r = subprocess.run(cmd.split())
    if r.returncode != 0:
        raise click.Abort()


def deploy_docker_image(repository, dockerfile_folder):
    image_uri = get_image_uri(repository)

    build_docker_image(image_uri, dockerfile_folder)

    # Tag docker image
    cmd = f"docker tag {get_image_id(image_uri)} {image_uri}"
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
        click.secho(
            "Error pushing docker image. Try `ctf docker login` ?",
            fg="red",
        )
        raise click.Abort()
