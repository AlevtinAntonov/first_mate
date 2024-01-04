import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.variables import LARGE_FONT, CONF_D_W, CONF
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, next_entries
from app_view_model.functions.referral_select import referral_select
from app_view_model.print_forms.functions.print_application_form import print_application


class PrintApplication(Gui):
    def __init__(self, width: str = '650', height: str = '400'):
        super().__init__(width, height)

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        tk.Label(frame, text="Печать заявления", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W, columnspan=4,
                                                                       sticky="nsew")
        referral_select(self, frame)

        buttons_add_new(self, frame, 30)
        btn_ok = tk.Button(frame, text='Печать заявления', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (print_application(db, self.child_id,
                                                                   self.referral_id
                                                                   )))
        next_entries(frame)
