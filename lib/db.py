import sqlite3
from sqlite3 import Error

def create_connection(db_path):
    try:
        connection = sqlite3.connect(db_path)
        print("Connected to database with version "  + sqlite3.version)

    except Error as e:
        print(e)

    finally:
        connection.close()

def execute_sql(connection, sql_file):
    try:
        c = connection.cursor()
        c.execute(sql_file)
    except Error as e:
        print(e)

