import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.variables import LARGE_FONT, CONF_D_W, CONF
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, next_entries, select_from_db, fill_combobox, \
    fill_combobox_users
from app_view_model.functions.person_select_combo import person_select_combo
from app_view_model.functions.referral_select import referral_select
from app_view_model.print_forms.functions.print_all_forms import print_all_forms


class PrintAllForms(Gui):
    def __init__(self, width: str = '600', height: str = '400'):
        super().__init__(width, height)

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        tk.Label(frame, text="Печать документов", font=LARGE_FONT).grid(row=0, column=0, cnf=CONF_D_W,
                                                                        columnspan=4,
                                                                        sticky="nsew")
        referral_select(self, frame)
        tk.Label(frame, text='Родитель/представитель: ').grid(row=10, column=0, cnf=CONF)
        self.person_select = person_select_combo(db, frame, 10, 1, 'parents')

        tk.Label(frame, text='Документовед: ').grid(row=11, column=0, cnf=CONF)
        self.user_select = ttk.Combobox(frame, width=30)
        self.user_select.grid(row=11, column=1, columnspan=1, cnf=CONF)
        fill_combobox_users(db, self.user_select)

        tk.Label(frame, text="Отметьте какие документы нужно сформировать").grid(row=12, column=0, cnf=CONF_D_W,
                                                                                 columnspan=4,
                                                                                 sticky="nsew")
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        self.var7 = tk.IntVar()
        self.select_all_status = tk.IntVar()
        self.var7.set(1)

        self.cb1 = tk.Checkbutton(frame, text="Заявление на прием", variable=self.var1)
        self.cb2 = tk.Checkbutton(frame, text="Договор об образовании ", variable=self.var2)
        self.cb3 = tk.Checkbutton(frame, text="Согласие на обработку перс.данных", variable=self.var3)
        self.cb4 = tk.Checkbutton(frame, text="Заявление на компенсацию", variable=self.var4)
        self.cb5 = tk.Checkbutton(frame, text="Расписка о приеме компенсации", variable=self.var5)
        self.cb6 = tk.Checkbutton(frame, text="Доп. соглашение о род.плате ", variable=self.var6)
        self.cb7 = tk.Checkbutton(frame, text="Открыть документы для печати ", variable=self.var7)

        self.cb1.grid(row=20, column=0, cnf=CONF)
        self.cb2.grid(row=22, column=0, cnf=CONF)
        self.cb3.grid(row=24, column=0, cnf=CONF)
        self.cb4.grid(row=20, column=1, cnf=CONF)
        self.cb5.grid(row=22, column=1, cnf=CONF)
        self.cb6.grid(row=24, column=1, cnf=CONF)
        self.cb7.grid(row=26, column=0, cnf=CONF)
        btn_select_all = tk.Button(frame, text="Отметить/снять все", command=self.select_all)
        btn_select_all.grid(row=28, column=0, sticky='e')

        buttons_add_new(self, frame, 36)
        btn_ok = tk.Button(frame, text='Сформировать', bg='red', fg='white')
        btn_ok.grid(row=36, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (print_all_forms(self.child_id,
                                                                 self.referral_id,
                                                                 self.person_select.get(),
                                                                 self.execute_actions(),
                                                                 self.user_select.get()
                                                                 )))
        next_entries(frame)

    def execute_actions(self):
        actions = {
            "Заявление на прием": (self.var1, 1, './templates/template_application.docx', 'Заявление_на_прием'),
            "Договор об образовании": (self.var2, 2, './templates/template_agreement.docx', 'Договор'),
            "Согласие на обработку перс.данных": (
            self.var3, 3, './templates/template_consent.docx', 'Согласие_ОПД'),
            "Заявление на компенсацию": (self.var4, 4, './templates/template_compensation.docx', 'Компенсация'),
            "Расписка о приеме компенсации": (
                self.var5, 5, './templates/template_compensation_receipt.docx', 'Компенсация_расписка'),
            "Доп. соглашение о род.плате": (
                self.var6, 6, './templates/template_add_agreement.docx', 'Доп_согл_о_род_плате'),
        }

        results_for_print = {}
        for index, (action, var) in enumerate(actions.items(), start=1):
            results_for_print[index] = (int(var[0].get()), self.var7.get(), var[2], var[3])
        return results_for_print

    def select_all(self):
        if self.select_all_status.get() == 0:
            self.var1.set(1)
            self.var2.set(1)
            self.var3.set(1)
            self.var4.set(1)
            self.var5.set(1)
            # self.var6.set(1) #Доп. соглашение о род.плате
            self.select_all_status.set(1)
        else:
            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            # self.var6.set(0) #Доп. соглашение о род.плате
            self.select_all_status.set(0)
