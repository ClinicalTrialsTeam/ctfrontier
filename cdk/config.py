from cdk import names
import boto3
from botocore.exceptions import ParamValidationError, ClientError
import json
import tempfile
from subprocess import call
from enum import Enum
import os
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint


# load dotenv
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

SSM_BASE_PATH = f"/{names.PROJECT_NAME}"
AWS_PROFILE = os.getenv("AWS_PROFILE")

if AWS_PROFILE:
    boto3.Session(profile_name=AWS_PROFILE)

ssm = boto3.client("ssm")


class ParamValidationError(Exception):
    def __init__(self, message=None, errors=[]):
        super(ParamValidationError, self).__init__(message)
        self.errors = errors


class ParamTypes(Enum):
    STRING = "String"
    STRING_LIST = "StringList"
    SECURE_STRING = "SecureString"


class Config:
    def __init__(self):
        pass

    def new(self, initial_config_file):
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
            raise Exception(f"Error storing ssm parameters: {e}")
        except ParamValidationError as e:
            raise Exception(f"The parameters you provided are incorrect: {e}")

    def edit(self):
        tf = TemporaryFile()

        # while True:
        #     try:
        #         tf.open_editor()
        #         changes = tf.diff()
        #         if changes:
        #             click.echo("\n".join(tf.diff()) + "\n")
        #             if click.confirm("Accept changes?"):
        #                 break
        #             if click.confirm("Continue editing?", abort=True):
        #                 continue
        #         if not changes:
        #             click.echo("No changes made")
        #             return
        #     except ParamSchemaValidationError as e:
        #         click.echo("\nSchema validation failed:")
        #         for error in e.errors:
        #             click.echo(error, err=True)
        #         click.confirm("Continue editing?", abort=True)

        # tf.push_updates()
        # tf.delete()

    def save(self):
        pass

    def delete(self):
        pass


class Param:
    """
    Class to create, update, delete an individual SSM parameter.
    """

    def __init__(self, param_name):
        self.name = param_name
        self.path_name = f"{SSM_BASE_PATH}/{param_name}"

    def create(self, value, param_type=ParamTypes.SECURE_STRING):
        if param_type not in ParamTypes:
            raise Exception(f"{param_type} is an invalid ssm parameter type")
        self.type = param_type.value

        resp = ssm.put_parameter(
            Name=self.path_name,
            Description=f"{names.PROJECT_NAME} environment variable {self.name}",
            Value=value,
            Type=self.type,
            Tags=[
                {
                    "Key": "project",
                    "Value": "CTF",
                }
            ],
            Tier="Standard",
        )
        print(f"Created ssm param {self.name},{value}: {resp}")

    def exists(self):
        try:
            ssm.get_parameter(Name=self.path_name, WithDecryption=False)
            return True
        except ssm.exceptions.ParameterNotFound:
            return False

    def update(self, value):
        resp = ssm.put_parameter(
            Name=self.path_name, Value=value, Overwrite=True
        )
        print(f"Updated ssm param {self.name} value to {value}: {resp}")

    def delete(self):
        resp = ssm.delete_parameter(Name=self.path_name)
        print(f"Delted ssm param {self.name}: {resp}")


class TemporaryFile:
    def __init__(self, base_path=SSM_BASE_PATH):

        # Load current parameters
        resp = ssm.get_parameters_by_path(Path=base_path, WithDecryption=True)
        pprint(resp["Parameters"])

        self.current_params = {
            r["Name"].split("/")[-1]: r["Value"] for r in resp["Parameters"]
        }

        # write a temporary file with the current parameters
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            json.dump(self.current_params, f)

        self.name = f.name
        self.new_params = {}

    def open_editor(self):
        editor = os.environ.get("EDITOR")
        if not editor:
            editor = "vim"

        call([editor, self.name])

        self.validate()

        self.envs = {}
        with open(self.name, "r") as tf:
            lines = tf.readlines()
            for line in lines:
                env_name, env_value = line.strip().split("=")
                self.envs[env_name] = env_value

    def validate(self):
        with open("example-config.json", "r") as f:
            data = json.load(f)

        required_params = set(data.keys())
        existing_params = set(self.current_params.keys())

        errors = []
        for missing in existing_params.difference(required_params):
            errors.append(f"{missing} exists in SSM but is not required")
        for missing in required_params.difference(existing_params):
            errors.append(f"{missing} required but missing from SSM")
        if errors:
            raise ParamValidationError(errors=errors)

    # def diff(self):
    #     config = get_config(self.config_file)
    #     schema = config["schema"]
    #     existing_params = {p.name: p for p in self.stage.get_params()}

    #     changes = []
    #     for param in self.envs:
    #         if param not in existing_params:
    #             if self.envs[param]:
    #                 # in schema but not yet in parameter store
    #                 param_type = schema[param][0]
    #                 changes.append(
    #                     "Adding param of type {} {}={}."
    #                     .format(param_type, param, self.envs[param])
    #                 )
    #             else:
    #                 # not in schema
    #                 changes.append(
    #                     "Warning: param {} not defined in schema."
    #                     " Add to schema before accepting changes.".format(param)
    #                 )
    #         else:
    #             if existing_params[param].value != self.envs[param]:
    #                 changes.append("Updating param {} from {} to {}"
    #                                .format(param, existing_params[param].value,
    #                                        self.envs[param]))
    #             current_param_type = existing_params[param].type
    #             schema_param_type = schema[param][0]
    #             if current_param_type != schema_param_type:
    #                 changes.append("Changing param {} from type {} to type {}."
    #                                .format(
    #                                     param,
    #                                     current_param_type,
    #                                     schema_param_type))

    #     for param in self.deleted_params():
    #         changes.append("Deleting param {}".format(param))

    #     return changes

    # def deleted_params(self):
    #     deleted_params = {}
    #     existing_params = {p.name: p.value for p in self.stage.get_params()}

    #     for param in existing_params:
    #         if param not in self.envs:
    #             deleted_params[param] = existing_params[param]

    #     return deleted_params

    # def push_updates(self):
    #     config = get_config(self.config_file)
    #     schema = config["schema"]
    #     tags = config.get("tags", {})

    #     for param in self.envs:
    #         if param not in schema:
    #             click.echo(
    #                 "Param {}(value={}) not in schema, skipping update"
    #                 .format(param, self.envs[param])
    #             )
    #             continue
    #         param_type = schema[param][0]
    #         param_desc = None
    #         if len(schema[param]) > 1:
    #             param_desc = schema[param][1]
    #         args = [param, self.envs[param], param_type, param_desc]

    #         Param.create(
    #             self.stage.project,
    #             self.stage.name,
    #             *args,
    #             overwrite=True,
    #             tags=tags
    #         )

    #     for param in self.deleted_params():
    #         self.stage.delete(param)

    def delete(self):
        os.unlink(self.name)


tf = TemporaryFile()
