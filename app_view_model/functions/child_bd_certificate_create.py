from datetime import date
from tkinter import messagebox

from app_model.db.db_query import query_insert_into_table_return_id, document, DB_DICT, document_type, citizenship, \
    query_child_person_id, query_update_child_person
from app_view_model.functions.functions import current_timestamp, find_id, check_if_exists, save_access


def child_db_cert_create(db, child_id: int, citizenship_id, sniils: str, document_type_id: int, place_of_birth: str,
                         document_series: str, document_number: str, document_issued_by: str,
                         document_date_of_issue: date, document_assembly_record: str):
    document_type_id = find_id(db, document_type, DB_DICT[document_type][0], DB_DICT[document_type][1],
                               document_type_id)
    citizenship_id = find_id(db, citizenship, DB_DICT[citizenship][0], DB_DICT[citizenship][1], citizenship_id)

    if not check_if_exists(db, document, document_series, document_number, document_date_of_issue,
                           document_type_id):
        with db as cur:
            document_date_of_expire = None

            # Add document of child to table DOCUMENT and return document_id for table PERSON
            query_add_doc = query_insert_into_table_return_id(document, document) % DB_DICT[document]
            cur.execute(query_add_doc, (document_series, document_number, document_issued_by, document_date_of_issue,
                                        document_date_of_expire, document_type_id, place_of_birth, current_timestamp(),
                                        document_assembly_record))
            # document_id from table DOCUMENT
            document_id = cur.fetchone()[0]

            # Update CHILD fields: document_id, sniils, citizenship_id into table PERSON
            cur.execute(query_child_person_id, (child_id,))
            person_id = cur.fetchone()[0]

            query_update_child = query_update_child_person % (
                'person', 'document_id', 'sniils', 'citizenship_id', 'date_of_modify', 'person_id')
            cur.execute(query_update_child, (document_id, sniils, citizenship_id, current_timestamp(), person_id))
            save_access()

    else:
        messagebox.showinfo(title="Внимание!",
                            message=f'Документ серия: {document_series} номер: {document_number} ,'
                                    f'дата выдачи:  {document_date_of_issue} - уже существует в базе!')


if __name__ == '__main__':
    pass
