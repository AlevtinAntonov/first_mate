import fdb
import pathlib
from pathlib import Path

from app_model.variables import DB_NAME, DB_DIR, DB_SUB_DIR


# from functions import path_to_file
# from variables import DB_DIRECTORY, DB_NAME


class DB:
    """
    Connect to Firebird database
    """

    def __init__(self, name):
        self.name = name
        self.cursor = self.connection = None

    def __enter__(self):
        self.connection = fdb.connect(host='localhost', database=self.name, user='SYSDBA',
                                      password='masterkey', charset='UTF8')
        self.cursor = self.connection.cursor()
        return self.cursor

    def insert_data(self, table_name):
        pass

    # def insert_referral(self, table_name, referral_number):
    #     pass

    def update_data(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


# print(Path(pathlib.Path.cwd(), DB_DIRECTORY, DB_NAME))
# db = DB(Path(pathlib.Path.cwd(), 'DB_DEV.FDB'))
db = DB(Path(pathlib.Path.cwd(), DB_DIR, DB_SUB_DIR, DB_NAME))

if __name__ == '__main__':
    # print(Path(pathlib.Path.home(), 'DB_DEV.FDB'))
    # db = DB(Path(pathlib.Path.cwd(), 'DB_DEV.FDB'))
    with db as cur:
        ccc = cur.execute("""SELECT * FROM age""").fetchall()
        for c in ccc:
            print(c)
    print('Connection -> Ok')
