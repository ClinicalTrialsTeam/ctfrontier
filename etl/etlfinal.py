import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv
from os.path import join, dirname
from sql_scripts import SqlScripts

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
limit = 100

sql_scripts = SqlScripts()

ctti_connection = psycopg2.connect(
    user="ctfrontiercsci599",
    password=os.getenv("CTTI_DB_PASSWORD"),
    host=os.getenv("CTTI_DB_HOST"),
    port=os.getenv("CTTI_DB_PORT"),
    database="aact",
)

ctf_connection = psycopg2.connect(
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database="aact",
)

ctf_connection.set_session(autocommit=True)


# This method runs the extraction and insertion into the new database
# All of the queries run here exist in a separate file
def elt_connection(queries, data):
    ctti_cursor = None
    ctf_cursor = None

    try:
        for query in queries:
            # Get records from CTTI datasource
            split_query = query.split("|")
            ctti_cursor = ctti_connection.cursor()
            ctti_cursor.execute(split_query[0], data)
            records = ctti_cursor.fetchall()

            # Insert or Update new records
            if records is not None:
                for record in records:
                    ctf_cursor = ctf_connection.cursor()
                    ctf_cursor.execute(split_query[1], record)
                    ctf_connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if ctti_connection:
            if ctti_cursor:
                ctti_cursor.close()
        if ctf_connection:
            if ctf_cursor:
                ctf_cursor.close()


# This method is used to pull the initial metadata for the data extraction
# The main column used is the last_run_date. Additional columns exist for
# building out microbatching in the future
def get_etl_metadata():
    ctti_cursor = None
    ctf_cursor = None

    try:
        ctf_cursor = ctf_connection.cursor()
        ctf_cursor.execute(sql_scripts.last_run_date)
        last_run_date_rec = ctf_cursor.fetchone()

        # Get Insert Count from CTTI
        split_insert_query = sql_scripts.insert_count_from_ctti.split("|")
        ctti_cursor = ctti_connection.cursor()
        ctti_cursor.execute(split_insert_query[0], (last_run_date_rec))
        insert_count_ctti = ctti_cursor.fetchone()

        # Add Insert Count to CTF
        ctf_cursor = ctf_connection.cursor()
        ctf_cursor.execute(split_insert_query[1], insert_count_ctti)
        ctf_connection.commit()

        # Get Update Count from CTTI
        split_update_query = sql_scripts.update_count_from_ctti.split("|")
        ctti_cursor = ctti_connection.cursor()
        ctti_cursor.execute(
            split_update_query[0], (last_run_date_rec, last_run_date_rec)
        )
        update_count_ctti = ctti_cursor.fetchone()

        # Add Update Count to CTF
        ctf_cursor = ctf_connection.cursor()
        ctf_cursor.execute(split_update_query[1], update_count_ctti)
        ctf_connection.commit()

        # Pull back all of the current metadata for ETL, which will allways
        # be one record
        ctf_cursor = ctf_connection.cursor()
        ctf_cursor.execute(sql_scripts.get_etl_metadata)
        return ctf_cursor.fetchone()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if ctti_connection:
            if ctti_cursor:
                ctti_cursor.close()
            # ctti_connection.close()
        if ctf_connection:
            if ctf_cursor:
                ctf_cursor.close()
            # ctf_connection.close()


# Update the ctgov.etl table with the current date so when it runs next it can
# pull the next set of data
def update_last_run():
    # ctf_connection = None
    ctf_cursor = None

    try:
        # Update last run date
        ctf_cursor = ctf_connection.cursor()
        ctf_cursor.execute(sql_scripts.update_last_run_date, [datetime.now()])
        ctf_connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if ctf_connection:
            if ctf_cursor:
                ctf_cursor.close()


# Update the ctgov.etl table with the current date so when it runs next it can
# pull the next set of data
def rebuild_views():
    # ctf_connection = None
    ctf_cursor = None

    try:
        # Update last run date
        ctf_cursor = ctf_connection.cursor()
        ctf_cursor.execute(sql_scripts.rebuild_search_studies)
        ctf_cursor.execute(sql_scripts.rebuild_all_sponsors_type)
        ctf_cursor.execute(sql_scripts.rebuild_all_documents)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if ctf_connection:
            if ctf_cursor:
                ctf_cursor.close()


print(datetime.now())

# Pull back initial metadata
etl_metadata = get_etl_metadata()

last_run_date = etl_metadata[0]

insert_current_offset = etl_metadata[1]
insert_max_rows = etl_metadata[2]

update_current_offset = etl_metadata[3]
update_max_rows = etl_metadata[4]

# Inserts
insert_queries = [
    sql_scripts.insert_studies,
    sql_scripts.insert_conditions,
    sql_scripts.insert_detailed_descriptions,
    sql_scripts.insert_countries,
    sql_scripts.insert_interventions,
    sql_scripts.insert_keywords,
    sql_scripts.insert_eligibilities,
    sql_scripts.insert_facilities,
    sql_scripts.insert_brief_summaries,
    sql_scripts.insert_sponsors,
    sql_scripts.insert_outcomes,
    sql_scripts.insert_results_groups,
    sql_scripts.insert_outcome_measures,
    sql_scripts.insert_id_information,
    sql_scripts.insert_documents,
]
for offset in range(0, insert_max_rows, limit):
    elt_connection(insert_queries, (last_run_date, limit, offset))

print("Insert Complete")

# Updates
update_queries = [
    sql_scripts.update_studies,
    sql_scripts.update_conditions,
    sql_scripts.update_detailed_descriptions,
    sql_scripts.update_countries,
    sql_scripts.update_interventions,
    sql_scripts.update_keywords,
    sql_scripts.update_eligibilities,
    sql_scripts.update_facilities,
    sql_scripts.update_brief_summaries,
    sql_scripts.update_sponsors,
    sql_scripts.update_outcomes,
    sql_scripts.update_results_groups,
    sql_scripts.update_outcome_measures,
    sql_scripts.update_id_information,
    sql_scripts.update_documents,
]

for offset in range(0, update_max_rows, limit):
    elt_connection(update_queries, (last_run_date, last_run_date, limit,
                   offset))

print("Update Complete")
update_last_run()

rebuild_views()

print(datetime.now())
