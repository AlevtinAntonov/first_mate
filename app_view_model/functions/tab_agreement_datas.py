from tkinter import ttk

from app_model.db.db_connect import db
from app_model.db.db_query import team, DB_DICT
from app_model.variables import label_agreement, CONF_D_W, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY
from app_view_model.functions.functions import create_labels_in_grid, select_from_db, select_date
from app_view_model.functions.person_select_combo import person_select_combo


def show_agreement_datas(tab):

    create_labels_in_grid(tab, label_agreement)

    person_select = person_select_combo(db, tab, 14, 1, 'parents')
    create_labels_in_grid(tab, label_agreement)

    team_id_value = select_from_db(tab, db, team, DB_DICT[team][0], DB_DICT[team][1], 15, 1, CONF_D_W, 2)

    statement_number = ttk.Entry(tab)
    statement_number.grid(row=16, column=1, cnf=CONF_D_W)
    statement_date = select_date(tab, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 18, 1, CONF_D_W)
    date_of_joining_team = select_date(tab, CURRENT_YEAR, 9, 1, 20, 1, CONF_D_W)

    contract_number = ttk.Entry(tab)
    contract_number.grid(row=22, column=1, cnf=CONF_D_W)
    contarct_date = select_date(tab, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 24, 1, CONF_D_W)
    contract_begin_date = select_date(tab, CURRENT_YEAR, 9, 1, 26, 1, CONF_D_W)
    order_of_admission_number = ttk.Entry(tab)
    order_of_admission_number.grid(row=28, column=1, cnf=CONF_D_W)
    order_of_admission_date = select_date(tab, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 30, 1, CONF_D_W)
    order_of_expulsion_number = ttk.Entry(tab)
    order_of_expulsion_number.grid(row=32, column=1, cnf=CONF_D_W)
    order_of_expulsion_date = select_date(tab, CURRENT_YEAR + 5, 8, 31, 34, 1, CONF_D_W)