import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import query_child_person_id, person
from app_model.domain.child import Child
from app_model.variables import LARGE_FONT, CONF_D_W, label_child_list, CONF
from app_view.gui_input_window import Gui
from app_view_model.address_toplevel import AddressWindow
from app_view_model.functions.child_bd_certificate_create import child_db_cert_create
from app_view_model.functions.document_entries import document_entries
from app_view_model.functions.functions import on_validate_input, create_labels_in_grid, buttons_add_new, \
    fill_combobox, validate_combobox, next_entries, check_if_exists
from app_view_model.new_address import AddressWin


class NewChild(Gui):
    def __init__(self, width: str = '650', height: str = '400', child: Child = None, comment: str = None):
        super().__init__(width, height)
        self.child = child
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))
        self.comment = comment

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        vcmd = self.root.register(on_validate_input)

        tk.Label(frame, text="Ввод свидетельства о рождении", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W,
                                                                                    columnspan=4, sticky="nsew")
        child_select_label = ttk.Label(frame, text='Выберите ФИО ребенка*', foreground='red')
        child_select_label.grid(row=2, column=0, cnf=CONF_D_W)

        create_labels_in_grid(frame, label_child_list)
        self.data = fill_combobox(db, 'child_list_show', None, None)
        self.child_select = ttk.Combobox(frame, width=30)
        self.child_select["values"] = [person_info[0] for person_info in self.data.values()]
        self.child_select.grid(row=2, column=1, columnspan=2, sticky=tk.W)
        self.child_id = self.child_select.bind("<<ComboboxSelected>>", self.display_info)
        self.child_select.bind("<KeyRelease>", self.update_combobox_values)

        self.date_of_birth = ttk.Label(frame, text='Дата рождения: ')
        self.date_of_birth.grid(row=8, column=0, cnf=CONF_D_W)
        self.gender_label = ttk.Label(frame, text="Пол: ")
        self.gender_label.grid(row=8, column=2, cnf=CONF_D_W)
        place_of_birth = ttk.Entry(frame)
        place_of_birth.grid(row=18, column=1, cnf=CONF_D_W, columnspan=3, sticky="ew")

        document_assembly_record = ttk.Entry(frame)
        document_assembly_record.grid(row=20, column=1, cnf=CONF_D_W)
        citizenship_id, document_type_id, document_series, document_number, document_issued_by, document_date_of_issue = (
            document_entries(frame, (22, 1)))
        sniils = ttk.Entry(frame)
        sniils.grid(row=30, column=1, cnf=CONF_D_W)

        # tk.Button(frame, text="Добавить адрес", bg='LimeGreen', fg='white',
        #           command=lambda: self.create_address_window(), width=25, height=1).grid(row=48, column=1)

        print_test = f'{self.child_id=} {citizenship_id.get()=} {document_type_id.get()=}'

        btn_test = tk.Button(frame, text='Test', command=lambda: print(print_test))
        btn_test.grid(row=41, column=0)

        buttons_add_new(self, frame, 40)
        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (
            validate_combobox(self.child_select, child_select_label), child_db_cert_create(db,
                                                                                           self.child_id,
                                                                                           citizenship_id.get(),
                                                                                           sniils.get(),
                                                                                           document_type_id.get(),
                                                                                           place_of_birth.get(),
                                                                                           document_series.get(),
                                                                                           document_number.get(),
                                                                                           document_issued_by.get(),
                                                                                           document_date_of_issue.get(),
                                                                                           document_assembly_record.get(),
                                                                                           )))
        next_entries(frame)

    def display_info(self, *args):
        selected_name = self.child_select.get()
        for person, person_info in self.data.items():
            if person_info[0] == selected_name:
                self.date_of_birth.config(text="Дата рождения: " + person_info[1].strftime("%d.%m.%Y"))
                self.gender_label.config(text="Пол: " + person_info[2])
                self.child_id = person
                return self.child_id

    def update_combobox_values(self, event=None):
        search_text = self.child_select.get()
        matching_values = [person_info[0] for person_info in self.data.values() if
                           search_text.lower() in person_info[0].lower()]
        self.child_select["values"] = matching_values

    # def create_address_window(self):
    #     if isinstance(self.child_id, int):
    #         with db as cur:
    #             cur.execute(query_child_person_id, (self.child_id,))
    #             self.person_id = cur.fetchone()[0]
    #         AddressWin(self.person_id)
    # def create_address_window(self):
    #     self.person_id = check_if_exists(db, person, self.last_name.get(), self.first_name.get(), self.patronymic.get(),
    #                                      self.date_of_birth.get())
    #     print(f'{self.person_id=}')
    #     if self.person_id:
    #         AddressWin(self.person_id)

if __name__ == '__main__':
    pass
