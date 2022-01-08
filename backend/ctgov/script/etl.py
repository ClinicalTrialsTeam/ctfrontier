import psycopg2
import re

from datetime import datetime
from dotenv import load_dotenv
from os import getenv
from os.path import dirname, join
from psycopg2 import Error

dotenv_path = join(dirname(dirname(dirname(__file__))), ".env")
print(dotenv_path)
load_dotenv(dotenv_path)


def print_current_time(step):
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    print(f"{step} time {dt_string}")


"""
This method is used to connect to the database and execute the query that is
specified, with the provided data
query: Represents a SQL query. If dynamic data is required, this must be passed
       in the data parameter
data: A tuple or list of tuples that contain dynamic data to be added into the
      query. A list would be provided to execute multiple commands where the
      only change is the provided data. This prevents multiple opens and closes
      for the connection string.
"""


def connect_and_execute_psql(query, data):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(
            database="aact",
            user="postgres",
            password=getenv("DB_PASSWORD"),
            host="pgdb",
            port=5432,
        )

        # This means there is a single query provided and the result set should return a single query
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

        # This means multiple queries were provided and that the data object will be more complex
        elif isinstance(data, list):
            cursor = connection.cursor()
            for d in data:
                cursor.execute(query, d)
                connection.commit()

    except (Exception, Error) as error:
        print(f"Error while connecting to PostgreSQL {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()


"""
This method runs to setup the infrastructure within the PostgreSql database.
By including this method, any provided SQL scripts will be run by this script
instead of separately by the user.
"""


def ensure_supporting_infrastructure_exists():
    with open("sql-infrastructure.sql", "r") as file:
        sql_inf = file.read()
    connect_and_execute_psql(sql_inf, None)
    print("Sql Infrastructure Built")


"""
This method runs the two regex mining commands, one for Races, one for Routes
of Administration.
"""


def regex_parsing():
    # Get the data to parse
    race_records = connect_and_execute_psql(
        "SELECT nct_id, criteria FROM ctgov.eligibilities", None
    )

    # List of races to validate against. These are upper case for matching purposes only.
    # When saving to the database, they will be Title Case
    races = [
        "AMERICAN INDIAN",
        "ALASKA NATIVE",
        "ASIAN",
        "BLACK",
        "AFRICAN AMERICAN",
        "NATIVE HAWAIIAN",
        "PACIFIC ISLANDER",
        "WHITE",
        "HISPANIC",
        "LATINO",
    ]
    pattern = "|".join(races)
    race_data = []
    for record in race_records:
        results = re.findall(pattern, record[1].upper())
        if results:
            for result in results:
                race_data.append((record[0], result.title()))

    if race_data:
        # Required because regex finds all instance matches and can add
        # duplicate records
        unique_race_data = []
        for data in race_data:
            if data not in unique_race_data:
                unique_race_data.append(data)
        print(f"Processing {len(unique_race_data)} records of race data")
        connect_and_execute_psql(
            "INSERT INTO ctgov.race(nct_id, race) VALUES(%s, %s)",
            unique_race_data,
        )
    print("Race data processed")

    roa_records = connect_and_execute_psql(
        "SELECT bs.nct_id, CONCAT(bs.description, dd.description) FROM ctgov.brief_summaries bs INNER JOIN ctgov.detailed_descriptions dd ON bs.nct_id = dd.nct_id",
        None,
    )
    roa = [
        "CUTANEOUS",
        "NEBULIZATION",
        "INHALATION",
        "NASAL",
        "OTIC",
        "OCULAR",
        "VAGINAL",
        "RECTAL",
        "SUBLINGUAL",
        "BUCCAL",
        "INTRAVENOUS",
        "INTRAMUSCULAR",
        "SUBCUTANEOUS",
        "TRANSDERMAL",
        "IMPLANT",
        "ORAL",
    ]
    roa_pattern = "|".join(roa)
    roa_data = []

    for record in roa_records:
        results = re.findall(roa_pattern, record[1].upper())
        if results:
            for result in results:
                roa_data.append((record[0], result.title()))

    if roa_data:
        # Required because regex finds all instance matches and can add
        # duplicate records
        unique_roa_data = []
        for data in roa_data:
            if data not in unique_roa_data:
                unique_roa_data.append(data)
        print(
            f"Processing {len(unique_roa_data)} records of Route of Administration data"
        )

        connect_and_execute_psql(
            "INSERT INTO ctgov.route_of_administration(nct_id, roa) VALUES(%s, %s)",
            unique_roa_data,
        )
    print("ROA data processed")


print_current_time("Start")
ensure_supporting_infrastructure_exists()
regex_parsing()
print("Finished")
print_current_time("End")
