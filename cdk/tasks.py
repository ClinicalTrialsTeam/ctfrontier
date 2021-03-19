from invoke import task
from config import Config


@task(help={"config_filename": "an initial config filename"})
def create(ctx, config_filename=None):
    """
    Create initial stack. Must supply config.
    """

    if not config_filename or not config_filename.endswith(".json"):
        print("Config file must be a .json file")

    Config(config_filename)
