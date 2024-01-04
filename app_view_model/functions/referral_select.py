import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.variables import CONF_D_W, FONT, CONF_EW
from app_view_model.functions.person_select_combo import person_select_combo
from app_view_model.functions.select_referral_data import display_referral_data


def referral_select(self, frame, row=2, column=0):
    referral_select_label = ttk.Label(frame, text='Выберите номер направления*', foreground='red')
    referral_select_label.grid(row=row, column=column, cnf=CONF_D_W)
    self.data = display_referral_data(db)
    self.referral_select = ttk.Combobox(frame)
    self.referral_select["values"] = [value[0] for value in self.data.values()]
    self.referral_select.grid(row=row, column=column + 1, columnspan=1, sticky=tk.W)
    self.referral_select.bind("<<ComboboxSelected>>", self.display_info)

    self.child_full_name_label = ttk.Label(frame, text='ФИО ребенка: ', font=FONT)
    self.child_full_name_label.grid(row=row + 2, column=0, columnspan=4, cnf=CONF_EW)
    self.date_of_birth_label = ttk.Label(frame, text='Дата рождения: ', font=FONT)
    self.date_of_birth_label.grid(row=row + 4, column=0, columnspan=4, cnf=CONF_EW)
    self.team_plan_label = ttk.Label(frame, text='Группа план: ', font=FONT)
    self.team_plan_label.grid(row=row + 6, column=0, columnspan=4, cnf=CONF_EW)
