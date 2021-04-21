import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import environment
import click
import json


CONFIG_SCHEMA_FILE = "config-schema.json"


class ConfigValidationError(Exception):
    def __init__(self, message=None, errors=[]):
        super(ConfigValidationError, self).__init__(message)
        self.errors = errors


@click.group()
def config():
    pass


@config.command("create")
@click.option(
    "--config-file",
    prompt=(
        "Initial config filename "
        "(Note: editing config can only be done with 'ctf config-edit')"
    ),
    help="Provide and initial config file",
)
def config_create(config_file):
    """
    Create a new config.
    """
    if not config_file.strip():
        click.echo("Missing config file!")
        raise click.Abort()

    if not click.confirm(
        "Creating a new config will overwrite the old config"
        " if any exists. Create a new config?"
    ):
        return

    Config.delete()
    Config.new(config_file)


@config.command("delete")
def config_delete():
    Config.delete()


@config.command("show")
def config_show():
    """
    Show the current config
    """
    Config().show()


@config.command("edit")
def config_edit():
    """
    Edit the current config
    """
    Config().edit()


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

        with open(CONFIG_SCHEMA_FILE, "r") as f:
            config_schema = json.load(f)

        # Read json key, values and create parameters for each
        try:
            for key, val in current_config.items():
                if key in config_schema:
                    if (
                        config_schema[key]["type"]
                        == environment.ParamTypes.STRING.value
                    ):
                        param_type = environment.ParamTypes.STRING
                    elif (
                        config_schema[key]["type"]
                        == environment.ParamTypes.STRING_LIST.value
                    ):
                        param_type = environment.ParamTypes.STRING_LIST
                    else:
                        param_type = environment.ParamTypes.SECURE_STRING
                environment.Param(key).create(val, param_type=param_type)
                click.echo(
                    f"Created ssm param {key}={val}, type: {param_type.value}"
                )
        except Exception as e:
            click.secho(f"Error creating ssm parameters: {e}", fg="red")
            raise click.Abort()

    @classmethod
    def delete(cls):
        for key in environment.Param.current_parameters().keys():
            environment.Param(key).delete()

    def show(self):
        if not self.current_config:
            click.echo("No existing config")
        else:
            click.echo(json.dumps(self.current_config, indent=4))

    def edit(self):

        while True:
            try:
                edited = click.edit(json.dumps(self.current_config, indent=4))
                if edited:
                    try:
                        new_config = json.loads(edited)
                    except json.JSONDecodeError as e:
                        click.secho(f"Invalid JSON. {e}", fg="red")
                        if click.confirm("Continue editing?", abort=True):
                            continue
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

        schema = self._schema()

        required_params = set(schema.keys())
        current_params = set(config.keys())

        errors = []
        for missing in required_params.difference(current_params):
            errors.append(f"{missing} required but missing from SSM")
        if errors:
            raise ConfigValidationError(errors=errors)

    def _schema(self):
        with open(CONFIG_SCHEMA_FILE, "r") as f:
            return json.load(f)

    def _print_diff(self):
        schema = self._schema()

        for key, val in self._create.items():
            click.echo(f"Create {key}={val}, type={schema[key]['type']}")

        for key, val in self._update.items():
            click.echo(f"Update {key} to {val}")

        for key in self._delete:
            click.echo(f"Delete {key}")

        return self._create or self._update or self._delete

    def _push_updates(self):
        """
        Push updates to SSM
        """
        schema = self._schema()

        for key, val in self._create.items():
            param_type_str = schema[key]["type"]
            if param_type_str == environment.ParamTypes.STRING.value:
                param_type = environment.ParamTypes.STRING
            elif param_type_str == environment.ParamTypes.STRING_LIST.value:
                param_type = environment.ParamTypes.STRING_LIST
            else:
                param_type = environment.ParamTypes.SECURE_STRING
            environment.Param(key).create(val, param_type=param_type)
            click.echo(f"Added {key}={val}")

        for key, val in self._update.items():
            environment.Param(key).update(val)
            click.echo(f"Updated {key} to {val}")

        for key in self._delete:
            environment.Param(key).delete()
            click.echo(f"Deleted {key}")
