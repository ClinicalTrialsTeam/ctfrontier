import boto3
from botocore.exceptions import ClientError
from enum import Enum
from . import names, aws


SSM_BASE_PATH = f"/{names.PROJECT_NAME}"

if aws.AWS_PROFILE:
    boto3.Session(profile_name=aws.AWS_PROFILE)

ssm = boto3.client("ssm")


class ParamTypes(Enum):
    STRING = "String"
    STRING_LIST = "StringList"
    SECURE_STRING = "SecureString"


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

        try:
            ssm.put_parameter(
                Name=self.path_name,
                Description=(
                    f"{names.PROJECT_NAME} environment variable {self.name}"
                ),
                Value=value,
                Type=self.type,
                Tags=aws.STACK_TAGS,
                Tier="Standard",
            )
        except ClientError as e:
            raise Exception(f"Error storing ssm parameters: {e}")

    def exists(self):
        try:
            ssm.get_parameter(Name=self.path_name, WithDecryption=False)
            return True
        except ssm.exceptions.ParameterNotFound:
            return False

    def get_value(self, decrypt=False, required=True):
        try:
            r = ssm.get_parameter(Name=self.path_name, WithDecryption=decrypt)
            return r["Parameter"]["Value"]
        except ssm.exceptions.ParameterNotFound:
            if required:
                raise Exception(f"Missing required config param {self.name}")
            return None

    def update(self, value):
        ssm.put_parameter(Name=self.path_name, Value=value, Overwrite=True)

    def delete(self):
        ssm.delete_parameter(Name=self.path_name)
