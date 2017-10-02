import sqlite3
from sqlite3 import Error

class Database():
    path = ""

    def __init__(self, db_path):
        self.path = db_path

    def createConnection(self):
        try:
            connection = sqlite3.connect(self.path)
            return connection

        except Error as e:
            print(e)
            return None

    def executeSQLFile(self, sql_path, params=[]):
        connection = self.createConnection()

        with open(sql_path, "r") as sql_file:
            command = sql_file.read().replace("\n", "")

        try:
            c = connection.cursor()

            if len(params) > 0:
                print(command)
                command = command % tuple(params)

            c.execute(command)
            connection.commit()

        except Error as e:
            print(e)

        connection.close()

    def executeSQL(self, command, params=[]):
        connection = self.createConnection()

        try:
            c = connection.cursor()

            if len(params) > 0:
                command = command % tuple(params)

            c.execute(command)
            connection.commit()

        except Error as e:
            print(e)

        connection.close()

    # create table from name, column names, and column types
    def createTable(self, name, cNames, cTypes):
        if len(cNames) != len(cTypes):
            print("Number of column names does not match number of column types; try again.")
            return

        firstLine = "CREATE TABLE IF NOT EXISTS " + name + "("
        variables = ""
        for aName, aType in zip(cNames, cTypes):
            variables += aName + " " + aType + ","

        variables = variables[:-1] + ");"

        command = firstLine + variables

        self.executeSQL(command)
