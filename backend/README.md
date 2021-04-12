# Django project

## Tests
Run `pytest tests` from the `backend` directory


## Setup: Initial load of CT.gov data

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

<span style="color:red">Please note there are significant changes to Search API. Rerun Step 3 to make sure new views are created in your local database. The materialized view creation will take few minutes to complete.</span>

## Setup: Clinical Studies Search API

1. Run the pgdb container with `docker-compose up pgdb`
1. In another terminal, connect to the postgres docker container: `docker exec -it --user postgres pgdb /bin/bash`
1. Run the basic_search.sql script with the command: `psql -d aact -f database/scripts/search_studies.sql`
1. Connect to the aact database `psql -d aact`
1. Use the command `\dv` to list the views and verify that basic_search appears in the list of views.
1. Ctrl + D twice to exit psql and then the postgres container. Then `docker-compose up` to bring up the whole app.

### psql

Here's a useful psql command cheat sheet: [https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)

## API Endpoints

### Clinical Studies Search API
#### Parameters

#### Please note api endpoint name is changed to "search_studies" to be more generic.

The end point for Clinical Studies Search API is:
<http://127.0.0.1:8000/ctgov/api/search_studies>

#### Please note the change in api parameters. If metadata is required, pass "metadata_required"="True"; if metadata is not required (for example, during pagination) pass empty string as "metadata_required="".

Example query located in `database/examples/search_studies_query.json`:

	{
		"status":"Recruiting",
		"condition":"",
		"other_terms":"POETYK",
		"country":"",
		"intervention":"",
		"target":"",
		"nct_id":"",
		"eligibility_criteria":"",
		"modality":"exercise",
		"sponsor":"",
		"phase":"Phase 1",
		"start_date_from":"2019-01-01",
		"start_date_to":"2020-01-01",
		"primary_completion_date_from":"",
		"primary_completion_date_to":"",
		"first_posted_date_from":"",
		"first_posted_date_to":"",
		"results_first_posted_date_from":"",
		"results_first_posted_date_to":"",
		"last_update_posted_date_from":"",
		"last_update_posted_date_to":"",
		"study_results":"",
		"study_type":"",
		"eligibility_age":"",
		"eligibility_min_age":"25",
		"eligibility_max_age":"75",
		"eligibility_gender":"Female",
		"eligibility_ethnicity":"",
		"eligibility_condition":"",
		"eligibility_healthy_volunteer":"",
		"study_title_acronym":"",
		"study_outcome_measure":"",
		"study_collaborator":"",
		"study_ids":"",
		"study_location_terms":"",
		"study_funder_type":"Industry",
		"study_document_type":"Study Protocol",
		"study_results_submitted":"",
		"study_roa":"",
		"first":"",
		"last":"",
		"metadata_required":"True"
	}


1. Pass all of the above 'post' parameters with exact name. You can choose to pass only those parameters that have value entered/selected by user. You don't need to pass all parameters. If none of the parameters are passed, the API will get first 100 records from database.

1. 'first' and 'last' parameters are for pagination. If these parameters are blank or not passed, Django API will assume first = 0 and last = 100.

Example curl command with a timer using the example json:

`time curl -X POST http://127.0.0.1:8000/ctgov/api/search_studies -d database/examples/search_studies_query.json`

#### Output

#### Please note search results now contains "metadata" information. This means ReactJS parsing needs to be modified accordingly.

Sample result below. Note that 'intervention_name' and 'location_name' are pipe delimited values. You have to parse them to display as a list in html.


	{
		"metadata": [
			{
				"results_count": "148"
			}
		],
		"search_results": [
			{
				"status": "Completed",
				"brief_title": "Immunogenicity and Safety of Booster Dose of BoostrixTM Polio Vaccine in Previously Boosted Adults",
				"nct_id": "NCT01323959",
				"condition_name": "Acellular Pertussis|Diphtheria|Poliomyelitis|Tetanus",
				"intervention_name": "BoostrixTM Polio",
				"location_name": "GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site|GSK Investigational Site"
			},
			{
				"status": "Completed",
				"brief_title": "A Study to Determine the Excretion Balance and Pharmacokinetics of 14C-GSK573719",
				"nct_id": "NCT01362257",
				"condition_name": "Pulmonary Disease, Chronic Obstructive",
				"intervention_name": "Treatment Period 1 - IV dose of GSK573719|Treatment Period 2 - Oral dose of GSK573719",
				"location_name": "GSK Investigational Site"
			}
		]
	}

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
