import sqlite3
from sqlite3 import Error

def create_connection(db_path):
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except Error as e:
        print(e)
   
    return None

def execute_sql(connection, sql_file):
    try:
        c = connection.cursor()
        c.execute(sql_file)
    except Error as e:
        print(e)

def setup():
    database = "cryptos.db"

    connection = create_connection(database)

