# Django project

## Tests
Run `pytest tests` from the `backend` directory

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
