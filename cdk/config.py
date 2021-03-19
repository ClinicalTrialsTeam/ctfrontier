from cdk import names
import boto3
import json
from enum import Enum

SSM_BASE_PATH = f"/{names.PROJECT_NAME}"

ssm = boto3.client("ssm")


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

        for key, val in data.items():
            Param(key).create(val)

    def save(self):
        pass

    def delete(self):
        pass


class Param:
    def __init__(self, param_name, param_type=ParamTypes.SECURE_STRING):
        self.name = param_name
        self.path_name = f"{SSM_BASE_PATH}/{param_name}"
        if param_type not in ParamTypes:
            raise Exception(f"{param_type} is an invalid ssm parameter type")
        self.type = param_type

    def create(self, value):
        resp = ssm.put_parameter(
            Name=self.path_name,
            Description=f"{names.PROJECT_NAME} environment variable {self.name}",
            Value=value,
            Type=self.type,
            Overwrite=True,
            Tags=[{"Key": "project", "Value": "CTF"}],
            Tier="Standard",
        )
        print(f"Created ssm param {self.name},{value}: {resp}")

    def exists(self):
        resp = ssm.get_parameter(Name=self.path_name, WithDecryption=False)
        print(f"Checked existence: {resp}")

    def update(self, value):
        resp = ssm.put_parameter(
            Name=self.path_name,
            Value=value,
        )
        print(f"Updated ssm param {self.name} value to {value}: {resp}")

    def delete(self):
        resp = ssm.delete_parameter(Name=self.path_name)
        print(f"Delted ssm param {self.name}: {resp}")
