import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import address_type, DB_DICT, region_type, town_type, locality_type, street_type, \
    query_full_addresses
from app_model.variables import label_address_list, CONF, CONF_D_W, LARGE_FONT, town_districts
from app_view.gui_input_window import Gui
from app_view_model.functions.address_create import address_create
from app_view_model.functions.find_address import find_full_addresses
from app_view_model.functions.functions import create_labels_in_grid, select_from_db, next_entries, \
    find_id, check_type_address, buttons_add_new, fill_combobox
from app_view_model.functions.person_select_combo import person_select_combo


class AddressWin(Gui):
    def __init__(self, width: str = '650', height: str = '500'):
        # окно для ввода адреса
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)

        tk.Label(frame, text="Адрес", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W, columnspan=4, sticky="nsew")

        def update_address_info(event):
            type_var = self.address_type_id.get()
            addresses_from_db_dict = find_full_addresses(db, person_select.get(), query_full_addresses)
            match type_var:
                case 'регистрации по месту жительства':
                    dict_key = 1
                case 'фактического проживания':
                    dict_key = 2
                case 'регистрации по месту пребывания':
                    dict_key = 3

            if person_select.get():
                try:
                    zipcode_var.set(addresses_from_db_dict[dict_key][2][0])
                    region_var.set(addresses_from_db_dict[dict_key][2][1])
                    region_type_id_var.set(addresses_from_db_dict[dict_key][2][2])
                    district_var.set(addresses_from_db_dict[dict_key][2][3])
                    town_var.set(addresses_from_db_dict[dict_key][2][4])
                    town_type_id_var.set(addresses_from_db_dict[dict_key][2][5])
                    locality_var.set(addresses_from_db_dict[dict_key][2][6])
                    locality_type_id_var.set(addresses_from_db_dict[dict_key][2][7])
                    street_var.set(addresses_from_db_dict[dict_key][2][8])
                    street_type_id_var.set(addresses_from_db_dict[dict_key][2][9])
                    house_var.set(addresses_from_db_dict[dict_key][2][10])
                    house_body_var.set(addresses_from_db_dict[dict_key][2][11])
                    house_liter_var.set(addresses_from_db_dict[dict_key][2][12])
                    house_building_var.set(addresses_from_db_dict[dict_key][2][13])
                    flat_var.set(addresses_from_db_dict[dict_key][2][14])

                except Exception as err:
                    print(f'Ошибка у данной персоны нет такого типа адреса {err=}')
            else:
                zipcode_var.set('')
                region_var.set('')
                region_type_id_var.set('')
                district_var.set('')
                town_var.set('')
                town_type_id_var.set('')
                locality_var.set('')
                locality_type_id_var.set('')
                street_var.set('')
                street_type_id_var.set('')
                house_var.set('')
                house_body_var.set('')
                house_liter_var.set('')
                house_building_var.set('')
                flat_var.set('')

        self.address_type_id_var = tk.StringVar()
        child_select_label = ttk.Label(frame, text='Выберите ФИО*', foreground='red')
        child_select_label.grid(row=2, column=0, cnf=CONF_D_W)

        zipcode_var = tk.StringVar()
        region_var = tk.StringVar()
        region_type_id_var = tk.StringVar()
        district_var = tk.StringVar()
        town_var = tk.StringVar()
        town_type_id_var = tk.StringVar()
        locality_var = tk.StringVar()
        locality_type_id_var = tk.StringVar()
        street_var = tk.StringVar()
        street_type_id_var = tk.StringVar()
        house_var = tk.StringVar()
        house_body_var = tk.StringVar()
        house_liter_var = tk.StringVar()
        house_building_var = tk.StringVar()
        flat_var = tk.StringVar()

        person_select = person_select_combo(db, frame, 2, 1)

        create_labels_in_grid(frame, label_address_list)

        self.same_fact_as_register_var = tk.BooleanVar()
        self.same_fact_as_register_var.set(False)
        self.same_residence_as_fact_var = tk.BooleanVar()
        self.same_residence_as_fact_var.set(False)
        same_fact_as_register_checkbox = tk.Checkbutton(frame,
                                                        text='Фактический адрес совпадает с регистрацией',
                                                        variable=self.same_fact_as_register_var,
                                                        onvalue=True, offvalue=False)
        same_fact_as_register_checkbox.grid(row=30, column=0, cnf=CONF, columnspan=3)
        same_residence_as_fact_checkbox = tk.Checkbutton(frame,
                                                         text='Фактический адрес совпадает с рег. по месту пребывания',
                                                         variable=self.same_residence_as_fact_var, onvalue=True,
                                                         offvalue=False)

        same_residence_as_fact_checkbox.grid(row=32, column=0, cnf=CONF, columnspan=3)

        value_from_db = [v for v in fill_combobox(db, 'address_type', 'address_type_id',
                                                  'address_type_name').values()]
        self.address_type_id = ttk.Combobox(frame, values=value_from_db, state='readonly', width=45)
        self.address_type_id.grid(row=4, column=1, columnspan=3, cnf=CONF_D_W)

        self.zipcode = ttk.Entry(frame, textvariable=zipcode_var)
        self.zipcode.grid(row=6, column=2, cnf=CONF_D_W)
        self.region = ttk.Entry(frame, textvariable=region_var)
        self.region.grid(row=8, column=2, cnf=CONF_D_W)
        self.region_type = select_from_db(frame, db, 'region_type', 'region_type_id',
                                          'region_type_name', 8, 1,
                                          CONF_D_W, width=10)
        self.district = ttk.Entry(frame, textvariable=district_var)
        self.district.grid(row=10, column=2, cnf=CONF_D_W)
        self.town = ttk.Entry(frame, textvariable=town_var)
        self.town.grid(row=12, column=2, cnf=CONF_D_W)
        self.town_type = select_from_db(frame, db, 'town_type', 'town_type_id', 'town_type_name', 12,
                                        1,
                                        CONF_D_W, width=10)
        self.locality = ttk.Entry(frame, textvariable=locality_var)
        self.locality.grid(row=14, column=2, cnf=CONF_D_W)
        self.locality_type = select_from_db(frame, db, 'locality_type', 'locality_type_id',
                                            'locality_type_name', 14,
                                            1,
                                            CONF_D_W, width=10)
        self.street = ttk.Entry(frame, textvariable=street_var)
        self.street.grid(row=16, column=2, cnf=CONF_D_W)
        self.street_type = select_from_db(frame, db, 'street_type', 'street_type_id',
                                          'street_type_name', 16,
                                          1,
                                          CONF_D_W,
                                          width=10)
        self.house = ttk.Entry(frame, textvariable=house_var)
        self.house.grid(row=18, column=2, cnf=CONF_D_W)
        self.house_body = ttk.Entry(frame, textvariable=house_body_var)
        self.house_body.grid(row=20, column=2, cnf=CONF_D_W)
        self.house_liter = ttk.Entry(frame, textvariable=house_liter_var)
        self.house_liter.grid(row=22, column=2, cnf=CONF_D_W)
        self.house_building = ttk.Entry(frame, textvariable=house_building_var)
        self.house_building.grid(row=24, column=2, cnf=CONF_D_W)
        self.flat = ttk.Entry(frame, textvariable=flat_var)
        self.flat.grid(row=26, column=2, cnf=CONF_D_W)
        self.town_district = ttk.Combobox(frame, values=list(town_districts.keys()))
        self.town_district.grid(row=28, column=2, cnf=CONF_D_W)

        self.address_type_id.bind("<<ComboboxSelected>>", update_address_info)

        buttons_add_new(self, frame, 40)
        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)

        btn_ok.bind('<Button-1>',
                    lambda event: (take_type_address(), address_create(db, person_select.get(), self.address_type_id,
                                                                       self.zipcode.get(),
                                                                       self.region.get(), self.region_type_id,
                                                                       self.district.get(),
                                                                       self.town.get(), self.town_type_id,
                                                                       self.locality.get(),
                                                                       self.locality_type_id, self.street.get(),
                                                                       self.street_type_id,
                                                                       self.house.get(), self.house_body.get(),
                                                                       self.house_liter.get(),
                                                                       self.house_building.get(), self.flat.get(),
                                                                       self.is_registration, self.is_fact,
                                                                       self.is_residence, self.town_district.get())))
        next_entries(frame)

        def take_type_address():
            self.address_type_id = find_id(db, address_type, DB_DICT[address_type][0], DB_DICT[address_type][1],
                                           self.address_type_id.get() or self.address_type_id)
            self.region_type_id = find_id(db, region_type, DB_DICT[region_type][0], DB_DICT[region_type][1],
                                          self.region_type.get())
            self.town_type_id = find_id(db, town_type, DB_DICT[town_type][0], DB_DICT[town_type][1],
                                        self.town_type.get())
            self.locality_type_id = find_id(db, locality_type, DB_DICT[locality_type][0], DB_DICT[locality_type][1],
                                            self.locality_type.get())
            self.street_type_id = find_id(db, street_type, DB_DICT[street_type][0], DB_DICT[street_type][1],
                                          self.street_type.get())
            match self.address_type_id:
                case 1:
                    registration, fact, residence = True, False, False
                case 2:
                    registration, fact, residence = False, True, False
                case 3:
                    registration, fact, residence = False, False, True
                case _:
                    residence, registration, fact = False, False, False

            self.is_registration, self.is_fact, self.is_residence = check_type_address(registration,
                                                                                       fact, residence,
                                                                                       self.same_fact_as_register_var.get(),
                                                                                       self.same_residence_as_fact_var.get())


if __name__ == '__main__':
    pass
