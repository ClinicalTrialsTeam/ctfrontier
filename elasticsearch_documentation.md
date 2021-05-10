## Elasticsearch Setup

#### Local Instructions

1. Bring up docker container using the command: `docker-compose -f elasticsearch.yml up`

1. In another terminal, connect to django container: `docker exec -it django /bin/sh`

1. Run the command: `python manage.py search_index --create -f`

1. In another terminal, run the index mapping command to restrict the length of location_name and city_name fields to 32766: `curl -X PUT --header 'Content-type: application/json' http://127.0.0.1:9200/search_studies/_mapping -d @backend/elastic_search_mapping.json`. When you run this command in cloud, the URL needs to be changed based on cloud elasticsearch setting.

1. In the terminal connected to the django container, run the command: `python manage.py search_index --populate -f`. This will index all the clinical trial records in the materialized view search_studies.

1. Once above command is complete, exit django container: `exit`

1. If you want to delete the index, run the command: `curl -XDELETE 'http://localhost:9200/search_studies'` from your shell/command prompt.


#### Cloud Instructions

1. Run `ctf config edit` and set ELASTICSEARCH_ENABLED to true.

1. Propogate this change to the CloudFormation stack resouces by running `ctf stack update`.

(Have django container automatically run commands if elasticsearch is enabled)

1. To delete index run curl XDELETE (write detailed command here) from the django container.