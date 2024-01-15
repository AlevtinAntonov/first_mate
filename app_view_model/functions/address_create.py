from tkinter import messagebox

from app_model.db.db_query import address, query_insert_into_table_return_id, DB_DICT, \
    person_address, query_insert_into
from app_view_model.functions.functions import save_access


def address_create(db, person_id, address_type_id, zipcode, region, region_type_id, district, town, town_type_id,
                   locality,
                   locality_type_id, street, street_type_id, house, house_body, house_liter, house_building, flat,
                   is_registration, is_fact, is_residence, town_district):
    try:
        with db as cur:
            # Add address to table ADDRESS
            query_add_address = query_insert_into_table_return_id(address, address) % DB_DICT[address]
            cur.execute(query_add_address,
                        (address_type_id, zipcode, region, region_type_id, district, town, town_type_id, locality,
                         locality_type_id, street, street_type_id, house, house_body, house_liter, house_building, flat,
                         is_registration, is_fact, is_residence, town_district))
            # address_id from table ADDRESS
            address_id = cur.fetchone()[0]

            # Add person_id and address_id into table PERSON_ADDRESS
            query_person_address = query_insert_into(person_address) % DB_DICT[person_address]
            cur.execute(query_person_address, (person_id, address_id))

            save_access()
    except Exception as e:
        messagebox.showinfo(title="Внимание!", message=f'Адрес не записан попробуйте еще раз!')


if __name__ == '__main__':
    pass
