Next steps...

- shared code between lambdas
- remove stuff for dockerized lambdas
- don't delete config when stack is deleted?
maybe just manage the config separately?



docker exec -it <container-name> /bin/sh


Run Lambda Locally
https://hub.docker.com/r/amazon/aws-lambda-python

build - docker build -t <image name> .

run - docker run -p 9000:8080 <image name>

test - curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'

VSCode AWS Toolkit



pyenv activate venv
pyenv deactivate


pip install --editable .


pip-compile requirements/dev.in
pip-sync requirements/dev.txt

Create a named profile with
aws configure --profile

then save this name in cdk/.env
AWS_PROFILE="profile-name"


AWS USER PERMISSIONS NEEDED
- AmazonSSMFullAccess
- AWSCloudFormationFullAccess


Make sure you are looking at the us-east-1 region!!



~/.aws/config
[default]
region = us-east-1

[profile personal-user]
region = us-east-1

~/.aws/credentials
[default]
aws_access_key_id = default_id
aws_secret_access_key = default_key

[personal-user]
aws_access_key_id = id
aws_secret_access_key = key


TODO

make stack create/delete idempotent
- check if config already exists
- check if bootstrapping has already been done
use absolute path for dockerfile


# see stack outputs
aws cloudformation describe-stacks --stack-name ctfrontier --profile personal-user

# delete untagged images
aws ecr put-lifecycle-policy --repository-name ctf-frontend-repository --lifecycle-policy-text "file://policy.json"


# Notes (remove)

Before you load the data:

* Temporarily disable backups (set backup retention to 0). This is recommended by AWS to speed up performance.
* Connect to RDS via SSH

	psql -h hostname -p portNumber -U userName dbName -W
	
	
	psql -h ctf-postgres-db-instance.cwjk3wcpcb5v.us-east-1.rds.amazonaws.com -p 5432 -U nataliemona-personal ctf-postgres-db-instance -W
	
hostname = endpoint of RDS
port = 5432
userName = AWS user account name
dbName = DB Identifier

* Temporarily add your IP to the RDS security group
* Temporary disable backups (set backup retention to 0)

On EC2 container instance security group, allow TCP port 22 for your IP.

Example:`ssh -i CtfBackendKeyPair.pem ec2-user@[ec2-DNS]`

Mine: `ssh -i CtfBackendKeyPair.pem ec2-user@ec2-3-238-143-224.compute-1.amazonaws.com`


SSH Tunnel
`ssh -N -L 10101:ctf-db-instance.cwjk3wcpcb5v.us-east-1.rds.amazonaws.com:5432 -i CtfBackendKeyPair.pem ec2-user@ec2-3-238-143-224.compute-1.amazonaws.com`

In another terminal... 
Make sure you can connect to the database. Use: 
psql -h localhost -p 10101 -U postgres
And enter the RDS password Z4bhwhW_1C__03Gg_1ihbJ2WneEKFl (find in secrets manager)

Load the data from the .dmp file
`pg_restore -h localhost -p 10101 -U postgres -e -v -O -x -d aact --no-owner ../database/data/postgres_data.dmp`

ALTER ROLE
Connect to the database with: `psql -h localhost -p 10101 -U postgres`
Enter the password
Run `alter role postgres in database aact set search_path = ctgov, public;`

Run the .sql setup script
`psql -h localhost -p 10101 -U postgres -d aact -f database/scripts/search_studies.sql`


Update database endpoint and password in config

