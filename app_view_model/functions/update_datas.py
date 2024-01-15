from app_model.db.db_connect import db
from app_view_model.functions.functions import current_timestamp


def update_user_data(table_name, child_id, field, new_value, query):
    with db as cur:
        cur.execute(query, (child_id,))
        print(f'update_func {table_name=} {field=} {new_value=}  {child_id=}\n {query=}')
        query = f'UPDATE {table_name} SET {field} = ?'
        if table_name == 'person':
            data_id = cur.fetchone()[0]
            query += f", date_of_modify = '{current_timestamp()}'"
        elif table_name == 'gender':
            data_id = cur.fetchone()[1]
        elif table_name == 'document':
            data_id = cur.fetchone()[2]
            query += f", date_of_modify = '{current_timestamp()}'"
        elif table_name == 'address':
            data_id = cur.fetchone()[3]
        elif table_name == 'movement':
            data_id = cur.fetchone()[4]
            query += f", date_of_modify = '{current_timestamp()}'"
        elif table_name == 'parents':
            data_id = cur.fetchone()[3]
            query += f", date_of_modify = '{current_timestamp()}'"
        elif table_name == 'email':
            data_id = cur.fetchone()[4]
        elif table_name == 'phone':
            data_id = cur.fetchone()[5]
        elif table_name == 'referral':
            data_id = cur.fetchone()[2]
        elif table_name == 'benefit':
            data_id = cur.fetchone()[3]
        elif table_name == 'building':
            data_id = cur.fetchone()[4]
        elif table_name == 'team':
            data_id = cur.fetchone()[5]
        elif table_name == 'age':
            data_id = cur.fetchone()[6]
        elif table_name == 'focus':
            data_id = cur.fetchone()[7]
        elif table_name == 'mode':
            data_id = cur.fetchone()[8]
        elif table_name == 'compensation_statement':
            data_id = cur.fetchone()[1]
        elif table_name == 'compensation':
            data_id = cur.fetchone()[2]
        elif table_name == 'compensation_add_document':
            data_id = cur.fetchone()[3]

        query += f" WHERE {table_name}_id = ?;"

        print(query, new_value, data_id)
        cur.execute(query, (new_value, data_id))


query_child_compensation = """
SELECT
P.PERSON_ID,
CS.compensation_statement_id,
C.compensation_id,
CAD.add_document_id
FROM FAMILY F
JOIN PARENTS PARENTS ON F.PARENTS_ID = PARENTS.PARENTS_ID
JOIN PERSON P ON PARENTS.PERSON_ID = P.PERSON_ID
JOIN COMPENSATION_STATEMENT CS ON F.CHILD_ID = CS.CHILD_ID
JOIN COMPENSATION C ON CS.COMPENSATION_ID = C.COMPENSATION_ID
LEFT JOIN COMPENSATION_ADD_DOCUMENT CAD ON CS.COMPENSATION_STATEMENT_ID = CAD.COMPENSATION_STATEMENT_ID
WHERE F.CHILD_ID = ?;
"""
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

query_child_referral = (f'SELECT person.person_id, gender.gender_id, referral.referral_id, benefit.benefit_id, '
                        f'building.building_id,  TEAM.TEAM_ID, age.age_id, focus.focus_id, mode.mode_id '
                        f'FROM CHILD '
                        f'JOIN REFERRAL ON CHILD.CHILD_ID = REFERRAL.CHILD_ID '
                        f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                        f'JOIN TEAM ON CHILD.TEAM_ID = TEAM.TEAM_ID '
                        f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
                        f'JOIN BUILDING ON REFERRAL.BUILDING_ID = BUILDING.BUILDING_ID '
                        f'JOIN AGE ON REFERRAL.AGE_ID = AGE.AGE_ID '
                        f'JOIN FOCUS ON REFERRAL.FOCUS_ID = FOCUS.FOCUS_ID '
                        f'JOIN MODE ON REFERRAL.MODE_ID = MODE.MODE_ID '
                        f'JOIN BENEFIT ON REFERRAL.BENEFIT_ID = BENEFIT.BENEFIT_ID '
                        f'WHERE CHILD.CHILD_ID = ?;')

