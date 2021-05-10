## Elasticsearch Setup

1. Bring up docker container using the command: `docker-compose -f elasticsearch.yml up`

1. Connect to django container: `docker exec -it django /bin/sh`

1. Run the command: `python manage.py search_index --create -f`

1. Exit the django container: `exit`

1. Run the index mapping command to restrict the length of location_name and city_name fields to 32766: `curl -X PUT --header 'Content-type: application/json' http://127.0.0.1:9200/search_studies/_mapping -d @backend/elastic_search_mapping.json`. When you run this command in cloud, the URL needs to be changed based on cloud elasticsearch setting.

1. Connect to django container again: `docker exec -it django /bin/sh`

1. Run the command: `python manage.py search_index --populate -f`. This will index all the clinical trial records in the materialized view search_studies.

1. Once above command is complete, exit django container: `exit`

1. Goto `backend/core/settings.py` and make sure "ENABLE_ELASTIC" configuration is set to ON:  `ENABLE_ELASTIC = "ON"`. If this configuration is "OFF", search will be performed using Django ORM.

1. Note that in `backend/ctgov/api/views.py`, elasticsearch host is indicated as `elasticsearch:9200` (line#: 340). This needs to be changed based on cloud setting. 

1. If you want to delete the index, run the command: `curl -XDELETE 'http://localhost:9200/search_studies'` from your shell/command prompt.
