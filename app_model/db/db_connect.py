import fdb
import pathlib
from pathlib import Path

from app_model.db_path import DB_PATH
from app_model.variables import DB_NAME, DB_DIR, DB_SUB_DIR


class DB:
    """
    Connect to Firebird database
    """

    def __init__(self, name):
        self.name = name
        self.cursor = self.connection = None

    def __enter__(self):
        # Establishes a connection to the Firebird database when used in a 'with' statement
        self.connection = fdb.connect(host='localhost', database=self.name, user='SYSDBA',
                                      password='masterkey', charset='UTF8')
        self.cursor = self.connection.cursor()
        return self.cursor  # Returns a cursor object

    def insert_data(self, table_name):
        pass  # Placeholder for inserting data into the specified table

    def update_data(self):
        pass  # Placeholder for updating data in the database

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Commits any pending transactions and closes the database connection and cursor
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB(Path(pathlib.Path.cwd(), DB_PATH, DB_NAME))

if __name__ == '__main__':
    pass
    # db = DB(Path(DB_PATH, DB_NAME))
    # print(Path(DB_PATH, DB_NAME))
    # with db as cur:
    #     ccc = cur.execute("""SELECT * FROM age""").fetchall()
    #     for c in ccc:
    #         print(c)
    # print('Connection -> Ok')