query_tab_parent_document = (f'SELECT person.person_id, gender.gender_id, document.document_id, parents.parents_id, '
                             f' email.email_id, phone.phone_id FROM PARENTS '
                             f'JOIN PERSON ON PARENTS.PERSON_ID = PERSON.PERSON_ID '
                             f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                             f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
                             f'JOIN CITIZENSHIP ON PERSON.CITIZENSHIP_ID = CITIZENSHIP.CITIZENSHIP_ID '
                             f'JOIN DOCUMENT_TYPE ON DOCUMENT.DOCUMENT_TYPE_ID = DOCUMENT_TYPE.DOCUMENT_TYPE_ID '
                             f'join email on parents.parents_id = email.parents_id '
                             f'join phone on parents.parents_id = phone.parents_id '
                             f'join status on parents.status_id = status.status_id '
                             f'WHERE PERSON.PERSON_ID = ?;')

query_parents_doc_move_reg_adr = (f'SELECT person.person_id, gender.gender_id, document.document_id, '
                                  f' address.address_id '
                                  f'FROM parents '
                                  f'JOIN PERSON on parents.PERSON_ID = person.person_id '
                                  f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                                  f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
                                  f'join person_address on person.person_id = person_address.person_id '
                                  f'join address on person_address.address_id = address.address_id '
                                  f'WHERE PERSON.PERSON_ID = ? and (address.address_type_id = 1 OR '
                                  f'address.is_registration = true);')

query_date_entry_child = (f'FROM CHILD '
                          f' JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                          f' JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                          f' WHERE CHILD.CHILD_ID = ?;')

query_date_entry_parents = (f'FROM PARENTS '
                            f'JOIN PERSON ON PARENTS.PERSON_ID = PERSON.PERSON_ID '
                            f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                            f'WHERE PERSON.PERSON_ID = ?;')

query_date_entry_movement = (f'FROM CHILD '
                             f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                             f'JOIN TEAM ON CHILD.TEAM_ID = TEAM.TEAM_ID '
                             f'JOIN MOVEMENT ON CHILD.CHILD_ID = MOVEMENT.CHILD_ID '
                             f'WHERE CHILD.CHILD_ID = ?;')

query_date_entry_compensation = """
FROM FAMILY 
JOIN PARENTS ON FAMILY.PARENTS_ID = PARENTS.PARENTS_ID
JOIN PERSON  ON PARENTS.PERSON_ID = PERSON.PERSON_ID
JOIN COMPENSATION_STATEMENT  ON FAMILY.CHILD_ID = COMPENSATION_STATEMENT.CHILD_ID
JOIN COMPENSATION  ON COMPENSATION_STATEMENT.COMPENSATION_ID = COMPENSATION.COMPENSATION_ID
LEFT JOIN COMPENSATION_ADD_DOCUMENT ON COMPENSATION_STATEMENT.COMPENSATION_STATEMENT_ID = COMPENSATION_ADD_DOCUMENT.COMPENSATION_STATEMENT_ID
WHERE FAMILY.CHILD_ID = ?;
"""

query_date_entry_compensation = """
 FROM FAMILY F
JOIN PARENTS PARENTS ON F.PARENTS_ID = PARENTS.PARENTS_ID
JOIN PERSON P ON PARENTS.PERSON_ID = P.PERSON_ID
JOIN COMPENSATION_STATEMENT CS ON F.CHILD_ID = CS.CHILD_ID
JOIN COMPENSATION C ON CS.COMPENSATION_ID = C.COMPENSATION_ID
LEFT JOIN COMPENSATION_ADD_DOCUMENT CAD ON CS.COMPENSATION_STATEMENT_ID = CAD.COMPENSATION_STATEMENT_ID
"""
query_date_entry_referral = ("""
FROM CHILD 
JOIN REFERRAL ON CHILD.CHILD_ID = REFERRAL.CHILD_ID
JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID
JOIN TEAM ON REFERRAL.TEAM_ID = TEAM.TEAM_ID
JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
JOIN BUILDING ON REFERRAL.BUILDING_ID = BUILDING.BUILDING_ID
JOIN AGE ON REFERRAL.AGE_ID = AGE.AGE_ID
JOIN FOCUS ON REFERRAL.FOCUS_ID = FOCUS.FOCUS_ID
JOIN MODE ON REFERRAL.MODE_ID = MODE.MODE_ID
JOIN BENEFIT ON REFERRAL.BENEFIT_ID = BENEFIT.BENEFIT_ID 
WHERE CHILD.CHILD_ID = ?;""")

