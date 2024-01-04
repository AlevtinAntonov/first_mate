import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.domain.child import Child
from app_model.variables import LARGE_FONT, CONF_D_W, CONF, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, label_agreement, \
    FONT, CONF_EW
from app_view.gui_input_window import Gui
from app_view_model.functions.compensation_create import compensation_create
from app_view_model.functions.functions import on_validate_input, create_labels_in_grid, buttons_add_new, \
    next_entries, select_date
from app_view_model.functions.movement_create import movement_create
from app_view_model.functions.person_select_combo import person_select_combo
from app_view_model.functions.select_referral_data import display_referral_data


class NewAgreement(Gui):
    def __init__(self, width: str = '500', height: str = '500', child: Child = None):
        super().__init__(width, height)
        self.child = child
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        vcmd = self.root.register(on_validate_input)

        tk.Label(frame, text="Реквизиты договора/ прием в сад", font=LARGE_FONT).grid(row=0, column=0, cnf=CONF_D_W,
                                                                                      columnspan=4, sticky="nsew")
        referral_select_label = ttk.Label(frame, text='Выберите номер направления*', foreground='red')
        referral_select_label.grid(row=2, column=0, cnf=CONF_D_W)

        create_labels_in_grid(frame, label_agreement)
        self.person_select = person_select_combo(db, frame, 14, 1, 'parents')

        self.data = display_referral_data(db)
        self.referral_select = ttk.Combobox(frame)
        self.referral_select["values"] = [value[0] for value in self.data.values()]
        self.referral_select.grid(row=2, column=1, columnspan=1, sticky=tk.W)
        self.referral_select.bind("<<ComboboxSelected>>", self.display_info)

        self.child_full_name_label = ttk.Label(frame, text='ФИО ребенка: ', font=FONT)
        self.child_full_name_label.grid(row=4, column=0, columnspan=4, cnf=CONF_EW)
        self.date_of_birth_label = ttk.Label(frame, text='Дата рождения: ', font=FONT)
        self.date_of_birth_label.grid(row=6, column=0, columnspan=4, cnf=CONF_EW)
        self.team_plan_label = ttk.Label(frame, text='Группа план: ', font=FONT)
        self.team_plan_label.grid(row=8, column=0, columnspan=4, cnf=CONF_EW)

        self.statement_number = ttk.Entry(frame)
        self.statement_number.grid(row=16, column=1, cnf=CONF_D_W)
        self.statement_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 18, 1, CONF_D_W)
        self.date_of_joining_team = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY + 1, 20, 1, CONF_D_W)

        self.contract_number = ttk.Entry(frame)
        self.contract_number.grid(row=22, column=1, cnf=CONF_D_W)
        self.contarct_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 24, 1, CONF_D_W)
        self.contract_begin_date = select_date(frame, CURRENT_YEAR, 9, 1, 26, 1, CONF_D_W)
        self.order_of_admission_number = ttk.Entry(frame)
        self.order_of_admission_number.grid(row=28, column=1, cnf=CONF_D_W)
        self.order_of_admission_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 30, 1, CONF_D_W)
        self.order_of_expulsion_number = ttk.Entry(frame)
        self.order_of_expulsion_number.grid(row=32, column=1, cnf=CONF_D_W)
        self.order_of_expulsion_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 34, 1, CONF_D_W)

        buttons_add_new(self, frame, 40)

        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (movement_create(db, self.statement_number.get(),
                                                                 self.statement_date.get(),
                                                                 self.date_of_joining_team.get(),
                                                                 self.contract_number.get(),
                                                                 self.contarct_date.get(),
                                                                 self.contract_begin_date.get(),
                                                                 self.order_of_admission_number.get(),
                                                                 self.order_of_admission_date.get(),
                                                                 self.child_id,
                                                                 self.referral_id,
                                                                 self.team_id,
                                                                 self.person_select.get()
                                                                 )))
        next_entries(frame)

    def display_info(self, *args):
        selected_name = self.referral_select.get()
        for key, value in self.data.items():
            if value[0] == selected_name:
                self.child_full_name_label.config(text=f"ФИО ребенка: {value[3]} {value[4]} {value[5]}")
                self.date_of_birth_label.config(text=f"Дата рождения: {value[6].strftime("%d.%m.%Y")}")
                self.team_plan_label.config(text=f"Группа план: {value[2]}")
                self.referral_id = key
                self.child_id = value[7]
                self.team_id = value[8]
                # return self.referral_id, self.child_id, self.team_id


if __name__ == '__main__':
    pass
