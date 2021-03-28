
# CTFrontier CDK documentation

## Requirements

#### Python

* Python 3.8
* A python virtual environment tool of your preference

#### CDK

* AWS CLI 2.1.0+ installed and configured  <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html>
* Node.js 15.4.0+
* The `aws-cdk` Node.js toolkit installed. `npm install -g aws-cdk@1.94.1`. (`npm list -g` to check the current versions of your globally installed node packages)
 

## Setup

#### Local environment setup

1. Make sure that you have set up your AWS credentials (set up using `aws configure`, check to see if they exist with `ls ~/.aws/`, you should see the files `config` and `credentials`
1. If you want to use a named profile. Create a file `cdk/.env` with the variable `AWS_PROFILE` defined.

Set up Python virtual environment. For example, if you were using virtualenv you might: 

1. Install virtualenv `pip install virtualenv`
1. Create your virtual environment with `virtualenv venv`
1. Start your virtual environment with `source venv/bin/activate`
(`deactivate` to turn it off)

Once you have your virtual environment set up and it is active:

1. Python dependencies are handled via `pip-tools`, so you need to install that first: `pip install pip-tools`
1. From the `ctfrontier/cdk` folder, install the dependencies by running `pip-sync requirements/dev.txt`


#### AWS Permissions

Your default AWS user (configured with `aws configure`) or your named aws profile (configured with `aws configure --profile <profile-name>` and specified in `cdk/.env` with `AWS_PROFILE=<profile-name>`) must have the following AWS managed policies or equivalent permissions attached:

* IAMFullAccess
* AmazonEC2ContainerRegistryFullAccess
* AmazonS3FullAccess
* CloudWatchFullAccess
* AmazonSSMFullAccess
* AmazonSSNFullAccess
* AWSCloudFormationFullAccess
* AWSLambda_FullAccess

## Running the project

Interact with the ctfrontier CDK project by using the `ctf` command line tool.

After following the above setup instructions, you should be able to run the command `ctf` and see a list of the available commands. For example:

	Usage: ctf [OPTIONS] COMMAND [ARGS]...
	
	Options:
	  --help  Show this message and exit.
	
	Commands:
	  config-edit   Edit the current config
	  config-show   Show the current config
	  stack-create  Create a new CloudFormation stack
	  stack-delete  Delete the CloudFormation stack
	  stack-diff    Compares the specified stack with the deployed stack
	  stack-list    Lists the stacks in the app
	  stack-synth   Synthesize and print CloudFormation template
	  stack-update  Update the existing CloudFormation stack
	  
	  
### Create a new Stack

To create a new stack, create a json file for your initial configuration
that contains entries for all the keys in `config-schema.json`. Types can
be ignored.

For example, if the `config-schema.json` is:

```
{
    "notification_email": {
        "type": "String"
    },
	"secret_password": {
		"type": "SecureString"
	}
}
```

Then create a file `myconfig.json`:

```
{
    "notification_email": "youremail@example.com",
	"secret_password": "super-secret-password"
}
```

Then run `ctf stack-create`. You will be prompted to enter your the filename of your initial config file.

*Note: The initial config file is just loads the initial config values, the actual config is stored in the cloud and must be managed with teh `ctf config-*` commands.*

If `ctf stack-create` fails, there is likely an error with your AWS configuration. 

If `ctf stack-create` completes, then you should should have a new CloudFormation stack in your AWS account with all the resources defined in `cdk/lib/stack.py`.


### Update the stack

Run `ctf stack-update` to push changes to an already created stack.


### Delete the stack

Run `ctf stack-delete` to delete the stack. This will delete all associated resources including the ones that AWS creates for bootstrapping.


### Edit the config

Edit the config in the cloud with `ctf config-edit`. This will allow you to edit the config using your default command line text editor defined by the `EDITOR` environment variable. Or, if none is specified, vim.

### Show the current config

Run `ctf config-show` to show the current config. You can also log into AWS and look at the "Parameter Store" in "Systems Manager" which is where these are stored.


## Useful Links

AWS CDK documentation in Python: <https://docs.aws.amazon.com/cdk/api/latest/python/index.html>

AWS CLI documentation: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html>

Python boto3 documentation: <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>