query_read_birth_certificate = """
SELECT 
    PERSON.LAST_NAME, 
    PERSON.FIRST_NAME, 
    PERSON.PATRONYMIC, 
    GENDER.GENDER_NAME,
    PERSON.DATE_OF_BIRTH,
    CITIZENSHIP.CITIZENSHIP_SHORT_NAME,
    DOCUMENT_TYPE.DOCUMENT_TYPE_NAME,
    DOCUMENT.PLACE_OF_BIRTH,
    DOCUMENT.DOCUMENT_ASSEMBLY_RECORD,
    DOCUMENT.DOCUMENT_SERIES, 
    DOCUMENT.DOCUMENT_NUMBER, 
    DOCUMENT.DOCUMENT_ISSUED_BY, 
    DOCUMENT.DOCUMENT_DATE_OF_ISSUE,
    PERSON.SNIILS
FROM CHILD
    JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID
    JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID
    JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
    JOIN CITIZENSHIP ON PERSON.CITIZENSHIP_ID = CITIZENSHIP.CITIZENSHIP_ID
    JOIN DOCUMENT_TYPE ON DOCUMENT.DOCUMENT_TYPE_ID = DOCUMENT_TYPE.DOCUMENT_TYPE_ID
WHERE CHILD.CHILD_ID = ?;
"""

query_read_address = """
SELECT 
    ADDRESS_TYPE.ADDRESS_TYPE_NAME,
    ADDRESS.ZIPCODE,
    REGION_TYPE.REGION_TYPE_NAME,
    ADDRESS.REGION,
    ADDRESS.DISTRICT,
    TOWN_TYPE.TOWN_TYPE_NAME,
    ADDRESS.TOWN,
    LOCALITY_TYPE.LOCALITY_TYPE_NAME,
    ADDRESS.LOCALITY,
    STREET_TYPE.STREET_TYPE_NAME,
    ADDRESS.STREET,
    ADDRESS.HOUSE,
    ADDRESS.HOUSE_BODY,
    ADDRESS.HOUSE_LITER,
    ADDRESS.HOUSE_BUILDING,
    ADDRESS.FLAT,
    TOWN_DISTRICT.TOWN_DISTRICT_NAME,
    ADDRESS.IS_REGISTRATION,
    ADDRESS.IS_FACT,
    ADDRESS.IS_RESIDENCE
FROM CHILD
    JOIN FAMILY ON CHILD.CHILD_ID = FAMILY.CHILD_ID
    JOIN PARENTS ON FAMILY.PARENTS_ID = PARENTS.PARENTS_ID
    JOIN PERSON ON PARENTS.PERSON_ID = PERSON.PERSON_ID
    JOIN PERSON_ADDRESS ON PERSON.PERSON_ID = PERSON_ADDRESS.PERSON_ID
    join address on PERSON_ADDRESS.ADDRESS_ID = address.address_id
    join address_type on address.address_type_id = address_type.address_type_id
    join region_type on address.region_type_id = region_type.region_type_id
     join town_type on address.town_type_id = town_type.town_type_id
    join street_type on address.street_type_id = street_type.street_type_id
    join locality_type on address.locality_type_id = locality_type.locality_type_id
    join town_district on address.town_district_id = town_district.town_district_id 
    """
query_read_address_reg = query_read_address + (f'WHERE CHILD.CHILD_ID = ? and (address.address_type_id = 1 '
                                               f'OR address.is_registration = true) ;')
query_read_address_fact = query_read_address + (f'WHERE CHILD.CHILD_ID = ? and (address.address_type_id = 2 '
                                                f'OR address.IS_FACT = true);')
query_read_address_res = query_read_address + (f'WHERE CHILD.CHILD_ID = ? and (address.address_type_id = 3 '
                                               f'OR address.IS_RESIDENCE = true);')
