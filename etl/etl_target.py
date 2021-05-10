import pandas
import psycopg2
import re
import spacy
import numpy
import os
from datetime import datetime
from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


def connect_and_execute_psql(query, data):

    connection = None
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
            if query.__contains__("SELECT") and not query.__contains__(
                "CREATE"
            ):
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

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error, flush=True)
    finally:
        if connection:
            cursor.close()
            connection.close()


def ensure_supporting_infrastructure_exists():
    with open("SqlInfrastructure.sql", "r") as file:
        sql_inf = file.read()
    connect_and_execute_psql(sql_inf, None)
    print("Sql Infrastructure Built", flush=True)


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
        "DROP TABLE ctgov.recognized_entities, ctgov.target, ctgov.modality",
        None,
    )

    connect_and_execute_psql(
        "CREATE TABLE ctgov.recognized_entities(nct_id TEXT, entity_group TEXT)",
        None,
    )

    connect_and_execute_psql(
        "CREATE TABLE ctgov.target(nct_id TEXT, target TEXT)",
        None,
    )

    connect_and_execute_psql(
        "CREATE TABLE ctgov.modality(nct_id TEXT, modality TEXT)",
        None,
    )

    nlp = spacy.load("en_core_sci_sm")

    sql_command = "SELECT bs.nct_id, CONCAT(bs.description, ' ',  dd.description) FROM ctgov.brief_summaries bs INNER JOIN ctgov.detailed_descriptions dd ON bs.nct_id = dd.nct_id"
    print(f"Run command: {sql_command}")
    study_description_records = connect_and_execute_psql(
        sql_command,
        None,
    )
    n_records = len(study_description_records)

    nlp_data = []  # array of all named entities recognized by scipacy model
    proteins = (
        targets()
    )  # list of all proteins in 1-s2.0-S153204641300155X-mmc1.xlsx
    modality = modalities()  # list of all modalities in ModalityList.xlsx
    protein_arr = numpy.asarray(proteins)  # convert dataframe to array
    modality_arr = numpy.asarray(modality)  # convert dataframe to array
    print(modality_arr, flush=True)
    print(protein_arr, flush=True)
    protein_pattern = " | ".join(
        str(v) for v in protein_arr
    )  # generate pattern for regex match
    modality_pattern = " | ".join(str(v) for v in modality_arr)

    for (i, record) in enumerate(
        study_description_records
    ):  # create tuple of NER data for SQL insert
        print(f"NLP: Processing record #{i + 1} of {n_records}...", flush=True)
        nlp_tuple = nlp(record[1])
        nlp_string = ""
        for ent in nlp_tuple.ents:
            nlp_string = nlp_string + ent.text + ","
        nlp_data.append((record[0], nlp_string))

    sql_command = "INSERT INTO ctgov.recognized_entities(nct_id, entity_group) VALUES (%s, %s)"
    print(f"Run command: {sql_command}")
    for entry in nlp_data:
        connect_and_execute_psql(
            sql_command,
            (entry[0], entry[1]),
        )

    study_description_records = connect_and_execute_psql(  # open new connection and collect NER data limited to DRUG, BIOLOGICAL, and GENETIC types
        "SELECT nct_id, entity_group FROM ctgov.recognized_entities WHERE nct_id IN (SELECT nct_id FROM ctgov.interventions WHERE intervention_type = 'Drug' OR intervention_type = 'Genetic' OR intervention_type = 'Biological')",
        None,
    )

    print(
        "Looking for proteins...",
        flush=True,
    )  # find genetic targets in NER data, insert into DB
    for i, record in enumerate(study_description_records):
        print(
            f"Proteins: Processing record #{i + 1} of {n_records}...",
            flush=True,
        )
        results = re.findall(protein_pattern, record[1].upper())
        results = list(set(results))
        if results:
            list_t = ",".join(str(r) for r in results)
            connect_and_execute_psql(
                "INSERT INTO ctgov.target (nct_id, target) VALUES (%s, %s)",
                (record[0], list_t),
            )

    study_description_records = connect_and_execute_psql(  # open new connection and collect NER data ALL
        "SELECT * FROM ctgov.recognized_entities",
        None,
    )

    print(
        "Looking for modalities...",
        flush=True,
    )  # find modalities in NER data, insert into DB
    for i, record in enumerate(study_description_records):
        print(
            f"Modalities: Processing record #{i + 1} of {n_records}...",
            flush=True,
        )
        results = re.findall(modality_pattern, record[1].upper())
        results = list(set(results))
        if results:
            list_t = ",".join(str(r) for r in results)
            connect_and_execute_psql(
                "INSERT INTO ctgov.modality (nct_id, modality) VALUES (%s, %s)",
                (record[0], list_t),
            )


