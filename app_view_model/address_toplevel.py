import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.db.db_query import address_type, DB_DICT, region_type, town_type, locality_type, street_type
from app_model.domain.address import Address
from app_model.variables import MAIN_ICO, label_address_list, CONF, CONF_D_W
from app_view_model.functions.address_create import address_create
from app_view_model.functions.functions import position_center, create_labels_in_grid, select_from_db, next_entries, \
    find_id, check_type_address


class AddressWindow:
    def __init__(self, person_id):
        # окно для ввода адреса
        self.person_id = person_id
        self.address_window = tk.Toplevel()
        self.address_window.title("Ввод адреса")
        self.address_window.geometry('600x450')
        self.address_window.iconbitmap(MAIN_ICO)
        position_center(self.address_window, 600, 450)

        tk.Label(self.address_window, text=self.person_id).grid(row=55, column=0)

        create_labels_in_grid(self.address_window, label_address_list)
        self.create_address_window()

    def create_address_window(self):
        address = Address()
        self.same_fact_as_register_var = tk.BooleanVar()
        self.same_fact_as_register_var.set(False)
        self.same_residence_as_fact_var = tk.BooleanVar()
        self.same_residence_as_fact_var.set(False)
        same_fact_as_register_checkbox = tk.Checkbutton(self.address_window,
                                                        text='Фактический адрес совпадает с регистрацией',
                                                        variable=self.same_fact_as_register_var,
                                                        onvalue=True, offvalue=False)
        same_fact_as_register_checkbox.grid(row=28, column=0, cnf=CONF, columnspan=3)
        same_residence_as_fact_checkbox = tk.Checkbutton(self.address_window,
                                                         text='Фактический адрес совпадает с рег. по месту пребывания',
                                                         variable=self.same_residence_as_fact_var, onvalue=True,
                                                         offvalue=False)

        same_residence_as_fact_checkbox.grid(row=30, column=0, cnf=CONF, columnspan=3)
        address.address_type_id = select_from_db(self.address_window, db, 'address_type', 'address_type_id',
                                                 'address_type_name', 4,
                                                 3, CONF_D_W)

        address.zipcode = ttk.Entry(self.address_window)
        address.zipcode.grid(row=6, column=3, cnf=CONF_D_W)
        address.region = ttk.Entry(self.address_window)
        address.region.grid(row=8, column=3, cnf=CONF_D_W)
        address.region_type = select_from_db(self.address_window, db, 'region_type', 'region_type_id',
                                             'region_type_name', 8, 2,
                                             CONF_D_W, width=10)
        address.district = ttk.Entry(self.address_window)
        address.district.grid(row=10, column=3, cnf=CONF_D_W)
        address.town = ttk.Entry(self.address_window)
        address.town.grid(row=12, column=3, cnf=CONF_D_W)
        address.town_type = select_from_db(self.address_window, db, 'town_type', 'town_type_id', 'town_type_name', 12,
                                           2,
                                           CONF_D_W, width=10)
        address.locality = ttk.Entry(self.address_window)
        address.locality.grid(row=14, column=3, cnf=CONF_D_W)
        address.locality_type = select_from_db(self.address_window, db, 'locality_type', 'locality_type_id',
                                               'locality_type_name', 14,
                                               2,
                                               CONF_D_W, width=10)
        address.street = ttk.Entry(self.address_window)
        address.street.grid(row=16, column=3, cnf=CONF_D_W)
        address.street_type = select_from_db(self.address_window, db, 'street_type', 'street_type_id',
                                             'street_type_name', 16,
                                             2,
                                             CONF_D_W,
                                             width=10)
        address.house = ttk.Entry(self.address_window)
        address.house.grid(row=18, column=3, cnf=CONF_D_W)
        address.house_body = ttk.Entry(self.address_window)
        address.house_body.grid(row=20, column=3, cnf=CONF_D_W)
        address.house_liter = ttk.Entry(self.address_window)
        address.house_liter.grid(row=22, column=3, cnf=CONF_D_W)
        address.house_building = ttk.Entry(self.address_window)
        address.house_building.grid(row=24, column=3, cnf=CONF_D_W)
        address.flat = ttk.Entry(self.address_window)
        address.flat.grid(row=26, column=3, cnf=CONF_D_W)

        # buttons_add_new(self, self.address_window, 32)
        btn_ok = tk.Button(self.address_window, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=2, cnf=CONF)

        btn_ok.bind('<Button-1>',
                    lambda event: (take_type_address(),
                                   address_create(db, self.person_id, address.address_type_id, address.zipcode.get(),
                                                  address.region.get(), address.region_type_id, address.district.get(),
                                                  address.town.get(), address.town_type_id, address.locality.get(),
                                                  address.locality_type_id, address.street.get(),
                                                  address.street_type_id,
                                                  address.house.get(), address.house_body.get(),
                                                  address.house_liter.get(),
                                                  address.house_building.get(), address.flat.get(),
                                                  address.is_registration, address.is_fact, address.is_residence),
                                   self.address_window.destroy()))
        next_entries(self.address_window)

        def take_type_address():
            address.address_type_id = find_id(db, address_type, DB_DICT[address_type][0], DB_DICT[address_type][1],
                                              address.address_type_id.get())
            address.region_type_id = find_id(db, region_type, DB_DICT[region_type][0], DB_DICT[region_type][1],
                                             address.region_type.get())
            address.town_type_id = find_id(db, town_type, DB_DICT[town_type][0], DB_DICT[town_type][1],
                                           address.town_type.get())
            address.locality_type_id = find_id(db, locality_type, DB_DICT[locality_type][0], DB_DICT[locality_type][1],
                                               address.locality_type.get())
            address.street_type_id = find_id(db, street_type, DB_DICT[street_type][0], DB_DICT[street_type][1],
                                             address.street_type.get())
            match address.address_type_id:
                case 1:
                    registration, fact, residence = True, False, False
                case 2:
                    registration, fact, residence = False, True, False
                case 3:
                    registration, fact, residence = False, False, True
                case _:
                    residence, registration, fact = False, False, False

            address.is_registration, address.is_fact, address.is_residence = check_type_address(
                registration, fact,
                residence,
                self.same_fact_as_register_var.get(),
                self.same_residence_as_fact_var.get())

        self.address_window.grab_set()
        self.address_window.focus_set()


if __name__ == '__main__':
    pass
