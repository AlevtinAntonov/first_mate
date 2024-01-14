# variable - table name = string 'table name'
referral, person, child, parents, building, age = 'referral', 'person', 'child', 'parents', 'building', 'age'
focus, mode, benefit, team, gender = 'focus', 'mode', 'benefit', 'team', 'gender'
document, address, address_type = 'document', 'address', 'address_type'
citizenship, document_type, status = 'citizenship', 'document_type', 'status'
person_parent, family, phone, email = 'person_parent', 'family', 'phone', 'email'
region_type, town_type, locality_type, street_type = 'region_type', 'town_type', 'locality_type', 'street_type'
person_address, organization, compensation = 'person_address', 'organization', 'compensation'
compensation_statement, compensation_add_document = 'compensation_statement', 'compensation_add_document'
movement, town_district = 'movement', 'town_district'

# dictionary key: table name, vaulue : fields names
DB_DICT = {
    'referral': (
        'referral_number', 'referral_date', 'referral_begin_date', 'referral_comment', 'child_id', 'mode_id',
        'building_id', 'team_id', 'age_id', 'focus_id', 'benefit_id'),
    'person': ('last_name', 'first_name', 'patronymic', 'date_of_birth', 'gender_id', 'date_of_add'),
    'person_parent': ('last_name', 'first_name', 'patronymic', 'date_of_birth', 'gender_id', 'citizenship_id',
                      'document_id', 'sniils', 'date_of_add'),

    'child': ('person_id', 'date_of_add'),
    'parents': ('person_id', 'status_id', 'date_of_add'),
    'family': ('child_id', 'parents_id'),
    'phone': ('phone_number', 'parents_id'),
    'email': ('email_name', 'parents_id'),
    'building': ('building_id', 'building_name'),
    'age': ('age_id', 'age_name'),
    'focus': ('focus_id', 'focus_name'),
    'mode': ('mode_id', 'mode_name'),
    'benefit': ('benefit_id', 'benefit_name'),
    'team': ('team_id', 'team_name'),
    'gender': ('gender_id', 'gender_name'),
    'citizenship': ('citizenship_id', 'citizenship_short_name'),
    'status': ('status_id', 'status_name'),
    'document_type': ('document_type_id', 'document_type_name'),
    'document': ('document_series', 'document_number', 'document_issued_by', 'document_date_of_issue',
                 'document_date_of_expire', 'document_type_id', "place_of_birth", 'date_of_add',
                 'document_assembly_record'),
    'address': ('address_type_id', 'zipcode', 'region', 'region_type_id', 'district', 'town', 'town_type_id',
                'locality', 'locality_type_id', 'street', 'street_type_id', 'house', 'house_body', 'house_liter',
                'house_building', 'flat', 'is_registration', 'is_fact', 'is_residence', 'town_district'),
    'address_type': ('address_type_id', 'address_type_name'),
    'region_type': ('region_type_id', 'region_type_name'),
    'town_type': ('town_type_id', 'town_type_name'),
    'town_district': ('town_district_id', 'town_district_name'),
    'locality_type': ('locality_type_id', 'locality_type_name'),
    'street_type': ('street_type_id', 'street_type_name'),
    'person_address': ('person_id', 'address_id'),
    'compensation': ('compensation_id', 'compensation_short_basis'),
    'organization': (
        'full_name', 'short_name', 'legal_address', 'post_address', 'phone', 'email', 'okpo', 'ogrn', 'okogu', 'inn',
        'kpp', 'position_name', 'boss_last_name', 'boss_first_name', 'boss_patronymic', 'beneficiary', 'bank_name',
        'bic', 'cor_account', 'account'),
    'compensation_statement': ('compensation_statement_number', 'compensation_statement_date',
                               'compensation_statement_start_date', 'compensation_statement_end_date',
                               'compensation_id', 'child_id', 'person_id', 'movement_id', 'parental_fee_id'),
    'compensation_add_document': ('add_document_name', 'add_document_data', 'compensation_statement_id'),
    'movement': ('statement_number', 'statement_date', 'date_of_joining_team', 'contract_number', 'contract_date',
                 'contract_begin_date', 'order_of_admission_number', 'order_of_admission_date',
                 'date_of_add', 'child_id', 'referral_id', 'team_id', 'person_id'),
}

