import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import address_type, DB_DICT, region_type, town_type, locality_type, street_type
from app_model.domain.address import Address
from app_model.variables import MAIN_ICO, label_address_list, CONF, CONF_D_W
from app_view.gui_input_window import Gui
from app_view_model.functions.address_create import address_create
from app_view_model.functions.functions import position_center, create_labels_in_grid, select_from_db, next_entries, \
    find_id, check_type_address, buttons_add_new, fill_combobox, find_child, get_key
from app_view_model.functions.person_select_combo import person_select_combo


class AddressWin(Gui):
    def __init__(self, width: str = '650', height: str = '450'):
        # окно для ввода адреса
        super().__init__(width, height)
        self.width = width
        self.height = height
        # self.person_id = person_id
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        address = Address()
        child_select_label = ttk.Label(frame, text='Выберите ФИО*', foreground='red')
        child_select_label.grid(row=2, column=0, cnf=CONF_D_W)
        person_select = person_select_combo(db, frame, 2, 1)
        # person_select.bind("<KeyRelease>", update_combo_options)
        # child_dict = fill_combobox(db, 'child_list', None, None)
        # child_select = find_child(frame, child_dict, 2, 1, CONF_D_W)
        # tk.Label(frame, text=self.person_id).grid(row=55, column=0)
        create_labels_in_grid(frame, label_address_list)

        self.same_fact_as_register_var = tk.BooleanVar()
        self.same_fact_as_register_var.set(False)
        self.same_residence_as_fact_var = tk.BooleanVar()
        self.same_residence_as_fact_var.set(False)
        same_fact_as_register_checkbox = tk.Checkbutton(frame,
                                                        text='Фактический адрес совпадает с регистрацией',
                                                        variable=self.same_fact_as_register_var,
                                                        onvalue=True, offvalue=False)
        same_fact_as_register_checkbox.grid(row=28, column=0, cnf=CONF, columnspan=3)
        same_residence_as_fact_checkbox = tk.Checkbutton(frame,
                                                         text='Фактический адрес совпадает с рег. по месту пребывания',
                                                         variable=self.same_residence_as_fact_var, onvalue=True,
                                                         offvalue=False)

        same_residence_as_fact_checkbox.grid(row=30, column=0, cnf=CONF, columnspan=3)
        address.address_type_id = select_from_db(frame, db, 'address_type', 'address_type_id',
                                                 'address_type_name', 4,
                                                 1, CONF_D_W, 3, width=45)

        address.zipcode = ttk.Entry(frame)
        address.zipcode.grid(row=6, column=2, cnf=CONF_D_W)
        address.region = ttk.Entry(frame)
        address.region.grid(row=8, column=2, cnf=CONF_D_W)
        address.region_type = select_from_db(frame, db, 'region_type', 'region_type_id',
                                             'region_type_name', 8, 1,
                                             CONF_D_W, width=10)
        address.district = ttk.Entry(frame)
        address.district.grid(row=10, column=2, cnf=CONF_D_W)
        address.town = ttk.Entry(frame)
        address.town.grid(row=12, column=2, cnf=CONF_D_W)
        address.town_type = select_from_db(frame, db, 'town_type', 'town_type_id', 'town_type_name', 12,
                                           1,
                                           CONF_D_W, width=10)
        address.locality = ttk.Entry(frame)
        address.locality.grid(row=14, column=2, cnf=CONF_D_W)
        address.locality_type = select_from_db(frame, db, 'locality_type', 'locality_type_id',
                                               'locality_type_name', 14,
                                               1,
                                               CONF_D_W, width=10)
        address.street = ttk.Entry(frame)
        address.street.grid(row=16, column=2, cnf=CONF_D_W)
        address.street_type = select_from_db(frame, db, 'street_type', 'street_type_id',
                                             'street_type_name', 16,
                                             1,
                                             CONF_D_W,
                                             width=10)
        address.house = ttk.Entry(frame)
        address.house.grid(row=18, column=2, cnf=CONF_D_W)
        address.house_body = ttk.Entry(frame)
        address.house_body.grid(row=20, column=2, cnf=CONF_D_W)
        address.house_liter = ttk.Entry(frame)
        address.house_liter.grid(row=22, column=2, cnf=CONF_D_W)
        address.house_building = ttk.Entry(frame)
        address.house_building.grid(row=24, column=2, cnf=CONF_D_W)
        address.flat = ttk.Entry(frame)
        address.flat.grid(row=26, column=2, cnf=CONF_D_W)
        buttons_add_new(self, frame, 40)
        # buttons_add_new(self, self.address_window, 32)
        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)

        btn_ok.bind('<Button-1>',
                    lambda event: (take_type_address(),
                                   address_create(db, get_key(child_select.get(), child_dict), address.address_type_id,
                                                  address.zipcode.get(),
                                                  address.region.get(), address.region_type_id, address.district.get(),
                                                  address.town.get(), address.town_type_id, address.locality.get(),
                                                  address.locality_type_id, address.street.get(),
                                                  address.street_type_id,
                                                  address.house.get(), address.house_body.get(),
                                                  address.house_liter.get(),
                                                  address.house_building.get(), address.flat.get(),
                                                  address.is_registration, address.is_fact, address.is_residence),
                                   frame.destroy()))
        next_entries(frame)

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

        # self.address_window.grab_set()
        # self.address_window.focus_set()

if __name__ == '__main__':
    pass
