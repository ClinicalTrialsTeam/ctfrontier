# Django project

## Tests
Run `pytest tests` from the `backend` directory


## Initial load of CT.gov data

1. Download `.zip` from [https://aact.ctti-clinicaltrials.org/snapshots](https://aact.ctti-clinicaltrials.org/snapshots)
2. Unzip into `data` folder (`unzip <filename.zip> -d pgdb/data`)
3. Start running the docker containers `docker-compose up`. The first time you
run this it will take a LONG time! After the first time, much of the build
will be cached and it will not take so long.
4. Connect to postgres container. `docker exec -it --user postgres pgdb /bin/bash`
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