# compensation_statement_number, compensation_statement_date, compensation_statement_start_date, compensation_statement_end_date, compensation_id, child_id, person_id, movement_id, parental_fee_id
# queries
query_find_person = """ SELECT * FROM person WHERE (last_name = ? AND first_name = ? AND (patronymic = ? OR patronymic 
IS NULL) AND date_of_birth = ?);"""
query_check_person = """SELECT * FROM %s WHERE (last_name = ? AND first_name = ? AND (patronymic = ? OR patronymic 
IS NULL) AND date_of_birth = ?);"""
query_find_id = """SELECT * FROM %s WHERE (person_id = ?);"""

query_check_document = """SELECT * FROM %s WHERE (document_series = ? AND document_number = ? AND 
document_date_of_issue = ? AND document_type_id = ?) ;"""

query_login = "SELECT user_name, user_password FROM users WHERE (user_name = ? AND user_password = ? AND " \
              "is_visible)"
query_child_person_id = """SELECT person_id FROM child WHERE (child_id = ?) ;"""
# query_update_child_person = """UPDATE person SET (document_id = ?, sniils = ?) WHERE (person_id = ?) ;"""
query_update_child_person = "UPDATE %s SET %s=?, %s=?, %s=?, %s=? WHERE (%s=?); "

query_full_addresses = """SELECT 
    a.zipcode, 
    a.region, 
    rt.region_type_name_short, 
    a.district, 
    a.town, 
    tt.town_type_name_short, 
    a.locality, 
    lt.locality_type_name_short, 
    a.street, 
    st.street_type_name_short, 
    a.house, 
    a.house_body, 
    a.house_liter, 
    a.house_building, 
    a.flat
FROM 
    person_address pa
JOIN 
    address a ON pa.address_id = a.address_id
JOIN 
    address_type ad ON a.address_type_id = ad.address_type_id
JOIN 
    region_type rt ON a.region_type_id = rt.region_type_id
JOIN 
    town_type tt ON a.town_type_id = tt.town_type_id
JOIN 
    locality_type lt ON a.locality_type_id = lt.locality_type_id
JOIN 
    street_type st ON a.street_type_id = st.street_type_id
WHERE 
    pa.person_id = ?
    AND pa.is_visible = True
    AND a.%s  = True;
"""

query_find_last_movement_id = """
SELECT MAX(movement_id)
FROM movement 
WHERE child_id = ? 
AND IS_VISIBLE = True;
"""


def query_insert_into(table_name):
    fields = ', '.join(('%s',) * (len(DB_DICT[table_name])))
    val = ', '.join(('?',) * (len(DB_DICT[table_name])))
    return f'INSERT INTO {table_name} ({fields}) VALUES ( {val}) ;'


def query_insert_into_table_return_id(table_name, fields_name):
    fields = ', '.join(('%s',) * (len(DB_DICT[fields_name])))
    val = ', '.join(('?',) * (len(DB_DICT[fields_name])))
    name_id = '_'.join((table_name, 'id'))
    return f'INSERT INTO {table_name} ({fields}) VALUES ( {val}) RETURNING {name_id} ;'


def get_total_table_records(db, table_name):
    query = f"SELECT count(*) FROM {table_name}"
    with db as cur:
        cur.execute(query)
        result = cur.fetchone()
        return result[0] if result else 0


if __name__ == '__main__':
    # pass
    query = query_insert_into(compensation_add_document) % DB_DICT[compensation_add_document]
    print(query)
