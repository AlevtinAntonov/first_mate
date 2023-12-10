from tkinter import ttk

from app_model.db.db_connect import db
from app_model.db.db_query import citizenship, DB_DICT, document_type
from app_model.variables import CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, CONF_D_W
from app_view_model.functions.functions import select_date, select_from_db


def document_entries(frame, row_column: tuple):
    citizenship_id = select_from_db(frame, db, citizenship, DB_DICT[citizenship][0], DB_DICT[citizenship][1], 14,
                                    row_column[1],
                                    CONF_D_W, width=15)
    document_type_id = select_from_db(frame, db, document_type, DB_DICT[document_type][0],
                                      DB_DICT[document_type][1], 16, row_column[1], CONF_D_W, width=25)
    document_series = ttk.Entry(frame)
    document_series.grid(row=row_column[0], column=row_column[1], cnf=CONF_D_W)
    document_number = ttk.Entry(frame)
    document_number.grid(row=row_column[0] + 2, column=row_column[1], cnf=CONF_D_W)
    document_issued_by = ttk.Entry(frame)
    document_issued_by.grid(row=row_column[0] + 4, column=row_column[1], cnf=CONF_D_W, columnspan=3, sticky="ew")
    document_date_of_issue = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, row_column[0] + 6,
                                         row_column[1], CONF_D_W)
    return (citizenship_id, document_type_id, document_series, document_number, document_issued_by,
            document_date_of_issue)


if __name__ == '__main__':
    pass
