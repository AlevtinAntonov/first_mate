import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.variables import LARGE_FONT, CONF_D_W, CONF
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, next_entries
from app_view_model.functions.person_select_combo import person_select_combo
from app_view_model.functions.referral_select import referral_select
from app_view_model.print_forms.functions.print_agreement_form import print_agreement
from app_view_model.print_forms.functions.print_application_form import print_application


class PrintFormsBase(Gui):
    pass
    # def __init__(self, width: str = '500', height: str = '200', print_function_name=None, form_name=None, form_label=None):
    #     super().__init__(width, height)
    #     self.form_label = form_label
    #     self.form_name = form_name
    #     self.print_function_name = print_function_name
    #     # match self.form_name:
    #     #     case 'application':
    #     #         self.print_function_name = 'print_application'
    #     #         self.form_label = "Печать заявления на прием"
    #     #     case 'agreement':
    #     #         self.print_function_name = 'print_agreement'
    #     #         self.form_label = "Печать договора об образовании "
    #     #     case 'consent':
    #     #         self.print_function_name = 'print_consent'
    #     #         self.form_label = "Печать согласие на обработку ПД"
    #     #     case 'compensation':
    #     #         self.print_function_name = 'print_compensation'
    #     #         self.form_label = "Печать заявления на компенсацию"
    #     #     case 'compensation_receipt':
    #     #         self.print_function_name = 'print_compensation_receipt'
    #     #         self.form_label = "Печать расписка о приеме на компенсацию"
    #     #     case 'add_agreement':
    #     #         self.print_function_name = 'print_add_agreement'
    #     #         self.form_label = "Печать дополнит. соглашение"
    #     #     case 'export':
    #     #         self.print_function_name = 'print_export'
    #     #         self.form_label = "Экспорт данных в эксель"
    #     #     case '_':
    #     #         self.print_function_name = 'print_all'
    #     #         self.form_label = "Печать комплекта по приему"
    #
    # def create_widgets(self):
    #     print(f'{print_function_name=}, {self.form_name}')
    #     frame = ttk.Frame(self.root)
    #     frame.pack(fill=BOTH, expand=1)
    #     tk.Label(frame, text=f'ffffffffffffffff', font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W, columnspan=4,
    #                                                                     sticky="nsew")
    #     referral_select(self, frame)
    #     tk.Label(frame, text='Родитель/представитель: ').grid(row=10, column=0, cnf=CONF)
    #     self.person_select = person_select_combo(db, frame, 10, 1, 'parents')
    #
    #     buttons_add_new(self, frame, 30)
    #     btn_ok = tk.Button(frame, text='Сформировать', bg='red', fg='white')
    #     btn_ok.grid(row=30, column=3, cnf=CONF)
    #     btn_ok.bind('<Button-1>', lambda event: (print_application(self.child_id,
    #                                                                self.referral_id,
    #                                                                self.person_select.get()
    #                                                                )))
    #     next_entries(frame)
