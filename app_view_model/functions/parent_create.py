from datetime import date
from tkinter import messagebox

from app_model.db.db_query import parents, DB_DICT, document, gender, citizenship, \
    query_insert_into_table_return_id, person, person_parent, family, phone, email, document_type, status
from app_view_model.functions.functions import current_timestamp, check_if_exists, find_id, capitalize_double_surname, \
    save_access


#  Add new parent to database
def parent_create(db, child_select: int, status_id: int, last_name: str, first_name: str, patronymic: str,
                  gender_id, date_of_birth, citizenship_id, document_type_id: int, document_series: str,
                  document_number: str, document_issued_by: str, document_date_of_issue: date,
                  document_date_of_expire: date, phone_number: str, email_name: str, sniils: str):
    last_name = capitalize_double_surname(last_name)
    first_name = capitalize_double_surname(first_name)
    patronymic = capitalize_double_surname(patronymic)
    document_type_id = find_id(db, document_type, DB_DICT[document_type][0], DB_DICT[document_type][1],
                               document_type_id)
    gender_id = find_id(db, gender, DB_DICT[gender][0], DB_DICT[gender][1], gender_id)
    citizenship_id = find_id(db, citizenship, DB_DICT[citizenship][0], DB_DICT[citizenship][1], citizenship_id)
    status_id = find_id(db, status, DB_DICT[status][0], DB_DICT[status][1], status_id)

    #  If person not exists create new records in tables: PERSON, PARENTS, DOCUMENT, FAMILY
    if not check_if_exists(db, person, last_name, first_name, patronymic, date_of_birth):
        with db as cur:
            document_assembly_record = None
            place_of_birth = None

            # Add document of parent to table DOCUMENT and return document_id for table PERSON
            query_add_doc = query_insert_into_table_return_id(document, document) % DB_DICT[document]
            cur.execute(query_add_doc, (document_series, document_number, document_issued_by, document_date_of_issue,
                                        document_date_of_expire, document_type_id, place_of_birth, current_timestamp(),
                                        document_assembly_record))

            # document_id from table DOCUMENT
            document_id = cur.fetchone()[0]

            # Add new parent into table PERSON
            query = query_insert_into_table_return_id(person, person_parent) % DB_DICT[person_parent]
            cur.execute(query,
                        (last_name, first_name, patronymic, date_of_birth, gender_id, citizenship_id, document_id,
                         sniils, current_timestamp()))
            person_id = cur.fetchone()[0]

            # Add new person_id into table PARENTS
            query_add_parent_id = query_insert_into_table_return_id(parents, parents) % DB_DICT[parents]
            cur.execute(query_add_parent_id, (person_id, status_id, current_timestamp()))
            parents_id = cur.fetchone()[0]

            # Add child and parent into table FAMILY
            query_add_family = query_insert_into_table_return_id(family, family) % DB_DICT[family]
            cur.execute(query_add_family, (child_select, parents_id))

            # Add phone into table PHONE
            query_add_phone = query_insert_into_table_return_id(phone, phone) % DB_DICT[phone]
            cur.execute(query_add_phone, (phone_number, parents_id))

            # Add phone into table EMAIL
            query_add_email = query_insert_into_table_return_id(email, email) % DB_DICT[email]
            cur.execute(query_add_email, (email_name, parents_id))
            save_access()

    else:
        messagebox.showinfo(title="Внимание!", message=f'Родитель(представитель): {last_name} {first_name} {patronymic},'
                                                       f' {date_of_birth} г.р. - уже существует в базе!')


if __name__ == '__main__':
    pass
