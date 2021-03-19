# Django project

## Tests
Run `pytest tests` from the `backend` directory


## API Endpoints

### Basic Search API

#### Prerequisite

1. Connect to the postgres docker container 
```docker exec -it --user postgres pgdb /bin/bash```
2. Run the command: 

`psql -d aact -f data/database_scripts/basic_search.sql`


#### Parameters

The end point for Basic Search API is:
<http://127.0.0.1:8000/ctgov/api/basic_search>

The post format for the basic_search API should be:


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

Curl command

	curl -d '{"status":"Recruiting","condition":"","other_terms":"POETYK","country":"",
		    "intervention":"",
		    "target":"",
		    "nct_id":"",
		    "eligibility_criteria":"",
		    "first":"",
		    "last":""}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:8000/ctgov/api/basic_search

#### Output


Sample result below. Note that 'intervention_name' and 'location_name' are pipe delimited values. You have to parse them to display as a list in html.

```
{
    "status": "Recruiting",
    "brief_title": "An Investigational Study to Evaluate Experimental Medication BMS-986165 Compared to Placebo in Participants With Plaque Psoriasis (POETYK-PSO-3) in Mainland China, Taiwan, and South Korea",
    "nct_id": "NCT04167462",
    "condition_name": "Psoriasis",
    "intervention_name": "BMS-986165|Placebo",
    "location_name": "Local Institution|Local Institution|Local Institution"
}
```

1. Pass all of the above 'post' parameters with exact name even though one of the parameter may be blank. If it is blank, pass an empty double quoted string.

2. 'first' and 'last' is for pagination. If it is blank, Django backend will assume first = 0 and last = 100. I think you can accomplish pagination using hidden fields in your html and keep incrementing with offset for every 'previous' or 'next' action.


### Countries API

The end point for Countries API is:
<http://127.0.0.1:8000/ctgov/api/countries>

Countries API will return a unique list of countries associated with studies in the following format.

```
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
```

