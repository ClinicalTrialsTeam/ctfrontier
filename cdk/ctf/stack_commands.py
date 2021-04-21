import site
from os.path import join, dirname

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import names, aws
import click
import json
import boto3
from botocore.exceptions import ClientError
import subprocess
from .common import run_cdk_command, run_command, profile_arg
from .function_commands import build_lambda_package, function_deploy
from .container_commands import (
    build_frontend,
    build_backend,
    push_docker_image,
)


@click.group()
def stack():
    pass


@stack.command("bootstrap")
def boostrap_create():
    __bootstrap_cdk()
    __bootstrap_custom()


@stack.command("bootstrap.destroy")
def bootstrap_delete():
    __delete_bootstrap_custom()
    __delete_bootstrap_cdk()


@stack.command("create")
@click.pass_context
def stack_create(ctx):
    """
    Create a new CloudFormation stack
    """
    # Create key pair for EC2 instance
    cmd = (
        f"aws ec2 create-key-pair --key-name {names.BACKEND_KEY_PAIR} "
        f"--query 'KeyMaterial' --output text > {names.BACKEND_KEY_PAIR}.pem "
        f"{profile_arg()}"
    )
    run_command(cmd)
    run_command(f"chmod 400 {names.BACKEND_KEY_PAIR}.pem")

    build_frontend()
    push_docker_image(names.FRONTEND_REPOSITORY)
    build_backend()
    push_docker_image(names.BACKEND_REPOSITORY)

    try:
        # Must put lambas in S3 before deploying
        build_lambda_package(ctx, func=names.ETL_DOWNLOAD_FUNCTION)
        ctx.invoke(stack_update)
    except Exception as e:
        click.secho(f"Error creating stack: {e}", fg="red")
        raise click.Abort()


@stack.command("update")
@click.pass_context
def stack_update(ctx, update_functions=False):
    """
    Update the existing CloudFormation stack
    """
    run_cdk_command("deploy")

    if update_functions:
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

    # Clean up the key pair
    run_command(
        f"aws ec2 delete-key-pair --key-name {names.BACKEND_KEY_PAIR} "
        f"{profile_arg()}"
    )


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


def __bootstrap_custom():

    # Create S3 bucket to store lambda code
    cmd = (
        f"aws {profile_arg()} s3api create-bucket "
        f"--bucket {names.LAMBDA_CODE_BUCKET}"
    )
    run_command(cmd)

    # Create ECR repositories
    tags = ""
    for tag in aws.STACK_TAGS:
        tags += f"Key={tag['Key']},Value={tag['Value']} "

    policy_path = join(dirname(dirname(__file__)), "lib/ecr-policy.json")
    with open(policy_path, "r") as f:
        lifecycle_policy = json.loads(f.read())

    ecr = boto3.client("ecr")
    for repo in names.REPOSITORIES:
        try:
            ecr.create_repository(
                repositoryName=repo,
                tags=aws.STACK_TAGS,
                imageScanningConfiguration={"scanOnPush": True},
            )

        except ClientError as e:
            error = e.response["Error"]
            if error["Code"] == "RepositoryAlreadyExistsException":
                click.echo(
                    f"ECR repository {repo} already exists. Skipping create."
                )

        ecr.put_lifecycle_policy(
            repositoryName=repo,
            lifecyclePolicyText=json.dumps(lifecycle_policy),
        )
        click.echo(f"Updated ECR lifecycle policy for {repo}.")


def __delete_bootstrap_custom():
    # Clear lambda code S3 bucket and delete the bucket
    __empty_s3_bucket(names.LAMBDA_CODE_BUCKET)
    cmd = (
        f"aws {profile_arg()} s3api delete-bucket "
        f"--bucket {names.LAMBDA_CODE_BUCKET}"
    )
    run_command(cmd)

    for repo in names.REPOSITORIES:
        # Find and all ECR repository images
        cmd = (
            f"aws {profile_arg()} ecr list-images --repository-name " f"{repo}"
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
                f" {repo} --image-ids {image_digests} "
                f"{profile_arg()}"
            )
            run_command(cmd)

        # Delete ECR repository
        cmd = (
            f"aws ecr delete-repository "
            f"--repository-name {repo} {profile_arg()}"
        )
        run_command(cmd)


def __bootstrap_cdk():
    tags_args = ""
    for tag in aws.STACK_TAGS:
        tags_args += f"--tags {tag['Key']}={tag['Value']} "
    r = run_cdk_command(
        f"bootstrap --bootstrap-bucket-name {names.CDK_BOOTSTRAP_BUCKET} "
        f"--qualifier {names.PROJECT_NAME} {tags_args}"
    )
    if r.returncode != 0:
        click.secho(
            f"Error boostrapping environment. Returned {r.returncode}",
            fg="red",
        )
        raise click.Abort()


def __delete_bootstrap_cdk():
    bootstrap_repository_name = (
        f"cdk-{names.PROJECT_NAME}-container-assets-"
        f"{aws.AWS_ACCOUNT_ID}-{aws.AWS_REGION}"
    )

    __empty_s3_bucket(names.CDK_BOOTSTRAP_BUCKET)

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


def __empty_s3_bucket(bucket_name):
    cmd = f"aws {profile_arg()} s3 rm --recursive " f"s3://{bucket_name}"
    run_command(cmd)
