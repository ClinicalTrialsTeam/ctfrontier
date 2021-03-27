import click
import lib.config as config


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
def stack_create(config_file):
    """
    Create a new stack.
    """

    # Create initial parameters
    config.new(config_file)

    # Some error message if missing required parameters


@cli.command()
def stack_delete():
    """
    Delete the stack.
    """
    config.delete()


@cli.command()
def config_show():
    """
    Show the current config.
    """
    config.show()


@cli.command()
def config_edit():
    """
    Edit the current config.
    """
    config.edit()


if __name__ == "__main__":
    cli()
