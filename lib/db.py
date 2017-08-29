import sqlite3
from sqlite3 import Error

def create_connection(db_path):
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except Error as e:
        print(e)

    return None

def execute_sql(database, sql_filepath, params=[]):
    # read in sql from file at path
    connection = create_connection(database)

    with open(sql_filepath, "r") as sql_file:
        command = sql_file.read().replace('\n', '')

    try:
        c = connection.cursor()
        if len(params) > 0:
            command = command % tuple(params)

        c.execute(command)
        connection.commit()
        connection.close()
    except Error as e:
        print(e)

def setup():
    DATABASE_NAME = "cryptos.db"
    execute_sql(DATABASE_NAME, "lib/sql/create_crypto_table.sql")
