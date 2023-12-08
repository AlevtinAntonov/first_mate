import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.domain.address import Address
from app_model.variables import MAIN_ICO, label_address_list, CONF, CONF_D_W
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
        parent_address = Address()
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
        address_type_name = select_from_db(self.address_window, db, 'address_type', 'address_type_id',
                                           'address_type_name', 4,
                                           3, CONF_D_W)

        parent_address.zipcode = ttk.Entry(self.address_window)
        parent_address.zipcode.grid(row=6, column=3, cnf=CONF_D_W)
        parent_address.region = ttk.Entry(self.address_window)
        parent_address.region.grid(row=8, column=3, cnf=CONF_D_W)
        region_type = select_from_db(self.address_window, db, 'region_type', 'region_type_id', 'region_type_name', 8, 2,
                                     CONF_D_W, width=10)
        # self.region_type_id = find_id(db, 'region_type', 'region_type_id', 'region_type_name', region_type.get())
        parent_address.district = ttk.Entry(self.address_window)
        parent_address.district.grid(row=10, column=3, cnf=CONF_D_W)
        parent_address.town = ttk.Entry(self.address_window)
        parent_address.town.grid(row=12, column=3, cnf=CONF_D_W)
        town_type = select_from_db(self.address_window, db, 'town_type', 'town_type_id', 'town_type_name', 12, 2,
                                   CONF_D_W, width=10)
        # self.town_type_id = find_id(db, 'town_type', 'town_type_id', 'town_type_name', town_type.get())
        parent_address.locality = ttk.Entry(self.address_window)
        parent_address.locality.grid(row=14, column=3, cnf=CONF_D_W)
        locality_type = select_from_db(self.address_window, db, 'locality_type', 'locality_type_id',
                                       'locality_type_name', 14,
                                       2,
                                       CONF_D_W, width=10)
        # self.locality_type_id = find_id(db, 'locality_type', 'locality_type_id', 'locality_type_name',
        #                                 locality_type.get())
        parent_address.street = ttk.Entry(self.address_window)
        parent_address.street.grid(row=16, column=3, cnf=CONF_D_W)
        street_type = select_from_db(self.address_window, db, 'street_type', 'street_type_id', 'street_type_name', 16,
                                     2,
                                     CONF_D_W,
                                     width=10)
        # self.street_type_id = find_id(db, 'street_type', 'street_type_id', 'street_type_name', street_type.get())
        parent_address.house = ttk.Entry(self.address_window)
        parent_address.house.grid(row=18, column=3, cnf=CONF_D_W)
        parent_address.house_body = ttk.Entry(self.address_window)
        parent_address.house_body.grid(row=20, column=3, cnf=CONF_D_W)
        parent_address.house_liter = ttk.Entry(self.address_window)
        parent_address.house_liter.grid(row=22, column=3, cnf=CONF_D_W)
        parent_address.house_building = ttk.Entry(self.address_window)
        parent_address.house_building.grid(row=24, column=3, cnf=CONF_D_W)
        parent_address.flat = ttk.Entry(self.address_window)
        parent_address.flat.grid(row=26, column=3, cnf=CONF_D_W)

        # buttons_add_new(self, self.address_window, 32)
        btn_ok = tk.Button(self.address_window, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=2, cnf=CONF)

        btn_ok.bind('<Button-1>',
                    lambda event: (take_input_data(), print(self.address_dict), save_input_address()))
        # btn_ok.bind('<Button-1>',
        #             lambda event: (take_input_data(), insert_into_table(db, address, DB_DICT[address], (
        #                 self.address_type_id, self.zipcode.get(), self.region.get(), self.region_type_id,
        #                 self.district.get(), self.town.get(), self.town_type_id, self.locality.get(),
        #                 self.locality_type_id, self.street.get(), self.street_type_id, self.house.get(),
        #                 self.house_body.get(), self.house_liter.get(), self.house_building.get(), self.flat.get(),
        #                 self.is_registration, self.is_fact, self.is_residence)), save_access()))

        next_entries(self.address_window)

        def take_input_data():
            parent_address.address_type_id = find_id(db, 'address_type', 'address_type_id', 'address_type_name',
                                                     address_type_name.get())
            parent_address.region_type_id = find_id(db, 'region_type', 'region_type_id', 'region_type_name',
                                                    region_type.get())
            parent_address.town_type_id = find_id(db, 'town_type', 'town_type_id', 'town_type_name', town_type.get())
            parent_address.locality_type_id = find_id(db, 'locality_type', 'locality_type_id', 'locality_type_name',
                                                      locality_type.get())
            parent_address.street_type_id = find_id(db, 'street_type', 'street_type_id', 'street_type_name',
                                                    street_type.get())
            parent_address.street_type_id = find_id(db, 'street_type', 'street_type_id', 'street_type_name',
                                                    street_type.get())
            match parent_address.address_type_id:
                case 1:
                    registration, fact, residence = True, False, False
                case 2:
                    registration, fact, residence = False, True, False
                case 3:
                    registration, fact, residence = False, False, True
                case _:
                    residence, registration, fact = False, False, False

            parent_address.is_registration, parent_address.is_fact, parent_address.is_residence = check_type_address(
                registration, fact,
                residence,
                self.same_fact_as_register_var.get(),
                self.same_residence_as_fact_var.get())
            address_dict = {'address_type_id': parent_address.address_type_id,
                            'zipcode': parent_address.zipcode.get(),
                            'region': parent_address.region.get(),
                            'region_type_id': parent_address.region_type_id,
                            'district': parent_address.district.get(),
                            'town': parent_address.town.get(),
                            'town_type_id': parent_address.town_type_id,
                            'locality': parent_address.locality.get(),
                            'locality_type_id': parent_address.locality_type_id,
                            'street': parent_address.street.get(),
                            'street_type_id': parent_address.street_type_id,
                            'house': parent_address.house.get(),
                            'house_body': parent_address.house_body.get(),
                            'house_liter': parent_address.house_liter.get(),
                            'house_building': parent_address.house_building.get(),
                            'flat': parent_address.flat.get(),
                            'is_registration': parent_address.is_registration,
                            'is_fact': parent_address.is_fact,
                            'is_residence': parent_address.is_residence}
            # ', '.join(filter(None, map(str, address_dict.values())))
            self.address_dict = address_dict
            return self.address_dict

        def save_input_address():
            self.address_window.destroy()
            # self.address_dict = take_input_data()
            # print(self.address_dict)

            # a = ', '.join(filter(None, map(str, take_input_data().values())))
            # address_label = tk.Label(self.address_window, text=f"Адрес: {a}")
            # address_label.grid(row=26, column=1, columnspan=2)

        self.address_window.grab_set()
        self.address_window.focus_set()
