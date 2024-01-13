from app_model.db.db_connect import db
from app_view_model.functions.functions import current_timestamp

query_tab_birth_certificate = (f'SELECT person.person_id, gender.gender_id, document.document_id FROM CHILD '
                               f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                               f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                               f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
                               f'WHERE CHILD.CHILD_ID = ?;')

query_child_doc_move_reg_adr = (f'SELECT person.person_id, gender.gender_id, document.document_id, '
                                f'address.address_id,  movement.movement_id FROM CHILD '
                                f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                                f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                                f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
                                f'join person_address on person.person_id = person_address.person_id '
                                f'join address on person_address.address_id = address.address_id '
                                f'join movement on child.child_id = movement.child_id '
                                f'WHERE CHILD.CHILD_ID = ? and (address.address_type_id = 1 OR '
                                f'address.is_registration = true);')

query_date_entry_child = (f'FROM CHILD '
                          f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                          f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                          f'WHERE CHILD.CHILD_ID = ?;')


def update_user_data(table_name, child_id, field, new_value, query):
    with db as cur:
        cur.execute(query, (child_id,))
        query = f'UPDATE {table_name} SET {field} = ?'
        if table_name == 'person':
            data_id = cur.fetchone()[0]
            query += f", date_of_modify = '{current_timestamp()}'"
        elif table_name == 'document':
            data_id = cur.fetchone()[2]
            query += f", date_of_modify = '{current_timestamp()}'"
        elif table_name == 'gender':
            data_id = cur.fetchone()[1]
        query += f" WHERE {table_name}_id = ?;"
        print(query, new_value, data_id)
        cur.execute(query, (new_value, data_id))
