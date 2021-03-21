import hashlib
import json
import os.path
import psycopg2
import requests
import shutil
import zipfile
from psycopg2 import Error
from types import SimpleNamespace

# globals
download_directory = os.path.dirname(os.path.realpath(__file__))
download_file_name = "AllAPIJSON.zip"
extract_directory = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "ctgov"
)
fullName = os.path.join(download_directory, download_file_name)
url = "https://ClinicalTrials.gov/AllAPIJSON.zip"

select_query = "SELECT hashed_json FROM ctgov.Study WHERE nct_id = (%s)"

update_query = ""


# Properly quote from stack overflow
def download_json_data():

    # Download the json zip file
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(fullName, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    print("Download complete")


# Properly quote from stack overflow
def unzip_json_file():
    os.makedirs(extract_directory, exist_ok=True)
    with zipfile.ZipFile(fullName, "r") as zip_ref:
        zip_ref.extractall(extract_directory)
    print("Extract complete")


# Properly quote from stack overflow
def connect_and_execute_postgresql(query, data):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
            database="ctf",
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute(query, data)
        # Fetch result
        record = cursor.fetchone()

        return record

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_current_nctid_hash(nct_id):
    data = nct_id
    connect_and_execute_postgresql(select_query, data)


def deserialize_and_update():
    for root, subdirs, files in os.walk(extract_directory):
        for nct_file in files:
            nct_file_path_and_name = os.path.join(root, nct_file)
            """ If the file is a json file, then it will be a study. If
                not, it could be a metadata or support type of file that
                should be ignored"""
            if ".json" in nct_file:
                with open(nct_file_path_and_name, "rb") as file:
                    json_data = file.read()
                new_file_hash = hashlib.md5(json_data).hexdigest()
                # splitting on the '.' will ensure only the filename, or NCT_ID, is selected
                old_file_hash = connect_and_execute_postgresql(
                    select_query, nct_file.split("."[0])
                )

                if new_file_hash != old_file_hash:
                    print(new_file_hash)
                    print(old_file_hash)
                    print(
                        "Hashes don't match"
                    )  # to be removed once ETL process is fully functional
                    study_to_update = json.loads(
                        json_data, object_hook=lambda d: SimpleNamespace(**d)
                    )

                    print(
                        study_to_update.FullStudy.Study.ProtocolSection.IdentificationModule.NCTId
                    )

                    # updates the study record
                    # connect_and_execute_postgresql(update_query, )
                os.remove(nct_file_path_and_name)
            if len(os.listdir(root)) == 0:
                os.rmdir(root)


# ETL Process currently all steps commented out
# download_json_data()
# unzip_json_file()
# deserialize_and_update()
