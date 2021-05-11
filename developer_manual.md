# Clinical Trials Frontier Developer Manual

CTFrontier Team Members: Balaji Ragupathi, Bry Power, Elena Arens, Mike Blanchard, Stephen Thompson, Natalie Mona Matthews

## Overview

**Github link:** <https://github.com/ClinicalTrialsTeam/ctfrontier>

There are two options for running the CTFrontier application.

1. [Local Setup](#ctfrontier-local-setup) The first option is to run CTFrontier locally using docker-compose. 
1. [Cloud Setup](#ctfrontier-cloud-setup) The second option is to run CTFrontier on AWS infrastructure using the `ctf` CLI tool.

## CTFrontier Local Setup

### Setup: Prerequisites

* Docker installed and running
* Python 3.8
* Node.js 15.12.0+


### Setup: Prepare environment

1. Clone the repo
1. In the `backend` folder there is a file `example.env`. Copy this into a new `.env` file and fill it in (this .env file be in the "backend/core" folder). `DJANGO_SECRET` should be a value you get from running python `scripts/gen_random_key.py` `DB_PASSWORD` can be whatever you want.
1. Before building your docker images, it might be a good idea to run `docker system prune -a` to clear some space in case you have any previous docker images laying around.
1. Build the docker images `docker-compose build` (This may take a little while)

### Setup: Load Data and run setup scripts

**Download the data**

1. Download `.zip` from [https://aact.ctti-clinicaltrials.org/snapshots](https://aact.ctti-clinicaltrials.org/snapshots)
1. Save this `.zip` file in the project root directory `ctfrontier`. (You should also be in the project root directory in your terminal.)
1. Unzip into `data` folder (`unzip <filename.zip> -d database/data`)

**Load the data into the database**

1. Start running the postgres container with `docker-compose up pgdb`.
1. In a new terminal tab/window connect to postgres container. `docker exec -it --user postgres pgdb /bin/bash`
1. Create the database `createdb aact`
1. Restore the database from the `.dmp` file. `pg_restore -e -v -O -x -d aact --no-owner database/data/postgres_data.dmp`
1. Start psql `psql`
1. You should see the `postgres=#` prompt.
1. Add ctgov schema to psql search path `alter role postgres in database aact set search_path = ctgov, public;`
1. Connect to the aact database: `\c aact`
1. If you run `\dt` you should see something like this...


		                  List of relations
		 Schema |            Name            | Type  |  Owner   
		--------+----------------------------+-------+----------
		 ctgov  | baseline_counts            | table | postgres
		 ctgov  | baseline_measurements      | table | postgres
		 ctgov  | brief_summaries            | table | postgres
		 ctgov  | browse_conditions          | table | postgres
		 ctgov  | browse_interventions       | table | postgres
		 ctgov  | calculated_values          | table | postgres
		 ctgov  | categories                 | table | postgres
		 ctgov  | central_contacts           | table | postgres
		 ctgov  | conditions                 | table | postgres
		 ctgov  | countries                  | table | postgres


**Run the setup scripts**

1. Ctrl + D to get out of psql
1. Run the search_stuides.sql script with the command: `psql -d aact -f database/scripts/search_studies.sql`
1. Create the countries table with the command:`psql -d aact -f database/scripts/New_Countries.sql`
1. Connect to the aact database `psql -d aact`
1. Use the command `\dv` to list the views and verify that basic_search appears in the list of views.

**Exit the container and start the application**

1. Ctrl + D to get out of psql, Ctrl + D again to get out of the postgres container.
1. Finally, `docker-compose down` to take down the postgres container and `docker-compose up` to start running the whole application.


### Usage: Running Elasticsearch

Because Elasticsearch and Kibana are highly resource intensive, `docker-compose up` does not run them by default. To run the application with Elasticsearch run `docker-compose -f elasticsearch.yml up`.

*Steps To Build Initial Elasticsearch Index*

1. In another terminal, connect to django container: `docker exec -it django /bin/sh`

1. Run `python setup_elasticsearch.py`

1. Once above command is complete, exit django container: `exit`

1. If you want to delete the index, connect to the django container run the command: `python manage.py search_index --delete`.


### Usage: Where to reach each service

Although each service communicates with each other via a Docker bridge network, each service is bound to a port on localhost. This is the list of services and which ports they are accessible on when the containers are running:

* React <http://localhost:3000>
* Django REST API framework <http://localhost:8000>
* Elasticsearch <http://localhost:9200>
* Kibana <http://localhost:5601>

### Usage: Connect to the containers

**react**  
`docker exec -it react /bin/sh`

**django**  
`docker exec -it django /bin/sh`

**pgdb**   
`docker exec -it pgdb /bin/bash` 

**Note: You can only access the db as the user postges so if you connect this way you may need to switch users or to go straight into psql `docker exec -it pgdb psql -U postgres`**

### Changing your Postgres DB password

In order to run your docker containers, `DB_PASSWORD` in `backend/.env` must match the actual postgres database password. If you want to change your postgres database password, you cannot just changed the stored value in `.env`, you must connect to postgres and change the actual postgres database password first.

Steps to take: 

1. Make sure that `DB_PASSWORD` in your `.env` file is the current postgres database password. (The way you know is you can start your django container with no errors.)
1. Start the docker containers with `docker-compose up`. If you get the error `django.db.utils.OperationalError: FATAL: password authentication failed for user “postgres”`, then the password in your `.env` is incorrect. You need to fix it and start docker again.
1. Now that your docker cointainers are running. Open a new terminal and connect to the postgres container with: `docker exec -it --user postgres pgdb /bin/bash`
1. In the same terminal, connect to the database: `psql`
1. In the same terminal, change your password using the command: `ALTER USER postgres PASSWORD '<new password>';` but replace `<new password>` with your desired password.
1. Press Ctrl + D twice to exit psql and then exit the postgres container.
1. Shut down the docker containers with: `docker-compose down`
1. Update `DB_PASSWORD` in `.env` to have the same password you just set the postgres database to have.
1. Re-start the docker containers with: `docker-compose up`


## CTFrontier Cloud Setup

The AWS Cloud Development Kit (AWS CDK) is an open source software development framework to define AWS cloud application resources using code. This project uses AWS CDK in Python to define project resources.

The project also includes a command line utility for interacting with CDK. This command line utility wraps many of the standard CDK commands and some AWS CLI commands to provide additional functionality.


### Setup: Prerequisites

* Docker installed and running

**Domain**

* You must have a domain that you can use to host the website and access to one of the below email addresses:

    * administrator@your\_domain_name
    * hostmaster@your\_domain_name
    * postmaster@your\_domain_name
    * webmaster@your\_domain_name
    * admin@your\_domain_name

**Python**

* Python 3.8
* A python virtual environment tool of your preference

**AWS CDK**

* AWS credentials configured
* AWS CLI 2.1.0+ installed and configured  <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html>
* Node.js 15.4.0+
* The `aws-cdk` Node.js toolkit installed. `npm install -g aws-cdk@latest`. (`npm list -g` to check the current versions of your globally installed node packages)

**AWS Permissions**

Your default AWS user (configured with `aws configure`) or your named aws profile (configured with `aws configure --profile <profile-name>` and specified in `cdk/.env` with `AWS_PROFILE=<profile-name>`) must have the following AWS managed policies or equivalent permissions attached:

* IAMFullAccess
* SecretsManagerReadWrite
* AmazonEC2ContainerRegistryFullAccess
* AmazonS3FullAccess
* CloudWatchFullAccess
* AmazonSSMFullAccess
* AWSCloudFormationFullAccess
* AWSLambda_FullAccess
* AmazonEC2ContainerRegistryFullAccess
* AmazonECS_FullAccess
 
 
### Setup: Local environment

1. Create an empty file `.env` in the `cdk` folder
1. Make sure that you have set up your AWS credentials (set up using `aws configure`, check to see if they exist with `ls ~/.aws/`, you should see the files `config` and `credentials`
1. If you want to use a named profile, configure a named profile using `aws configure --profile <profile-name>` and define `AWS_PROFILE` in `cdk/.env`.

Set up Python virtual environment. For example, if you were using virtualenv you might: 

1. Install virtualenv `pip install virtualenv`
1. Create your virtual environment with `virtualenv venv`
1. Start your virtual environment with `source venv/bin/activate`
(`deactivate` to turn it off)

Once you have your virtual environment set up and it is active:

1. Python dependencies are handled via `pip-tools`, so you need to install that first: `pip install pip-tools`
1. From the `ctfrontier/cdk` folder, install the dependencies by running `pip-sync requirements/dev.txt`


### The `ctf` command line tool

***Note: Always run the ctf tool from the ctfrontier/cdk folder!***

The `ctf` CLI tool is automatically installed with the dependencies.

After following the above setup instructions, you should be able to run the command `ctf` and see a list of the available command groups. For example:

	Usage: ctf [OPTIONS] COMMAND [ARGS]...

	Options:
	--help  Show this message and exit.

	Commands:
	config
	container
	docker
	stack

Run `ctf [group]` to see the available commands for that group. For example, run the `create` command in the `config` group run `ctf config create`. To see all config commands, run `ctf config`.

`ctf config` - Create, edit, delete and view the config.  
`ctf container` - Automatically build frontend and backend containers and deploy them to the stack.  
`ctf docker` - Authenticate docker.  
`ctf function` - Automatically build and deploy lambdas.  
`ctf stack` - Create, update, delete and get information about the AWS CloudFormation stack.


### Setup: Create the config

CTFrontier uses a config which is stored in AWS SSM Parameter. Using a config stored in the cloud avoids the problem of diverging configurations when multiple people are working on the same AWS infrastructure.

1. Copy the `config-example.json` file to a new json file and update the values of each config variable to appropriate values.

		{
		    "site_domain": "ctfrontier.com",
		    "django_secret": "generated-django-secret",
		    "db_host": "db_host",
		    "db_password": "db_password"
		}

		
	`site_domain` - The domain that will host the website  
	`django_secret` - Autogenerate this from `scripts/gen_random_key.py` 
	`db_host` - Put a placeholder here initially.  
	`db_password` - Put a placeholder here initially. 
	`es_host` - Put a placeholder here initially.
	`elasticsearch_enabled` - Set as false initially.

1. Run the command `ctf config create`. You will be prompted to enter an initial config file. Enter the name of your config file.

***Note: Your initial config file is just an initial config file. The actual config is stored in AWS SSM Parameter Store. Editing the local file will not modify the config.***
		
1. To view the current config run `ctf config show`. You can also pipe this output to a file to save the current configuration locally.

1. To edit the config, use `ctf config edit` which will automatically open vi or your default text editor and allow you to edit the configuration in the cloud. Alternatively, you could pipe the current config to a file with `ctf config show > some-config-file.json`, edit it there, then load the new config in with `ctf config create`.


### Setup: Bootstrapping

Before launching a new AWS CloudFormation stack, there are some resources that must be bootstrapped.

* AWS CDK provided bootstrap resources
* AWS Elastic Container Registries for storing docker images

1. Create the bootstrapped resources with `ctf stack bootstrap`

***Note: These resources can be cleaned up after deleting the "ctfrontier" CloudFormation stack with `ctf stack bootstrap.delete`***

### Setup: Create the CloudFormation stack

After setting up AWS credentials, setting up the config, and boostrapping the AWS environment, you should be ready to create the "ctfrontier" CloudFormation stack which will launch the resources needed for the application.

1. Create the stack with: `ctf stack create`
1. Approve the AWS Certificate Manager approval email which should have been sent to your domain associated email address such as admin@your_domain_name.
1. For subsequent stack changes use `ctf stack update`
1. To see the "ctfrontier" stack outputs run `ctf stack outputs`

**Check the setup**  
At this point you should have an AWS ECS cluster running with a backend and a frontend service. The backend service runs django on an EC2 instance and the frontend service runs react on Fargate. There should also be an RDS instance running. If you go to `your_domain_name` you should see the website frontend, however, the website will not be fully functional until the database is set up.


**Update the config**

Now that your stack is running you can update the database related config variables.

Use `ctf config edit` to edit. Set `db_host` to your RDS instance endpoint, set `db_password` to the database password stored in AWS Secrets Manager, and set `es_host` to your Elasticsearch VPC endpoint.

After the config has been edited. You can use `ctf config show` to confirm the correct values are set.

Finally, run `ctf stack update`, then `ctf container deploy.backend` to make sure the config changes have propagated to the running backend django task.

### Checking: Connect to the backend EC2 instance running django

At this point you should be able to connect to the container running django. The setup process should have automatically generated a file in the cdk folder `CtfBackendKeyPair.pem`.

First, add a rule to the `Ctfrontier-CtfSiteSecurityGroup` to allow your IP on port 22. Then, check that you can connect successfully. Look up the public DNS of the EC2 container running the django task and connect to it using:

`ssh -i CtfBackendKeyPair.pem ec2-user@[ec2-DNS]`

### Setup: Set up database

**Load data into RDS database**

* Before you load the data temporarily disable backups (set backup retention to 0). This is recommended by AWS to speed up performance.
* Temporarily allow all TCP from your IP address to the RDS security group by adding a rule to the `Ctfrontier-CtfDatabaseSecurityGroup`.
* Temporarily allow port 22 from your IP address to the EC2 instance running the django task by adding a rule to the `Ctfrontier-CtfSiteSecurityGroup`.
* Connect to the RDS instance via the django EC2 instance using an SSH tunnel.
* Find the RDS password in AWS Secrets Manager.

The command to create the SSH tunnel is, this is expected to not return:

	ssh -N -L 10101:[your-db-instance]:5432 -i CtfBackendKeyPair.pem ec2-user@[your-ec2-dns]

With the SSH tunnel open, in another terminal, load the data from the `.dmp` file (follow data download instructions in local development setup to get the `.dmp` file):

`pg_restore -h localhost -p 10101 -U postgres -e -v -O -x -d aact --no-owner /path/to/postgres_data.dmp`

Enter the password for RDS from AWS Secrets Manager. It is expected that the initial data load will take a long time to run.

**Run `.sql` setup script**

Once the initial data has been loaded, connect to the database in the same terminal using the same SSH tunnel and enter the same password:

`psql -h localhost -p 10101 -U postgres`

Run `alter role postgres in database aact set search_path = ctgov, public;` to add the ctgov schema to your search path.

Finally, disconnect from the RDS instance and run `psql -h localhost -p 10101 -U postgres -d aact -f /path/to/search_studies.sql` to create the database views.

The `search_studies.sql` script can be found in `database/scripts`.

### Setup: Set up elasticsearch

1. Start with `ELASTICSEARCH_ENABLED` set to false in the config. (See the config with `ctf config show`)

1. Connect to the EC2 instance running django with `ssh -i CtfBackendKeyPair.pem ec2-user@[ec2-DNS]`.

1. From within the EC2 instance, run `docker ps` to find the name of the running container and then `docker exec -it <name> /bin/sh` to connect to the container.

1. From within the django container run `python setup_elasticsearch.py`. This may take a long time but only has to be done once.

1. Exit out of the docker container / EC2 instance, then run `ctf config edit` and set `ELASTICSEARCH_ENABLED` to true.

1. Propagate this change to the CloudFormation stack resources by running `ctf stack update` to update the environment variables for the backend task. This should automatically restart the backend task with the new environment variables but if it doesn't then you can run `ctf container deploy.backend` to force a new deployment of the backend.

1. Now the website should use Elasticsearch for the "search_studies" endpoint.

1. To delete index run `python manage.py search_index --delete` from a running django task.

**At this point you should have a working version of ctfrontier in the cloud!**




