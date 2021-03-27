import click
import boto3
from botocore.exceptions import ParamValidationError, ClientError
import json
import tempfile
from subprocess import call
from enum import Enum
from os import getenv, environ, unlink
from os.path import join, dirname
from dotenv import load_dotenv
from . import names


# load dotenv
dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

SSM_BASE_PATH = f"/{names.PROJECT_NAME}"
AWS_PROFILE = getenv("AWS_PROFILE")
EXAMPLE_CONFIG = "template-config.json"
STACK_TAGS = {
    "Key": "project",
    "Value": "CTF",
}


if AWS_PROFILE:
    boto3.Session(profile_name=AWS_PROFILE)

ssm = boto3.client("ssm")


class ConfigValidationError(Exception):
    def __init__(self, message=None, errors=[]):
        super(ConfigValidationError, self).__init__(message)
        self.errors = errors


class ParamTypes(Enum):
    STRING = "String"
    STRING_LIST = "StringList"
    SECURE_STRING = "SecureString"


def new(initial_config_file):
    """
    Create a new configuration.
    """

    # Read json key, values and create parameters for each
    with open(initial_config_file, "r") as f:
        data = json.load(f)

    try:
        for key, val in data.items():
            Param(key).create(val)
    except ClientError as e:
        click.secho(f"Error storing ssm parameters: {e}", fg="red")
        raise
    except ParamValidationError as e:
        click.secho(
            f"The parameters you provided are incorrect: {e}", fg="red"
        )
        raise


def edit():
    tf = TemporaryFile()

    while True:
        try:
            tf.open_editor()
            diff = tf.diff()
            if diff:
                if click.confirm("Accept changes?"):
                    break
                if click.confirm("Continue editing?", abort=True):
                    continue
            else:
                click.echo("No changes made")
                return
        except ConfigValidationError as e:
            click.echo("\nMissing required config variables:")
            for error in e.errors:
                click.echo(error, err=True)
            click.confirm("Continue editing?", abort=True)

    tf.push_updates()
    tf.delete()


def show():
    current_config = Param.current_parameters()
    if not current_config:
        click.echo("No existing config")
    else:
        for key, val in current_config.items():
            click.echo(f"{key}={val}")


def delete():
    for key in Param.current_parameters().keys():
        Param(key).delete()


class Param:
    """
    Class to create, update, delete an individual SSM parameter.
    """

    def __init__(self, param_name):
        self.name = param_name
        self.path_name = f"{SSM_BASE_PATH}/{param_name}"

    @classmethod
    def current_parameters(cls):
        # Load current parameters
        resp = ssm.get_parameters_by_path(
            Path=SSM_BASE_PATH, WithDecryption=True
        )

        return {
            r["Name"].split("/")[-1]: r["Value"] for r in resp["Parameters"]
        }

    def create(self, value, param_type=ParamTypes.SECURE_STRING):
        if param_type not in ParamTypes:
            raise Exception(f"{param_type} is an invalid ssm parameter type")
        self.type = param_type.value

        ssm.put_parameter(
            Name=self.path_name,
            Description=f"{names.PROJECT_NAME} environment variable {self.name}",
            Value=value,
            Type=self.type,
            Tags=[STACK_TAGS],
            Tier="Standard",
        )
        print(f"Created ssm param {self.name}={value}")

    def exists(self):
        try:
            ssm.get_parameter(Name=self.path_name, WithDecryption=False)
            return True
        except ssm.exceptions.ParameterNotFound:
            return False

    def getvalue(self, decrypt=False, required=False):
        try:
            r = ssm.get_parameter(Name=self.path_name, WithDecryption=decrypt)
            return r["Parameter"]["Value"]
        except ssm.exceptions.ParameterNotFound:
            if required:
                raise Exception(f"Missing required config param {self.name}")
            return None

    def update(self, value):
        ssm.put_parameter(Name=self.path_name, Value=value, Overwrite=True)
        print(f"Updated ssm param {self.name} to {value}")

    def delete(self):
        ssm.delete_parameter(Name=self.path_name)
        print(f"Deleted ssm param {self.name}")


class TemporaryFile:
    def __init__(self, base_path=SSM_BASE_PATH):
        self.current_params = Param.current_parameters()

        # write a temporary file with the current parameters
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            json.dump(self.current_params, f, indent=4)

        self.name = f.name
        self.new_params = {}

    def open_editor(self):
        """
        Open in editor and track changes made
        """
        editor = environ.get("EDITOR")
        if not editor:
            editor = "vim"

        call([editor, self.name])

        with open(self.name, "r") as tf:
            self.new_params = json.load(tf)

        self.validate()

        self._create = {}
        self._update = {}
        self._delete = []

        for key, val in self.new_params.items():
            if key in self.current_params.keys():
                if val != self.current_params[key]:
                    self._update[key] = val
            else:
                self._create[key] = val

        for key in self.current_params.keys():
            if key not in self.new_params.keys():
                self._delete.append(key)

    def validate(self):
        """
        Make sure required config variables are set
        """
        with open(EXAMPLE_CONFIG, "r") as f:
            data = json.load(f)

        required_params = set(data.keys())
        new_params = set(self.new_params.keys())

        errors = []
        for missing in required_params.difference(new_params):
            errors.append(f"{missing} required but missing from SSM")
        if errors:
            raise ConfigValidationError(errors=errors)

    def diff(self):
        """
        Display changes made
        """
        for key, val in self._create.items():
            click.echo(f"Create {key}={val}")

        for key, val in self._update.items():
            click.echo(f"Update {key} to {val}")

        for key in self._delete:
            click.echo(f"Delete {key}")

        return self._create or self._update or self._delete

    def push_updates(self):
        """
        Push updates to SSM
        """
        for key, val in self._create.items():
            Param(key).create(val)

        for key, val in self._update.items():
            Param(key).update(val)

        for key in self._delete:
            Param(key).delete()

    def delete(self):
        """
        Delete the temporary file
        """
        unlink(self.name)
