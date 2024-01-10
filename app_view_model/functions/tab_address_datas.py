import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.variables import label_address_list, CONF_D_W, town_districts
from app_view_model.functions.functions import create_labels_in_grid, select_from_db


def show_address_datas(tab):
    create_labels_in_grid(tab, label_address_list)
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

    # address_type_id = ttk.Combobox(tab, values=value_from_db, state='readonly', width=45)
    address_type_id = ttk.Combobox(tab, state='readonly', width=45)
    address_type_id.grid(row=4, column=1, columnspan=3, cnf=CONF_D_W)

    zipcode = ttk.Entry(tab, textvariable=zipcode_var)
    zipcode.grid(row=6, column=2, cnf=CONF_D_W)
    region = ttk.Entry(tab, textvariable=region_var)
    region.grid(row=8, column=2, cnf=CONF_D_W)
    region_type = select_from_db(tab, db, 'region_type', 'region_type_id',
                                 'region_type_name', 8, 1,
                                 CONF_D_W, width=10)
    district = ttk.Entry(tab, textvariable=district_var)
    district.grid(row=10, column=2, cnf=CONF_D_W)
    town = ttk.Entry(tab, textvariable=town_var)
    town.grid(row=12, column=2, cnf=CONF_D_W)
    town_type = select_from_db(tab, db, 'town_type', 'town_type_id', 'town_type_name', 12,
                               1,
                               CONF_D_W, width=10)
    locality = ttk.Entry(tab, textvariable=locality_var)
    locality.grid(row=14, column=2, cnf=CONF_D_W)
    locality_type = select_from_db(tab, db, 'locality_type', 'locality_type_id',
                                   'locality_type_name', 14,
                                   1,
                                   CONF_D_W, width=10)
    street = ttk.Entry(tab, textvariable=street_var)
    street.grid(row=16, column=2, cnf=CONF_D_W)
    street_type = select_from_db(tab, db, 'street_type', 'street_type_id',
                                 'street_type_name', 16,
                                 1,
                                 CONF_D_W,
                                 width=10)
    house = ttk.Entry(tab, textvariable=house_var)
    house.grid(row=18, column=2, cnf=CONF_D_W)
    house_body = ttk.Entry(tab, textvariable=house_body_var)
    house_body.grid(row=20, column=2, cnf=CONF_D_W)
    house_liter = ttk.Entry(tab, textvariable=house_liter_var)
    house_liter.grid(row=22, column=2, cnf=CONF_D_W)
    house_building = ttk.Entry(tab, textvariable=house_building_var)
    house_building.grid(row=24, column=2, cnf=CONF_D_W)
    flat = ttk.Entry(tab, textvariable=flat_var)
    flat.grid(row=26, column=2, cnf=CONF_D_W)
    town_district = ttk.Combobox(tab, values=list(town_districts.keys()))
    town_district.grid(row=28, column=2, cnf=CONF_D_W)

    # address_type_id.bind("<<ComboboxSelected>>", update_address_info)