def endpoints():
    sql_command = """CREATE MATERIALIZED VIEW ctgov.test AS SELECT spns.name sponsor,
    stds.brief_title study_title,
    stds.study_type study_type,
    cv.registered_in_calendar_year entry_year,
    stds.nct_id study_id,
    lnks.url url,
    conds.name indication,
    dg.title treatment_name,
    dg.description treatment_duration,
    dg.description treatment_duration_unit,
    stds.phase study_phase,
    oag.ctgov_group_code arm_number,
    otcms.title arm_treatment,
    otcms.time_frame arm_dose_unit_regimen,
    bc.count total_study_number_participants,
    oc.count arm_number_of_participants,
    oa.p_value p_value,
    oa.p_value_description p_value_description,
    oa.method_description statistical_method,
    dgnotcms.time_frame arm_duration,
    otcms.title arm_endpoint,
    otcms.description endpoint_description,
    concat(elig.minimum_age, maximum_age) AS arm_population_age_group,
    CASE WHEN elig.gender = 'Male' THEN '100%'
    WHEN elig.gender = 'Female' THEN '0%'
    WHEN elig.gender = 'All' THEN 'Between 1% and 99%'
    END AS arm_population_male_percent,
    mods.modality arm_modality
    FROM ctgov.sponsors spns
    LEFT JOIN ctgov.studies stds
    ON spns.nct_id = stds.nct_id
    LEFT JOIN ctgov.calculated_values cv
    ON spns.nct_id = cv.nct_id
    LEFT JOIN ctgov.links lnks
    ON spns.nct_id = lnks.nct_id
    LEFT JOIN ctgov.conditions conds
    ON spns.nct_id = conds.nct_id
    LEFT JOIN ctgov.design_groups dg
    ON spns.nct_id = dg.nct_id
    LEFT JOIN ctgov.outcome_analysis_groups oag
    ON spns.nct_id = oag.nct_id
    LEFT JOIN ctgov.baseline_counts bc
    ON spns.nct_id = bc.nct_id
    LEFT JOIN ctgov.outcome_counts oc
    ON spns.nct_id = oc.nct_id
    LEFT JOIN ctgov.outcome_analyses oa
    ON spns.nct_id = oa.nct_id
    LEFT JOIN ctgov.design_outcomes dgnotcms
    ON spns.nct_id = dgnotcms.nct_id
    LEFT JOIN ctgov.outcomes otcms
    ON spns.nct_id = otcms.nct_id
    LEFT JOIN ctgov.eligibilities elig
    ON spns.nct_id = elig.nct_id
    LEFT JOIN ctgov.modality mods
    ON spns.nct_id = mods.nct_id
    WHERE oag.ctgov_group_code LIKE 'O%'
    ORDER BY spns.nct_id, oag.ctgov_group_code, conds.name, dg.title LIMIT 2000"""

    connect_and_execute_psql(sql_command, None)


def current_time():
    return datetime.now().strftime("%H:%M:%S")


print(f"start time: {current_time()}")
# target_find()
endpoints()
print(f"finish time: {current_time()}")
