import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.variables import LARGE_FONT, CONF_D_W, CONF
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, next_entries
from app_view_model.functions.person_select_combo import person_select_combo
from app_view_model.functions.referral_select import referral_select
from app_view_model.print_forms.functions.print_agreement_form import print_agreement


class PrintFormsAgreement(Gui):
    def __init__(self, width: str = '500', height: str = '200'):
        super().__init__(width, height)

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        tk.Label(frame, text="Печать договора об образовании", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W, columnspan=4,
                                                                       sticky="nsew")
        referral_select(self, frame)
        tk.Label(frame, text='Родитель/представитель: ').grid(row=10, column=0, cnf=CONF)
        self.person_select = person_select_combo(db, frame, 10, 1, 'parents')

        buttons_add_new(self, frame, 30)
        btn_ok = tk.Button(frame, text='Сформировать', bg='red', fg='white')
        btn_ok.grid(row=30, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (print_agreement(self.child_id,
                                                                   self.referral_id,
                                                                   self.person_select.get()
                                                                   )))
        next_entries(frame)
