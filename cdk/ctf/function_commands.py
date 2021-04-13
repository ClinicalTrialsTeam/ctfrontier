import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import names
import json
import click
import requests
from .common import (
    run_command,
    base64_encode_dict,
    profile_arg,
    get_image_uri,
    build_docker_image,
    deploy_docker_image,
)


@click.group()
def function():
    pass


@function.command("invoke")
def function_invoke():
    """
    Invoke the lambda function
    """
    payload = {"test": "foo"}

    function_name = f"{names.PROJECT_NAME}-{names.RAW_DATA_DOWNLOAD_FUNCTION}"
    cmd = (
        f"aws lambda invoke --function-name {function_name} "
        f"--payload '{base64_encode_dict(payload)}' "
        f"--qualifier {names.LAMBDA_RELEASE_ALIAS} "
        f"{profile_arg()} outfile.txt"
    )
    run_command(cmd)


@function.command("deploy")
def function_deploy():
    """
    Deploy the lambda function
    """
    deploy_docker_image()
    __update_function_code()


@function.command("local_run")
def function_local_run():
    """
    Build and run the lambda locally
    """
    image_uri = get_image_uri()
    build_docker_image(image_uri)

    cmd = f"docker run -p 9000:8080 {image_uri}"
    run_command(cmd)


@function.command("local_test")
def function_local_test():
    """
    Send a test payload to the locally running lambda
    """
    url = "http://localhost:9000/2015-03-31/functions/function/invocations"
    payload = {"payload": "hello_world"}

    r = requests.post(url, data=json.dumps(payload))

    r.raise_for_status
    click.echo(r.status_code)
    click.echo(json.dumps(json.loads(r.content.decode()), indent=4))


@function.command("local_stop")
def function_local_stop():
    """
    Stop the locally running lambda
    """
    cmd = f"docker stop {get_image_uri()}"
    run_command(cmd)


def __update_function_code():
    # Update code
    cmd = (
        f"aws {profile_arg()} lambda update-function-code "
        f"--function-name {names.PROJECT_NAME}-{names.RAW_DATA_DOWNLOAD_FUNCTION} "
        f"--image-uri {get_image_uri()} --publish"
    )
    r = run_command(cmd, capture_output=True, text=True)
    version = json.loads(r.stdout)["Version"]

    # Update release alias
    cmd = (
        f"aws {profile_arg()} lambda update-alias --function-name "
        f"{names.PROJECT_NAME}-{names.RAW_DATA_DOWNLOAD_FUNCTION} "
        f"--name {names.LAMBDA_RELEASE_ALIAS} --function-version {version} "
    )
    run_command(cmd)