query_read_parent_document = """
SELECT 
    STATUS.STATUS_NAME,
    PERSON.LAST_NAME, 
    PERSON.FIRST_NAME, 
    PERSON.PATRONYMIC, 
    GENDER.GENDER_NAME,
    PERSON.DATE_OF_BIRTH,
    CITIZENSHIP.CITIZENSHIP_SHORT_NAME,
    DOCUMENT_TYPE.DOCUMENT_TYPE_NAME,
    DOCUMENT.DOCUMENT_SERIES,
    DOCUMENT.DOCUMENT_NUMBER, 
    DOCUMENT.DOCUMENT_ISSUED_BY, 
    DOCUMENT.DOCUMENT_DATE_OF_ISSUE,
    DOCUMENT.DOCUMENT_DATE_OF_EXPIRE,
    PHONE.PHONE_NUMBER,
    EMAIL.EMAIL_NAME,
    PERSON.SNIILS,
    PARENTS.SVO_PARTICIPANT
FROM PARENTS
    JOIN PERSON ON PARENTS.PERSON_ID = PERSON.PERSON_ID
    JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID
    JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
    JOIN CITIZENSHIP ON PERSON.CITIZENSHIP_ID = CITIZENSHIP.CITIZENSHIP_ID
    JOIN DOCUMENT_TYPE ON DOCUMENT.DOCUMENT_TYPE_ID = DOCUMENT_TYPE.DOCUMENT_TYPE_ID
    JOIN EMAIL ON PARENTS.PARENTS_ID = EMAIL.PARENTS_ID
    JOIN PHONE ON PARENTS.PARENTS_ID = PHONE.PARENTS_ID
    JOIN STATUS ON PARENTS.STATUS_ID = STATUS.STATUS_ID
WHERE PERSON.PERSON_ID = ?;
"""

query_read_parent_address = """
SELECT
    ADDRESS_TYPE.ADDRESS_TYPE_NAME,
    ADDRESS.ZIPCODE,
    REGION_TYPE.REGION_TYPE_NAME,
    ADDRESS.REGION,
    ADDRESS.DISTRICT,
    TOWN_TYPE.TOWN_TYPE_NAME,
    ADDRESS.TOWN,
    LOCALITY_TYPE.LOCALITY_TYPE_NAME,
    ADDRESS.LOCALITY,
    STREET_TYPE.STREET_TYPE_NAME,
    ADDRESS.STREET,
    ADDRESS.HOUSE,
    ADDRESS.HOUSE_BODY,
    ADDRESS.HOUSE_LITER,
    ADDRESS.HOUSE_BUILDING,
    ADDRESS.FLAT,
    TOWN_DISTRICT.TOWN_DISTRICT_NAME,
    ADDRESS.IS_REGISTRATION,
    ADDRESS.IS_FACT,
    ADDRESS.IS_RESIDENCE
FROM PARENTS
    JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID
    JOIN FAMILY ON CHILD.CHILD_ID = FAMILY.CHILD_ID
    JOIN PARENTS ON FAMILY.PARENTS_ID = PARENTS.PARENTS_ID
    JOIN PERSON ON PARENTS.PERSON_ID = PERSON.PERSON_ID
    JOIN PERSON_ADDRESS ON PERSON.PERSON_ID = PERSON_ADDRESS.PERSON_ID
    JOIN ADDRESS ON PERSON_ADDRESS.ADDRESS_ID = ADDRESS.ADDRESS_ID
    JOIN ADDRESS_TYPE ON ADDRESS.ADDRESS_TYPE_ID = ADDRESS_TYPE.ADDRESS_TYPE_ID
    JOIN REGION_TYPE ON ADDRESS.REGION_TYPE_ID = REGION_TYPE.REGION_TYPE_ID
    JOIN TOWN_TYPE ON ADDRESS.TOWN_TYPE_ID = TOWN_TYPE.TOWN_TYPE_ID
    JOIN STREET_TYPE ON ADDRESS.STREET_TYPE_ID = STREET_TYPE.STREET_TYPE_ID
    JOIN LOCALITY_TYPE ON ADDRESS.LOCALITY_TYPE_ID = LOCALITY_TYPE.LOCALITY_TYPE_ID
    JOIN TOWN_DISTRICT ON ADDRESS.TOWN_DISTRICT_ID = TOWN_DISTRICT.TOWN_DISTRICT_ID  
    """
query_read_parent_address_reg = query_read_address + (f'WHERE person.person_id = ? and (address.address_type_id = 1 '
                                                      f'OR address.is_registration = true) order by  PERSON.LAST_NAME, '
                                                      f'PERSON.FIRST_NAME, PERSON.PATRONYMIC;')
