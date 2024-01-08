import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import team, DB_DICT
from app_model.domain.child import Child
from app_model.variables import LARGE_FONT, CONF_D_W, CONF, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, label_agreement
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import on_validate_input, create_labels_in_grid, buttons_add_new, \
    next_entries, select_date, select_from_db
from app_view_model.functions.movement_create import movement_create
from app_view_model.functions.person_select_combo import person_select_combo
from app_view_model.functions.referral_select import referral_select


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
        referral_select(self, frame)

        self.person_select = person_select_combo(db, frame, 14, 1, 'parents')
        create_labels_in_grid(frame, label_agreement)

        self.team_id_value = select_from_db(frame, db, team, DB_DICT[team][0], DB_DICT[team][1], 15, 1, CONF_D_W, 2)

        self.statement_number = ttk.Entry(frame)
        self.statement_number.grid(row=16, column=1, cnf=CONF_D_W)
        self.statement_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 18, 1, CONF_D_W)
        self.date_of_joining_team = select_date(frame, CURRENT_YEAR, 9, 1, 20, 1, CONF_D_W)

        self.contract_number = ttk.Entry(frame)
        self.contract_number.grid(row=22, column=1, cnf=CONF_D_W)
        self.contarct_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 24, 1, CONF_D_W)
        self.contract_begin_date = select_date(frame, CURRENT_YEAR, 9, 1, 26, 1, CONF_D_W)
        self.order_of_admission_number = ttk.Entry(frame)
        self.order_of_admission_number.grid(row=28, column=1, cnf=CONF_D_W)
        self.order_of_admission_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 30, 1, CONF_D_W)
        self.order_of_expulsion_number = ttk.Entry(frame)
        self.order_of_expulsion_number.grid(row=32, column=1, cnf=CONF_D_W)
        self.order_of_expulsion_date = select_date(frame, CURRENT_YEAR + 5, 8, 31, 34, 1, CONF_D_W)

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
                                                                 self.team_id_value.get(),
                                                                 self.person_select.get()
                                                                 )))
        next_entries(frame)


if __name__ == '__main__':
    pass
