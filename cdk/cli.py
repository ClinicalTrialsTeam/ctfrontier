import click
from lib.config import Config, Param


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option(
    "--config",
    prompt="Initial config filename",
    help="Provide and initial config file",
)
def create_stack(config):
    """
    Create a new stage.
    """

    # Create initial parameters
    Config().new(config)

    # Some error message if missing required parameters


if __name__ == "__main__":
    cli()
