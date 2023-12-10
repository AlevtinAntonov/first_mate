from datetime import date
from tkinter import messagebox

from app_model.db.db_query import address, query_insert_into_table_return_id, DB_DICT, address_type, region_type, \
    town_type, locality_type, street_type, person_address, query_insert_into
from app_view_model.functions.functions import find_id, save_access


def address_create(db, person_id, address_type_id, zipcode, region, region_type_id, district, town, town_type_id, locality,
                   locality_type_id, street, street_type_id, house, house_body, house_liter, house_building, flat,
                   is_registration, is_fact, is_residence):
    # address_type_id = find_id(db, address_type, DB_DICT[address_type][0], DB_DICT[address_type][1], address_type_id)
    # region_type_id = find_id(db, region_type, DB_DICT[region_type][0], DB_DICT[region_type][1], region_type_id)
    # town_type_id = find_id(db, town_type, DB_DICT[town_type][0], DB_DICT[town_type][1], town_type_id)
    # locality_type_id = find_id(db, locality_type, DB_DICT[locality_type][0], DB_DICT[locality_type][1],
    #                            locality_type_id)
    # street_type_id = find_id(db, street_type, DB_DICT[street_type][0], DB_DICT[street_type][1], street_type_id)
    try:
        with db as cur:
            # Add address to table ADDRESS
            query_add_address = query_insert_into_table_return_id(address, address) % DB_DICT[address]
            cur.execute(query_add_address,
                        (address_type_id, zipcode, region, region_type_id, district, town, town_type_id, locality,
                         locality_type_id, street, street_type_id, house, house_body, house_liter, house_building, flat,
                         is_registration, is_fact, is_residence))
            # address_id from table ADDRESS
            address_id = cur.fetchone()[0]

            # Add person_id and address_id into table PERSON_ADDRESS
            query_person_address = query_insert_into(person_address) % DB_DICT[person_address]
            cur.execute(query_person_address, (person_id, address_id))

            save_access()
    except:
        messagebox.showinfo(title="Внимание!", message=f'Адрес не записан попробуйте еще раз!')