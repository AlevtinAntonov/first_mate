import tkinter as tk
from app_model.variables import CONF_D_W
from app_view_model.functions.format_address import format_address


def find_full_addresses(db, person_id, query_full_addresses):
    addresses_types = {
        1: ('is_registration', 'Адрес регистрации'),
        2: ('is_fact', 'Адрес фактический'),
        3: ('is_residence', 'Адрес рег. по м.преб.'),
    }
    address_type = addresses_types
    for key, value in address_type.items():
        with db as cur:
            try:
                _ = cur.execute(query_full_addresses % (value[0],), (person_id,)).fetchone()
                address_type[key] += (_,)
            except Exception as e:
                print(f'Ошибка def find_full_addresses! - {e}')
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


if __name__ == '__main__':
    pass
