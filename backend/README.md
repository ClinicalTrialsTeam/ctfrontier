# Django project

## Tests
Run `pytest tests` from the `backend` directory


## Initial load of CT.gov data

1. Download `.zip` from [https://aact.ctti-clinicaltrials.org/snapshots](https://aact.ctti-clinicaltrials.org/snapshots)
1. Save this `.zip` file in the project root directory `ctfrontier`. (You should also be in the project root directory in your terminal.)
2. Unzip into `data` folder (`unzip <filename.zip> -d database/data`)
3. Start running the postgres container with `docker-compose up pgdb`. The first time you
run this it will take a LONG time! After the first time, much of the build
will be cached and it will not take so long.
4. In a new terminal tab/window connect to postgres container. `docker exec -it --user postgres pgdb /bin/bash`
5. Create the database `createdb aact`
6. Restore the database from the `.dmp` file. `pg_restore -e -v -O -x -d aact --no-owner database/data/postgres_data.dmp`
7. Start psql `psql`
8. You should see the `postgres=#` prompt.
9. Add ctgov schema to pSQL search path `alter role postgres in database aact set search_path = ctgov, public;`
10. Connect to the aact database: `\c aact`
11. If you run `\dt` you should see something like this...


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
12. Ctrl + D to get out of psql, Ctrl + D again to get out of the postgres container.
13. Finally, `docker-compose down` to take down the postgres container and `docker-compose up` to start running the whole application.

### psql

Here's a useful psql command cheat sheet: [https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)

## API Endpoints

### Basic Search API

#### Prerequisite

1. Connect to the postgres docker container: `docker exec -it --user postgres pgdb /bin/bash`
1. Run the basic_search.sql script with the command: `psql -d aact -f database/scripts/basic_search.sql`
1. Connect to the aact database `psql -d aact`
1. Use the command `\dv` to list the views and verify that basic_search appears in the list of views.


#### Parameters

The end point for Basic Search API is:
<http://127.0.0.1:8000/ctgov/api/basic_search>

Example query located in`database/examples/basic_search_query.json`:

	{
	    "status":"Recruiting",
	    "condition":"",
	    "other_terms":"POETYK",
	    "country":"",
	    "intervention":"",
	    "target":"",
	    "nct_id":"",
	    "eligibility_criteria":"",
	    "first":"",
	    "last":""
	}

Example curl command with a timer using the example json:

`time curl -X POST http://127.0.0.1:8000/ctgov/api/basic_search -d database/examples/basic_search_query.json`

#### Output


Sample result below. Note that 'intervention_name' and 'location_name' are pipe delimited values. You have to parse them to display as a list in html.


	{
	    "status": "Recruiting",
	    "brief_title": "An Investigational Study to Evaluate Experimental Medication BMS-986165 Compared to Placebo in Participants With Plaque Psoriasis (POETYK-PSO-3) in Mainland China, Taiwan, and South Korea",
	    "nct_id": "NCT04167462",
	    "condition_name": "Psoriasis",
	    "intervention_name": "BMS-986165|Placebo",
	    "location_name": "Local Institution|Local Institution|Local Institution"
	}


1. Pass all of the above 'post' parameters with exact name even though one of the parameter may be blank. If it is blank, pass an empty double quoted string.

1. 'first' and 'last' is for pagination. If it is blank, Django backend will assume first = 0 and last = 100. I think you can accomplish pagination using hidden fields in your html and keep incrementing with offset for every 'previous' or 'next' action.


### Countries API

The end point for Countries API is:
<http://127.0.0.1:8000/ctgov/api/countries>

Countries API will return a unique list of countries associated with studies in the following format.

	[
	    {
	        "country": ""
	    },
	    {
	        "country": "Afghanistan"
	    },
	    {
	        "country": "Albania"
	    },
	    {
	        "country": "Algeria"
	    },
	    {
	        "country": "American Samoa"
	    },
	    {
	        "country": "Andorra"
	    },
	    {
	        "country": "Angola"
	    },
	    {
	        "country": "Antarctica"
	    }
	    {
	        ...
	    }
	]

## Changing your Postgres DB password

In order to run your docker containers, `DB_PASSWORD` in `backend/core/.env` must match the actual postgres database password. If you want to change your postgres database password, you cannot just changed the stored value in `.env`, you must connect to postgres and change the actual postgres database password first.

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