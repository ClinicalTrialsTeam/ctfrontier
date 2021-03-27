
# CTFrontier CDK documentation

## Requirements

#### Python

* Python 3.8
* The Python `virtualenv` package (or similar if you are used to using a different one)

#### CDK

* AWS CLI installed and configured  <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html>
* Node.js 15.4.0+
* The `aws-cdk` Node.js toolkit installed. `npm install -g aws-cdk@1.94.1`. (`npm list -g` to check the current versions of your globally installed node packages)
 

## Set up

#### Local environment setup

1. Make sure that you have set up your AWS credentials (set up using `aws configure`, check to see if they exist with `ls ~/.aws/`, you should see the files `config` and `credentials`

Set up Python virtual environment

1. Install virtualenv `pip install virtualenv`
1. Create your virtual environment with `virtualenv venv`
1. Start your virtual environment with `source venv/bin/activate`
(`deactivate` to turn it off)
1. Python dependencies are handled via `pip-tools`, so you need to install that first: `pip install pip-tools`
1. Install the dependencies by running `pip-sync`


#### AWS Permissions

Your default AWS user (configured with `aws configure`) or your named aws profile (configured with `aws configure --profile <profile-name>` and specified in `cdk/.env` with `AWS_PROFILE=<profile-name>` must have the following AWS managed policies or equivalent permissions attached:

* IAMFullAccess
* AmazonEC2ContainerRegistryFullAccess
* AmazonS3FullAccess
* CloudWatchFullAccess
* AmazonSSMFullAccess
* AmazonSSNFullAccess
* AWSCloudFormationFullAccess
* AWSLambda_FullAccess

## Running the project



