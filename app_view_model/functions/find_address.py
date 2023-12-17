import tkinter as tk
from app_model.db.db_connect import DB
from app_model.db.db_query import query_full_addresses
from app_model.variables import CONF_D_W
from app_view_model.functions.format_address import format_address

addresses_types = {
    1: ('is_registration', 'Адрес регистрации',),
    2: ('is_fact', 'Адрес фактический',),
    3: ('is_residence', 'Адрес рег. по м.преб.',),
}


def find_full_addresses(db, person_id):
    address_type = addresses_types
    for key, value in address_type.items():
        with db as cur:
            try:
                _ = cur.execute(query_full_addresses % (value[0],), (person_id,)).fetchone()
                address_type[key] += (_,)
            except Exception as e:
                print(f'Ошибка! - {e}')
    return address_type


def print_addresses(dbase, frame, pers_id, row=42, row_step=2):
    if pers_id:
        addresses = find_full_addresses(dbase, pers_id)
        for key, value in addresses.items():
            label = tk.Label(frame, text=f"{value[1]}: {format_address(value[2])}")
            label.grid(row=row, column=0, columnspan=4, cnf=CONF_D_W)
            row += row_step
    else:
        addresses = {
            1: ('Адрес регистрации',),
            2: ('Адрес фактический',),
            3: ('Адрес рег. по м.преб.',),
        }
        for key, value in addresses.items():
            label = tk.Label(frame, text=f"{value[0]}: - ")
            label.grid(row=row, column=0, columnspan=4, cnf=CONF_D_W)
            row += row_step


# def load_full_addresses(db, person_id):
#         with db as cur:
#             cur.execute(query_full_addresses % (value[0],), (person_id,)).fetchone()
#     return address_type



if __name__ == '__main__':
    db = DB('C:/Users/anton/PycharmProjects/first_mate/app_model/db/DB_PROD.FDB')
    p = find_full_addresses(db, 29)
    for k, v in p.items():
        if v[2]:
            print(f'{v[1]}: {format_address(v[2])}')
    print(p)
