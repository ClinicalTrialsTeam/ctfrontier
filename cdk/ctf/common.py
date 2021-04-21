import site
from os.path import dirname, join

site.addsitedir(join(dirname(dirname(__file__)), "lib"))

from lib import aws
import click
import subprocess
import base64
import json


def profile_arg():
    if aws.AWS_PROFILE is not None:
        return f"--profile {aws.AWS_PROFILE}"
    return ""


def run_cdk_command(cmd):
    full_cmd = f"cdk {cmd} -c CTF_CLI=true {profile_arg()}"
    return run_command(full_cmd)


def run_command(cmd, capture_output=False, text=False):
    click.echo(cmd)
    r = subprocess.run(
        cmd, shell=True, capture_output=capture_output, text=text
    )
    if r.returncode != 0:
        raise click.Abort()
    return r


def base64_encode_dict(d):
    return base64.b64encode(json.dumps(d).encode()).decode()
