from tkinter import ttk

from app_model.db.db_connect import db
from app_model.db.db_query import gender, DB_DICT
from app_model.variables import label_child_list, CONF_D_W, DEFAULT_BORN_YEAR, DEFAULT_BORN_MONTH, DEFAULT_BORN_DAY
from app_view_model.functions.document_entries import document_entries
from app_view_model.functions.functions import create_labels_in_grid, select_from_db, select_date, on_validate_input


def show_child_datas(tab):

    create_labels_in_grid(tab, label_child_list)

    vcmd = tab.register(on_validate_input)
    ttk.Label(tab, text='Фамилия: ').grid(row=4, column=0, cnf=CONF_D_W)
    ttk.Label(tab, text='Имя: ').grid(row=5, column=0, cnf=CONF_D_W)
    ttk.Label(tab, text='Отчество: ').grid(row=6, column=0, cnf=CONF_D_W)
    last_name = ttk.Entry(tab, validate='key', validatecommand=(vcmd, "%S"))
    last_name.grid(row=4, column=1, cnf=CONF_D_W)
    first_name = ttk.Entry(tab, validate='key', validatecommand=(vcmd, "%S"))
    first_name.grid(row=5, column=1, cnf=CONF_D_W)
    patronymic = ttk.Entry(tab, validate='key', validatecommand=(vcmd, "%S"))
    patronymic.grid(row=6, column=1, cnf=CONF_D_W)
    gender_id = select_from_db(tab, db, gender, DB_DICT[gender][0], DB_DICT[gender][1], 7, 1, CONF_D_W, width=15)
    date_of_birth = select_date(tab, DEFAULT_BORN_YEAR, DEFAULT_BORN_MONTH, DEFAULT_BORN_DAY, 8, 1,
                                CONF_D_W)
    date_of_birth = ttk.Label(tab, text='Дата рождения: ')
    date_of_birth.grid(row=8, column=0, cnf=CONF_D_W)
    gender_label = ttk.Label(tab, text="Пол: ")
    gender_label.grid(row=7, column=0, cnf=CONF_D_W)
    place_of_birth = ttk.Entry(tab)
    place_of_birth.grid(row=18, column=1, cnf=CONF_D_W, columnspan=3, sticky="ew")

    document_assembly_record = ttk.Entry(tab)
    document_assembly_record.grid(row=20, column=1, cnf=CONF_D_W)
    citizenship_id, document_type_id, document_series, document_number, document_issued_by, document_date_of_issue = (
        document_entries(tab, (22, 1)))
    sniils = ttk.Entry(tab)
    sniils.grid(row=30, column=1, cnf=CONF_D_W)

    # buttons_add_new(self, tab, 40)