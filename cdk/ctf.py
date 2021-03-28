import click
import json
from lib import names, aws, environment
import subprocess
import base64


EXAMPLE_CONFIG = "template-config.json"


class ConfigValidationError(Exception):
    def __init__(self, message=None, errors=[]):
        super(ConfigValidationError, self).__init__(message)
        self.errors = errors


def profile_arg():
    if aws.AWS_PROFILE is not None:
        return f"--profile {aws.AWS_PROFILE}"
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

    tags_args = ""
    for key, val in aws.STACK_TAGS.items():
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
        Config.delete()
        click.secho("Error creating stack", fg="red")
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
    Compares the specified stack with the deployed stack
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
    Config().show()


@cli.command()
def config_edit():
    """
    Edit the current config
    """
    Config().edit()


@cli.command()
def invoke_function():
    """
    Invoke lambda function
    """
    payload = {"test": "foo"}

    function_name = f"{names.PROJECT_NAME}-{names.RAW_DATA_DOWNLOAD_FUNCTION}"
    cmd = (
        f"aws lambda invoke --function-name {function_name} "
        f"--payload '{base64_encode_dict(payload)}' "
        f"--qualifier {names.LAMBDA_RELEASE_ALIAS} "
        f"{profile_arg()} outfile.txt"
    )
    click.echo(cmd)
    r = subprocess.call(cmd.split())

    return r


"""
HELPERS
"""


def base64_encode_dict(d):
    return base64.b64encode(json.dumps(d).encode()).decode()


class Config:
    def __init__(self):
        self.current_config = environment.Param.current_parameters()

        # Keep track of the differences between current and new config
        self._create = {}
        self._update = {}
        self._delete = []

    @classmethod
    def new(cls, config_file):
        with open(config_file, "r") as f:
            current_config = json.load(f)

        # Read json key, values and create parameters for each
        try:
            for key, val in current_config.items():
                environment.Param(key).create(val)
                click.echo(f"Created ssm param {key}={val}")
        except Exception as e:
            click.secho(f"Error creating ssm parameters: {e}", fg="red")

    @classmethod
    def delete(cls):
        for key in environment.Param.current_parameters().keys():
            environment.Param(key).delete()

    def show(self):
        if not self.current_config:
            click.echo("No existing config")
        else:
            for key, val in self.current_config.items():
                click.echo(f"{key}={val}")

    def edit(self):

        while True:
            try:
                edited = click.edit(json.dumps(self.current_config, indent=4))
                if edited:
                    new_config = json.loads(edited)
                    self._validate(new_config)

                    self._create = {}
                    self._update = {}
                    self._delete = []

                    for key, val in new_config.items():
                        if key in self.current_config.keys():
                            if val != self.current_config[key]:
                                self._update[key] = val
                        else:
                            self._create[key] = val

                    for key in self.current_config.keys():
                        if key not in new_config.keys():
                            self._delete.append(key)

                    self._print_diff()
                    if click.confirm("Accept changes?"):
                        break
                    if click.confirm("Continue editing?", abort=True):
                        continue
                else:
                    click.echo("No config changes made")
                    return
            except ConfigValidationError as e:
                click.echo("\nMissing required config variables:")
                for error in e.errors:
                    click.echo(error, err=True)
                click.confirm("Continue editing?", abort=True)

        self._push_updates()

    def _validate(self, config=None):
        if not config:
            config = self.current_config

        with open(EXAMPLE_CONFIG, "r") as f:
            data = json.load(f)

        required_params = set(data.keys())
        current_params = set(config.keys())

        errors = []
        for missing in required_params.difference(current_params):
            errors.append(f"{missing} required but missing from SSM")
        if errors:
            raise ConfigValidationError(errors=errors)

    def _print_diff(self):
        for key, val in self._create.items():
            click.echo(f"Create {key}={val}")

        for key, val in self._update.items():
            click.echo(f"Update {key} to {val}")

        for key in self._delete:
            click.echo(f"Delete {key}")

        return self._create or self._update or self._delete

    def _push_updates(self):
        """
        Push updates to SSM
        """
        for key, val in self._create.items():
            environment.Param(key).create(val)
            click.echo(f"Added {key}={val}")

        for key, val in self._update.items():
            environment.Param(key).update(val)
            click.echo(f"Updated {key} to {val}")

        for key in self._delete:
            environment.Param(key).delete()
            click.echo(f"Deleted {key}")


if __name__ == "__main__":
    cli()
