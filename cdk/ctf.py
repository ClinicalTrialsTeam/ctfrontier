import click
import json
from lib import config, names, aws
import subprocess
from os import getenv, putenv
from os.path import join, dirname
from dotenv import load_dotenv


# load dotenv
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

AWS_PROFILE = getenv("AWS_PROFILE")
putenv("CDK_NEW_BOOTSTRAP", "1")


def profile_arg():
    if AWS_PROFILE is not None:
        return f"--profile {AWS_PROFILE}"
    return ""


def cdk_cmd(cmd):
    full_cmd = f"cdk {cmd} -c CTF_CLI=true {profile_arg()}"
    return subprocess.call(full_cmd.split())


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option(
    "--config-file",
    prompt="Initial config filename",
    help="Provide and initial config file",
)
@click.pass_context
def stack_create(ctx, config_file):
    """
    Create a new CloudFormation stack
    """
    click.secho(
        "Warning: creating a new stack will overwrite any existing "
        f"AWS SSM params in the path: {config.SSM_BASE_PATH}",
        fg="yellow",
    )
    if not click.confirm("Create a new stack?"):
        return

    config.delete()
    config.new(config_file)

    tags_args = ""
    for key, val in config.STACK_TAGS.items():
        tags_args += f"--tags {key}={val} "
    r = cdk_cmd(
        f"bootstrap --bootstrap-bucket-name {names.CDK_BOOTSTRAP_BUCKET} "
        f"--qualifier {names.PROJECT_NAME} {tags_args}"
    )
    if r != 0:
        click.secho("Error boostrapping environment", fg="red")
        raise click.Abort()

    try:
        ctx.invoke(stack_update)
    except Exception:
        config.delete()
        click.secho(f"Error creating stack", fg="red")
        raise click.Abort()


@cli.command()
def stack_update():
    """
    Update the existing CloudFormation stack
    """
    cdk_cmd("deploy")


@cli.command()
def stack_diff():
    """
    Compares the specified stack with the deployed stack.
    """
    cdk_cmd("diff")


@cli.command()
def stack_delete():
    """
    Delete the CloudFormation stack
    """

    ecr_repository_name = (
        f"cdk-{names.PROJECT_NAME}-container-assets-"
        f"{aws.AWS_ACCOUNT_ID}-{aws.AWS_REGION}"
    )

    click.secho(
        "This will also delete the bootstrap resources including the S3 bucket"
        f" '{names.CDK_BOOTSTRAP_BUCKET}' and the ECR repository "
        f"'{ecr_repository_name}'",
        fg="yellow",
    )
    if not click.confirm(
        f"Are you sure you want to delete the {names.PROJECT_NAME} stack "
        "and all related resources?"
    ):
        return

    # Delete application stack
    cdk_cmd("destroy")

    # Empty boostrap S3 bucket
    cmd = (
        f"aws {profile_arg()} s3 rm --recursive "
        f"s3://{names.CDK_BOOTSTRAP_BUCKET}"
    )
    subprocess.call(cmd.split(), shell=False)

    # Find all bootstrapped ECR repository images
    cmd = (
        f"aws ecr list-images --repository-name {ecr_repository_name} "
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
            f" {ecr_repository_name} --image-ids {image_tags}"
        )
        click.echo(cmd)
        subprocess.call(cmd.split(), shell=False)

    # Delete bootstrap stack
    cmd = (
        "aws cloudformation delete-stack "
        f"--stack-name CDKToolkit {profile_arg()}"
    )
    click.echo(cmd)
    subprocess.call(cmd.split(), shell=False)

    # Delete bootstrap S3 bucket
    cmd = (
        f"aws s3api delete-bucket --bucket {names.CDK_BOOTSTRAP_BUCKET} "
        f"{profile_arg()}"
    )
    click.echo(cmd)
    subprocess.call(cmd.split(), shell=False)


@cli.command()
def stack_synth():
    """
    Synthesize and print CloudFormation template
    """
    cdk_cmd("synth")


@cli.command()
def stack_list():
    """
    Lists the stacks in the app
    """
    cdk_cmd("list")


@cli.command()
def config_show():
    """
    Show the current config
    """
    config.show()


@cli.command()
def config_edit():
    """
    Edit the current config
    """
    config.edit()


if __name__ == "__main__":
    cli()
