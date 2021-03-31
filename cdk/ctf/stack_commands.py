import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import environment, names, aws
import click
import json
import subprocess
from .common import (
    run_cdk_command,
    run_command,
    profile_arg,
    deploy_docker_image,
)
from .config_commands import Config
from .function_commands import function_deploy


@click.group()
def stack():
    pass


@stack.command("create")
@click.option(
    "--config-file",
    prompt=(
        "Initial config filename "
        "(Note: editing config can only be done with 'ctf config-edit')"
    ),
    help="Provide and initial config file",
)
@click.pass_context
def stack_create(ctx, config_file):
    """
    Create a new CloudFormation stack
    """
    if not config_file.strip():
        click.echo("Missing initial config file!")
        raise click.Abort()

    click.secho(
        "Warning: creating a new stack will overwrite any existing "
        f"AWS SSM params in the path: {environment.SSM_BASE_PATH}",
        fg="yellow",
    )
    if not click.confirm("Create a new stack?"):
        return

    Config.delete()
    Config.new(config_file)

    __bootstrap_cdk()
    __bootstrap_ecr()
    deploy_docker_image()

    try:
        ctx.invoke(stack_update, ctx, False)
    except Exception:
        Config.delete()
        click.secho("Error creating stack", fg="red")
        raise click.Abort()


@stack.command("update")
@click.pass_context
def stack_update(ctx, update_containers=True):
    """
    Update the existing CloudFormation stack
    """
    run_cdk_command("deploy")

    if update_containers:
        ctx.invoke(function_deploy)


@stack.command("diff")
def stack_diff():
    """
    Compares the specified stack with the deployed stack
    """
    run_cdk_command("diff")


@stack.command("delete")
def stack_delete():
    """
    Delete the CloudFormation stack
    """
    run_cdk_command("destroy")

    __delete_ecr_bootstrap()
    __delete_bootstrap_cdk()


@stack.command("synth")
def stack_synth():
    """
    Synthesize and print CloudFormation template
    """
    run_cdk_command("synth")


@stack.command("list")
def stack_list():
    """
    Lists the stacks in the app
    """
    run_cdk_command("list")


"""
Private functions
"""


def __bootstrap_ecr():

    # Create ECR repository
    tags = ""
    for key, val in aws.STACK_TAGS.items():
        tags += f"Key={key},Value={val} "
    cmd = (
        f"aws ecr create-repository --repository-name {names.LAMBDA_REPOSITORY}"
        f" --image-scanning-configuration scanOnPush=true --tags {tags} "
        f"{profile_arg()}"
    )
    run_command(cmd)


def __delete_ecr_bootstrap():
    # Find and all ECR repository images
    cmd = (
        f"aws ecr list-images --repository-name "
        f"{names.LAMBDA_REPOSITORY} {profile_arg()}"
    )
    click.echo(cmd)
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    images = json.loads(output.communicate()[0])["imageIds"]

    # Clear ECR repository images
    if images:
        click.echo(images)
        image_digests = ""
        for image in images:
            image_digests += f" imageDigest={image['imageDigest']}"
        cmd = (
            f"aws ecr batch-delete-image --repository-name"
            f" {names.LAMBDA_REPOSITORY} --image-ids {image_digests} "
            f"{profile_arg()}"
        )
        run_command(cmd)

    # Delete ECR repository
    cmd = (
        f"aws ecr delete-repository "
        f"--repository-name {names.LAMBDA_REPOSITORY} {profile_arg()}"
    )
    run_command(cmd)


def __bootstrap_cdk():
    tags_args = ""
    for key, val in aws.STACK_TAGS.items():
        tags_args += f"--tags {key}={val} "
    r = run_cdk_command(
        f"bootstrap --bootstrap-bucket-name {names.CDK_BOOTSTRAP_BUCKET} "
        f"--qualifier {names.PROJECT_NAME} {tags_args}"
    )
    if r != 0:
        click.secho("Error boostrapping environment", fg="red")
        raise click.Abort()


def __delete_bootstrap_cdk():
    bootstrap_repository_name = (
        f"cdk-{names.PROJECT_NAME}-container-assets-"
        f"{aws.AWS_ACCOUNT_ID}-{aws.AWS_REGION}"
    )

    # Empty boostrap S3 bucket
    cmd = (
        f"aws {profile_arg()} s3 rm --recursive "
        f"s3://{names.CDK_BOOTSTRAP_BUCKET}"
    )
    run_command(cmd)

    # Find all bootstrapped ECR repository images
    cmd = (
        f"aws ecr list-images --repository-name {bootstrap_repository_name} "
        f"{profile_arg()}"
    )
    click.echo(cmd)
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    images = json.loads(output.communicate()[0])["imageIds"]

    # Clear ECR repository images
    if images:
        image_tags = ""
        for image in images:
            image_tags += f" imageTag={image['imageTag']}"
        cmd = (
            f"aws ecr batch-delete-image --repository-name"
            f" {bootstrap_repository_name} --image-ids {image_tags}"
        )
        run_command(cmd)

    # Delete bootstrap stack
    cmd = (
        "aws cloudformation delete-stack "
        f"--stack-name CDKToolkit {profile_arg()}"
    )
    run_command(cmd)

    # Delete bootstrap S3 bucket
    cmd = (
        f"aws s3api delete-bucket --bucket {names.CDK_BOOTSTRAP_BUCKET} "
        f"{profile_arg()}"
    )
    run_command(cmd)
