from datetime import date
from tkinter import messagebox

import fdb

from app_model.db.db_connect import DB
from app_model.db.db_query import query_insert_into_table_return_id, compensation_statement, DB_DICT, \
    query_find_parental_fee_id, query_find_last_movement_id, query_insert_into, compensation_add_document, compensation
from app_view_model.functions.functions import save_access, find_id


def compensation_create(db, child_id, person_select, number_application_compensation,
                        date_application_compensation: date, date_start_compensation: date, date_end_compensation: date,
                        compensation_name,
                        add_document_name_1, add_document_data_1, add_document_name_2, add_document_data_2,
                        add_document_name_3, add_document_data_3, add_document_name_4, add_document_data_4,
                        add_document_name_5, add_document_data_5, add_document_name_6, add_document_data_6):
    try:
        compensation_id = find_id(db, compensation, DB_DICT[compensation][0], DB_DICT[compensation][1],
                                  compensation_name)
        with db as cur:
            parental_fee_id = cur.execute(query_find_parental_fee_id, (child_id,)).fetchone()[0]
            movement_id = cur.execute(query_find_last_movement_id, (child_id,)).fetchone()[0]

            query_add_comp_statement = query_insert_into_table_return_id(compensation_statement,
                                                                         compensation_statement) % DB_DICT[
                                           compensation_statement]
            cur.execute(query_add_comp_statement,
                        (number_application_compensation, date_application_compensation, date_start_compensation,
                         date_end_compensation, compensation_id, child_id, int(person_select), movement_id,
                         parental_fee_id))
            compensation_statement_id = cur.fetchone()[0]
            query_add_docs = query_insert_into(compensation_add_document) % DB_DICT[compensation_add_document]
            for i in range(1, 7):
                add_name = locals()[f'add_document_name_{i}']
                add_data = locals()[f'add_document_data_{i}']
                if add_name != '':
                    cur.execute(query_add_docs, (add_name, add_data, compensation_statement_id))

        save_access()

    except Exception as err:
        print(f'Ошибка в def compensation_create - >>> {err}')
        messagebox.showinfo(title="Внимание!", message=f'Заявление не записано. Проверьте есть ли данные о приеме и '
                                                       f'попробуйте еще раз! Ошибка {err}')



if __name__ == '__main__':
    db = DB('C:/Users/anton/PycharmProjects/first_mate/app_model/db/db/DB_PROD.FDB')
    # number_application_compensation = '13'
    # date_application_compensation = '15.01.2024'
    # compensation_id = 5
    # date_start_compensation = '16.01.2024'
    # date_end_compensation = '17.01.2024'
    # child_id = 22
    # person_select = 50
    # movement_id = 3
    # parental_fee_id = 5

    with db as cur:
        res = cur.execute("select * from compensation_statement;").fetchone()
        for i in res:
            print(i, type(i))
        # query_add_comp_statement = query_insert_into_table_return_id(compensation_statement,
        #                                                              compensation_statement) % DB_DICT[
        #                                compensation_statement]
        # cur.execute(query_add_comp_statement,
        #             (number_application_compensation, date_application_compensation, date_start_compensation,
        #              date_end_compensation, compensation_id, child_id, int(person_select), movement_id,
        #              parental_fee_id))
        # query_add_comp_statement = query_insert_into_table_return_id(compensation_statement,
        #                                                              compensation_statement) % DB_DICT[
        #                                compensation_statement]
