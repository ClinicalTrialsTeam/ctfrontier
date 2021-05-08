import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

import click
from .stack_commands import stack
from .config_commands import config
from .docker_commands import docker
from .container_commands import container
from .function_commands import function


@click.group()
def cli():
    pass


cli.add_command(stack)
cli.add_command(config)
cli.add_command(docker)
cli.add_command(container)
cli.add_command(function)