query_read_parent_address_fact = query_read_address + (f'WHERE person.person_id and (address.address_type_id = 2 '
                                                       f'OR address.IS_FACT = true) order by  PERSON.LAST_NAME, '
                                                       f'PERSON.FIRST_NAME, PERSON.PATRONYMIC;')
query_read_parent_address_res = query_read_address + (f'WHERE person.person_id = ? and (address.address_type_id = 3 '
                                                      f'OR address.IS_RESIDENCE = true) order by  PERSON.LAST_NAME, '
                                                      f'PERSON.FIRST_NAME, PERSON.PATRONYMIC;')

query_read_movement = """
SELECT 
    PERSON.LAST_NAME || ' ' || PERSON.FIRST_NAME || ' ' ||   PERSON.PATRONYMIC AS FULL_NAME,
    TEAM.TEAM_NAME,
    MOVEMENT.STATEMENT_NUMBER,
    MOVEMENT.STATEMENT_DATE,
    MOVEMENT.DATE_OF_JOINING_TEAM,
    MOVEMENT.CONTRACT_NUMBER,
    MOVEMENT.CONTRACT_DATE,
    MOVEMENT.CONTRACT_BEGIN_DATE,
    MOVEMENT.ORDER_OF_ADMISSION_NUMBER,
    MOVEMENT.ORDER_OF_ADMISSION_DATE,
    MOVEMENT.ORDER_OF_EXPULSION_NUMBER,
    MOVEMENT.ORDER_OF_EXPULSION_DATE
FROM CHILD
    JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID
    JOIN TEAM ON CHILD.TEAM_ID = TEAM.TEAM_ID
    JOIN MOVEMENT ON CHILD.CHILD_ID = MOVEMENT.CHILD_ID
WHERE CHILD.CHILD_ID = ?;
"""

query_read_referral = """
SELECT
    REFERRAL.REFERRAL_NUMBER,
    REFERRAL.REFERRAL_DATE,
    PERSON.LAST_NAME,
    PERSON.FIRST_NAME,
    PERSON.PATRONYMIC,
    GENDER.GENDER_NAME,
    PERSON.DATE_OF_BIRTH,
    BUILDING.BUILDING_NAME,
    AGE.AGE_NAME,
    FOCUS.FOCUS_NAME,
    MODE.MODE_NAME,
    REFERRAL.REFERRAL_BEGIN_DATE,
    BENEFIT.BENEFIT_NAME,
    TEAM.TEAM_NAME,
    REFERRAL.REFERRAL_COMMENT
FROM CHILD
JOIN REFERRAL ON CHILD.CHILD_ID = REFERRAL.CHILD_ID
JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID
JOIN TEAM ON REFERRAL.TEAM_ID = TEAM.TEAM_ID
JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID
JOIN BUILDING ON REFERRAL.BUILDING_ID = BUILDING.BUILDING_ID
JOIN AGE ON REFERRAL.AGE_ID = AGE.AGE_ID
JOIN FOCUS ON REFERRAL.FOCUS_ID = FOCUS.FOCUS_ID
JOIN MODE ON REFERRAL.MODE_ID = MODE.MODE_ID
JOIN BENEFIT ON REFERRAL.BENEFIT_ID = BENEFIT.BENEFIT_ID
WHERE CHILD.CHILD_ID = ?;
"""

query_read_compensation = """
SELECT
    P.LAST_NAME || ' ' || P.FIRST_NAME || ' ' || P.PATRONYMIC AS FULL_NAME,
    CS.compensation_statement_number,
    CS.compensation_statement_date,
    C.compensation_short_basis,
    CS.compensation_statement_start_date,
    CS.compensation_statement_end_date,
    CAD.add_document_name,
    CAD.add_document_data
FROM FAMILY F
JOIN PARENTS PARENTS ON F.PARENTS_ID = PARENTS.PARENTS_ID
JOIN PERSON P ON PARENTS.PERSON_ID = P.PERSON_ID
JOIN COMPENSATION_STATEMENT CS ON F.CHILD_ID = CS.CHILD_ID
JOIN COMPENSATION C ON CS.COMPENSATION_ID = C.COMPENSATION_ID
LEFT JOIN COMPENSATION_ADD_DOCUMENT CAD ON CS.COMPENSATION_STATEMENT_ID = CAD.COMPENSATION_STATEMENT_ID
WHERE F.CHILD_ID =  ?;
"""
