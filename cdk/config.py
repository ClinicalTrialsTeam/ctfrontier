from cdk import names
import boto3

SSM_BASE_PATH = f"/{names.PROJECT_NAME}/"

ssm = boto3.client("ssm")


class Config:
    def __init__(self):
        pass

    def new(self, initial_config_file):
        """
        Create a new configuration.
        """
        f = open(initial_config_file, "r")
        print(f.read())

        # Read json key, values
        # Create parameters for each

    def save(self):
        pass

    def delete(self):
        pass


class Param:
    def __init__(self, param_name, param_type="SecureString"):
        self.name = param_name
        self.type = param_type

    def create(self):
        ssm.put_parameter()

    def exists(self):
        pass

    def update(self, ssm_name):
        pass
