REFERRAL_SAVE = 'referral', 'referral_number', 'referral_date', 'referral_begin_date', 'referral_comment', 'child_id', \
    'mode_id', 'building_id', 'team_id', 'age_id', 'focus_id', 'benefit_id'
CHECK_PERSON_CHILD = 'child', 'last_name', 'first_name', 'patronymic', 'date_of_birth', 'gender_id', 'date_of_add'
CHECK_PARENT = 'parents', 'last_name', 'first_name', 'patronymic', 'date_of_birth', 'gender_id', 'date_of_add'
referral, person, child, parents, building, age = 'referral', 'person', 'child', 'parents', 'building', 'age'
focus, mode, benefit, team, gender = 'focus', 'mode', 'benefit', 'team', 'gender'
document, address, address_type = 'document', 'address', 'address_type'
citizenship, document_type, status = 'citizenship', 'document_type', 'status'

DB_DICT = {
    'referral': (
        'referral_number', 'referral_date', 'referral_begin_date', 'referral_comment', 'child_id', 'mode_id',
        'building_id', 'team_id', 'age_id', 'focus_id', 'benefit_id'),
    'person': ('last_name', 'first_name', 'patronymic', 'date_of_birth', 'gender_id', 'date_of_add'),
    'child': ('person_id', 'date_of_add'),
    'parents': ('parents_id', 'person_id', 'date_of_add'),
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
                 'document_date_of_expire', 'document_type_id', 'date_of_add'),
    'address': ('address_type_id', 'zipcode', 'region', 'region_type_id', 'district', 'town', 'town_type_id',
                'locality', 'locality_type_id', 'street', 'street_type_id', 'house', 'house_body', 'house_liter',
                'house_building', 'flat', 'is_registration', 'is_fact', 'is_residence'),
    'address_type': ('address_type_id', 'address_type_name'),
}
# registration_address = registration_address_entry.get()
# residence_address = residence_address_entry.get()
# fact_address
query_find_person = """ SELECT * FROM person WHERE (last_name = ? AND first_name = ? AND (patronymic = ? OR patronymic 
IS NULL) AND date_of_birth = ?);"""
query_check_person = """SELECT * FROM %s WHERE (last_name = ? AND first_name = ? AND (patronymic = ? OR patronymic 
IS NULL) AND date_of_birth = ?);"""
query_find_id = """SELECT * FROM %s WHERE (person_id = ?);"""

query_check_document = """SELECT * FROM %s WHERE (document_series = ? AND document_number = ? AND 
document_date_of_issue = ? AND document_type_id = ?) ;"""

query_login = "SELECT user_name, user_password FROM users WHERE (user_name = ? AND user_password = ? AND " \
              "is_visible)"


# CHECK_ID_DICT = {
# 'building': ('building_id', 'building_name'),
# 'age': ('age_id', 'age_name'),
# 'focus': ('focus_id', 'focus_name'),
# 'mode': ('mode_id', 'mode_name'),
# 'benefit': ('benefit_id', 'benefit_name'),
# 'team': ('team_id', 'team_name'),

# }


def query_insert_into(table_name):
    fields = ', '.join(('%s',) * (len(DB_DICT[table_name])))
    val = ', '.join(('?',) * (len(DB_DICT[table_name])))
    return f'INSERT INTO {table_name} ({fields}) VALUES ( {val});'


def query_insert_into_person(table_name):
    fields = ', '.join(('%s',) * (len(DB_DICT[table_name])))
    val = ', '.join(('?',) * (len(DB_DICT[table_name])))
    name_id = '_'.join((table_name, 'id'))
    return f'INSERT INTO {table_name} ({fields}) VALUES ( {val}) RETURNING {name_id} ;'


# tbl_name = 'child'
# print(len(CHECK_PERSON_CHILD))
# print(CHECK_PERSON_CHILD)
# print(DB_DICT[child])
# print(query_insert_into(child))
# print(DB_DICT['team'])
if __name__ == '__main__':
    # print(query_insert_into(parents))
    tbl_name = {'address_type_id': 1, 'zipcode': 'eee', 'region': '', 'region_type_id': 0, 'district': 'eee',
                'town': 'eeee', 'town_type_id': 1, 'locality': '', 'locality_type_id': 0, 'street': 'fff',
                'street_type_id': 1, 'house': '56', 'house_body': '1', 'house_liter': 'F', 'house_building': '',
                'flat': '55', 'is_registration': True, 'is_fact': True, 'is_residence': False}

    for v in tbl_name.values():
        print(v, type(v))
    print(tbl_name['house'])
