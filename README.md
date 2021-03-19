[![python build](https://github.com/ClinicalTrialsTeam/ctfrontier/actions/workflows/python-checks.yml/badge.svg)](https://github.com/ClinicalTrialsTeam/ctfrontier/actions/workflows/python-checks.yml)
[![react build](https://github.com/ClinicalTrialsTeam/ctfrontier/actions/workflows/react-checks.yml/badge.svg)](https://github.com/ClinicalTrialsTeam/ctfrontier/actions/workflows/react-checks.yml)

# Clinical Trials Project

## Prerequisites

* Docker installed and running
* Python 3.9
* Node.js 15.4.0+


## Setup

1. Clone the repo
1. In the "backend/core" folder there is a file `example.env`.
Copy this into a new `.env` file and fill it in (this .env file be in the "backend/core" folder).
`DJANGO_SECRET` should be a value you get from running `python scripts/gen_random_key.py`
`DB_PASSWORD` can be whatever you want.
1. Before building your docker images, it might be a good idea to run `docker system prune` to clear some space in case you have any previous docker images laying around.
1. Build the docker image `docker-compose build` (This may take a little while)
1. Follow the steps below for "Running the project"

#### Developers-only
1. Run `pip install -r requirements-dev.txt` then install git hook scripts: `pre-commit install` (see Linting - Django/Python).
1. Install ESLint and Python linting packages to your IDE. (Suggestions for VSCode users: [Python package](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint))

## Linting

Linting enforces common code style rules. It can help keep everyone's code consistent and can prevent common errors.

### React/JavaScript 
This project has an ESLint configuration file. You will need to install ESLint package to give you hints in your IDE on how to fix the linting errors. The React project will not compile with ESLint errors.

For VSCode this is the package to install:
[VSCode ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

### Django/Python

For Python we use black autoformatter because it's the simplest to use. To run it on your code simply run `black backend` and it will automatically clean up your code.

**Pre-commit check**  
If you forget to run `black backend` to reformat your code, the pre-commit check will fail when you attempt to commit and it will automatically format your files for you. When this happens, simply add the modified files and try to commit again - this time it should pass.

**Github action**  
There is also a Github action that automatically checks for linting errors. See the result of these checks here: [https://github.com/ClinicalTrialsTeam/ctfrontier/actions](https://github.com/ClinicalTrialsTeam/ctfrontier/actions)

## Running the project

1. Run the project with `docker-compose up`
1. If all goes well, your React app should be accessible at: [http://localhost:3000](http://localhost:3000)
1. The Django REST API should be at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
1. Run `docker-compose down` or just `ctrl-C` to take everything down


## Initial load of CT.gov data

1. Download `.zip` from [https://aact.ctti-clinicaltrials.org/snapshots](https://aact.ctti-clinicaltrials.org/snapshots)
2. Unzip into `data` folder (`unzip <filename.zip> -d pgdb/data`)
3. Start running the docker containers `docker-compose up`. The first time you
run this it will take a LONG time! After the first time, much of the build
will be cached and it will not take so long.
4. Connect to postgres container. `docker exec -it --user postgres pgdb /bin/bash`
5. Create the database `createdb aact`
6. Restore the database from the `.dmp` file. `pg_restore -e -v -O -x -d aact --no-owner pgdb/data/postgres_data.dmp`
7. Start psql `psql`
8. You should see the `postgres=#` prompt.
9. Add ctgov schema to pSQL search path `alter role postgres in database aact set search_path = ctgov, public;`
10. Connect to the aact database: `\c aact`
11. If you run `\dt` you should see something like this...

```
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
```


## File Structure

	.
	├── .gitignore
	├── README.md
	├── backend 
	├── cdk 	
	├── frontend
	├── scripts				
	└── docker-compose.yml
	
`.gitignore` - Project wide gitignore

`backend` - Folder for all Django server code.

`cdk` - AWS CDK infrastructure code

`frontend` - Folder for all React client code.

`scripts` - Folder for any helpful scripts not directly part of the project.

`docker-compose.yml` - A docker file that defines how the react, django and pgdb docker containers will be run together. (The pgdb doesn't have its own docker file because the base setup for the postgres container is using a predefined image from dockerhub `image: postgres` without much additional setup needed).

### React Frontend

	frontend
	├── Dockerfile
	├── README.md
	├── package-lock.json
	├── package.json
	├── public
	│   ├── favicon.ico
	│   ├── index.html
	│   ├── logo192.png
	│   ├── logo512.png
	│   ├── manifest.json
	│   └── robots.txt
	└── src
	    ├── App.css
	    ├── App.js
	    ├── App.test.js
	    ├── index.css
	    ├── index.js
	    ├── logo.svg
	    ├── reportWebVitals.js
	    └── setupTests.js

`frontend/Dockerfile` - A Dockerfile that defines the base build for the django Docker container. This does some initial setup and installation of libraries on the django build. This file is run by the `docker-compose.yml` file by this line: `build: ./frontend`

### Django Backend

	backend
	├── Dockerfile
	├── core
	│   ├── __init__.py
	│   ├── asgi.py
	│   ├── example.env
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── manage.py
	├── requirements.in
	└── requirements.txt

`backend/Dockerfile` - A Dockerfile that defines the base build for the django Docker container. This does some initial setup and installation of libraries on the django build. This file is run by the `docker-compose.yml` file by this line: `build: ./backend`

`backend/requirements.in` - This is where you would add python libraries that you want to include in the project.

`backend/requirements.txt` - This file should NOT be manually edited. This file is auto generated by a script that takes in the `requirements.in` and outputs a `requirements.txt` file with the proper versions of each library.

## Other useful commands

### Docker

`docker images` - see your docker images

`docker ps` - see your currently running docker containers

### psql

Here's a useful psql command cheat sheet: [https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)

## Connect to the containers

### react
`docker exec -it react /bin/bash`

### django
`docker exec -it django /bin/bash`

### pgdb
`docker exec -it pgdb /bin/bash` (note: you can only access the db as the user postges so if you connect this way you may need to switch users)

or to go straight into psql `docker exec -it pgdb psql -U postgres`
