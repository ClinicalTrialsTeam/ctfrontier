import site
from os.path import dirname, join, exists

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

import json
import click
import requests
import shutil
from os import chdir, getcwd
from lib import names
from .common import (
    run_command,
    base64_encode_dict,
    profile_arg,
    get_image_uri,
    build_docker_image,
    get_image_id,
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

    func = names.ETL_DOWNLOAD_FUNCTION

    function_name = f"{names.PROJECT_NAME}-{func}"
    cmd = (
        f"aws lambda invoke --function-name {function_name} "
        f"--payload '{base64_encode_dict(payload)}' "
        f"--qualifier {names.LAMBDA_RELEASE_ALIAS} "
        f"{profile_arg()} outfile.txt"
    )
    run_command(cmd)


@function.command("deploy")
@click.pass_context
def function_deploy(ctx):
    """
    Deploy the lambda function
    """
    func = names.ETL_DOWNLOAD_FUNCTION

    __build_lambda_package(ctx, func)
    __update_function_code(func)


@function.command("local_run")
def function_local_run():
    """
    Build and run the lambda locally
    """
    image_uri = get_image_uri()
    build_docker_image(image_uri)

    cmd = f"docker run -d -p 9000:8080 {image_uri}"
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
    cmd = f"docker stop {get_image_id(running=True)}"
    run_command(cmd)


def __build_lambda_package(ctx, func):
    zip_path = join(dirname(dirname(__file__)), f"dist/{func}.zip")
    build_path = join(dirname(dirname(__file__)), f"dist/{func}")
    if exists(build_path):
        shutil.rmtree(build_path)

    # make sure dependencies are up to date
    func_path = join(dirname(dirname(__file__)), f"functions/{func}")
    run_command(f"pip-compile {func_path}/requirements.in")

    # create lambda deployment package
    run_command(
        f"pip install --target {build_path} -r {func_path}/requirements.txt"
    )

    run_command(f"cp {func_path}/app.py {build_path}")

    current_path = getcwd()
    chdir(build_path)
    # zip lambda deployment package
    run_command(f"zip -r ../{func}.zip .")
    chdir(current_path)

    # upload to S3
    s3_path = (
        f"s3://{names.LAMBDA_CODE_BUCKET}/{names.PROJECT_NAME}/{func}.zip"
    )
    run_command(f"aws {profile_arg()} s3 cp {zip_path} {s3_path}")


def __update_function_code(func):
    # Update code
    zip_path = join(dirname(dirname(__file__)), "dist", f"{func}.zip")
    cmd = (
        f"aws {profile_arg()} lambda update-function-code "
        f"--function-name {names.PROJECT_NAME}-{func} "
        f"--zip-file fileb://{zip_path} --publish"
    )
    r = run_command(cmd, capture_output=True, text=True)
    version = json.loads(r.stdout)["Version"]

    # Release updated code
    cmd = (
        f"aws {profile_arg()} lambda update-alias --function-name "
        f"{names.PROJECT_NAME}-{func} "
        f"--name {names.LAMBDA_RELEASE_ALIAS} --function-version {version} "
    )
    run_command(cmd)
