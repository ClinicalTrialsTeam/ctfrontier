import pandas
import psycopg2
import re
import spacy
import numpy
import os
from datetime import datetime
from dotenv import load_dotenv
from os.path import join, dirname
from psycopg2 import Error

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


def print_current_time():
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    print("start time", dt_string)


def connect_and_execute_psql(dbase, query, data):

    try:
        # Connect to an existing database
        connection = psycopg2.connect(
            user="postgres",
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database="aact",
        )

        # This means there is a single query provided and the result set should
        # return a single query
        if isinstance(data, tuple) or isinstance(data, type(None)):
            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Executing a SQL query
            cursor.execute(query, data)
            if query.__contains__("SELECT"):
                # Fetch result
                record = cursor.fetchall()
                return record
            else:
                connection.commit()

        # This means multiple queries were provided and that the data object
        # will be more complex
        elif isinstance(data, list):
            cursor = connection.cursor()
            for d in data:
                cursor.execute(query, d)
                connection.commit()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def ensure_supporting_infrastructure_exists():
    with open("SqlInfrastructure.sql", "r") as file:
        sql_inf = file.read()
    connect_and_execute_psql("AACT", sql_inf, None)
    print("Sql Infrastructure Built")


"""
Not blank

"""


def modalities():
    # Targets
    # Read in excel file using pandas
    # combine official symbol with synonyms into big list
    # Pull
    xl = pandas.ExcelFile("ModalityList.xlsx")
    df = xl.parse("Sheet1", parse_cols="B")
    modality = df["Modality Upper"]
    return modality


def targets():
    # Targets
    # Read in excel file using pandas
    # combine official symbol with synonyms into big list
    # Pull
    xl = pandas.ExcelFile("1-s2.0-S153204641300155X-mmc1.xlsx")
    df = xl.parse("Sheet2", parse_cols="A")
    proteins = df["Official Symbol"]
    return proteins


def target_find():
    # primary function creates tables, performes NER on all studies basic + detailed
    # descriptions then uses regex patterns to find terms for gene target and modality
    # from 1-s2.0-S153204641300155X-mmc1.xlsx and ModalityList.xlsx
    connect_and_execute_psql(
        "AACT",
        "CREATE TABLE ctgov.recognized_entities(nct_id TEXT, entity_group TEXT)",
        None,
    )

    connect_and_execute_psql(
        "AACT",
        "CREATE TABLE ctgov.target(nct_id TEXT, target TEXT)",
        None,
    )

    connect_and_execute_psql(
        "AACT",
        "CREATE TABLE ctgov.modality(nct_id TEXT, modality TEXT)",
        None,
    )

    nlp = spacy.load("en_core_sci_sm")

    study_description_records = connect_and_execute_psql(
        "AACT",
        "SELECT bs.nct_id, CONCAT(bs.description, ' ',  dd.description) FROM ctgov.brief_summaries bs INNER JOIN ctgov.detailed_descriptions dd ON bs.nct_id = dd.nct_id LIMIT 5000",
        None,
    )

    nlp_data = []  # array of all named entities recongized by scipacy model
    proteins = (
        targets()
    )  # list of all proteins in 1-s2.0-S153204641300155X-mmc1.xlsx
    modality = modalities()  # list of all modalities in ModalityList.xlsx
    protein_arr = numpy.asarray(proteins)  # convert dataframe to array
    modality_arr = numpy.asarray(modality)  # convert dataframe to array
    print(modality_arr)
    print(protein_arr)
    protein_pattern = " | ".join(
        str(v) for v in protein_arr
    )  # generate pattern for regex match
    modality_pattern = " | ".join(str(v) for v in modality_arr)

    for (
        record
    ) in study_description_records:  # create tuple of NER data for SQL insert
        nlp_tuple = nlp(record[1])
        nlp_string = ""
        for ent in nlp_tuple.ents:
            nlp_string = nlp_string + ent.text + ","
        nlp_data.append((record[0], nlp_string))

    for entry in nlp_data:
        connect_and_execute_psql(
            "AACT",
            "INSERT INTO ctgov.recognized_entities(nct_id, entity_group) VALUES (%s, %s)",
            (entry[0], entry[1]),
        )

    study_description_records = connect_and_execute_psql(  # open new connection and collect NER data limited to DRUG, BIOLOGICAL, and GENETIC types
        "AACT",
        "SELECT nct_id, entity_group FROM ctgov.recognized_entities WHERE nct_id IN (SELECT nct_id FROM ctgov.interventions WHERE intervention_type = 'Drug' OR intervention_type = 'Genetic' OR intervention_type = 'Biological')",
        None,
    )

    print(
        "Looking for proteins..."
    )  # find genetic targets in NER data, insert into DB
    for record in study_description_records:
        results = re.findall(protein_pattern, record[1].upper())
        results = list(set(results))
        if results:
            list_t = ",".join(str(r) for r in results)
            connect_and_execute_psql(
                "AACT",
                "INSERT INTO ctgov.target (nct_id, target) VALUES (%s, %s)",
                (record[0], list_t),
            )

    study_description_records = connect_and_execute_psql(  # open new connection and collect NER data ALL
        "AACT",
        "SELECT * FROM ctgov.recognized_entities",
        None,
    )

    print(
        "Looking for modalities..."
    )  # find modalities in NER data, insert into DB
    for record in study_description_records:
        results = re.findall(modality_pattern, record[1].upper())
        results = list(set(results))
        if results:
            list_t = ",".join(str(r) for r in results)
            connect_and_execute_psql(
                "AACT",
                "INSERT INTO ctgov.modality (nct_id, modality) VALUES (%s, %s)",
                (record[0], list_t),
            )


print_current_time()
target_find()
print_current_time()
