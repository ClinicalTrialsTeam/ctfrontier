from os import getenv, putenv
import requests
import subprocess
import logging

# Create a logger for this file
logger = logging.getLogger(__name__)

# Create index if it doesn't already exist
print("Create index")
r = subprocess.run(
    "python manage.py search_index --create",
    shell=True,
    capture_output=True,
    text=True,
)
if r.returncode != 0:
    if "resource_already_exists_exception" in r.stderr:
        logger.info("search_index already exists")
        print("search_index already exists")
        # sys.exit()
    else:
        raise Exception

# Run the index mapping command to restrict the length of location
# name and cityname fields to 32766
print("Run index mapping command")
r = requests.put(
    f"{getenv('ES_HOST')}/search_studies/_mapping",
    headers={"Content-type": "application/json"},
    data=open("elastic_search_mapping.json", "rb"),
)
r.raise_for_status
print("Index mapping successful")

# Populate the elasticsearch mappings with the django models data
print("Populate elasticsearch mappings")
r = subprocess.run(
    "python manage.py search_index --populate",
    shell=True,
    capture_output=True,
    text=True,
)
if r.returncode != 0:
    print(r.stderr)
    raise Exception("Failed to populate elasticsearch mappings")
print("Successfully populated elasticsearch mappings")

print("Set django to use elasticsearch")
putenv("ELASTICSEARCH_ENABLED", "true")
