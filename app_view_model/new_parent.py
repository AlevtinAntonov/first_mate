import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import gender, DB_DICT, status, person
from app_model.domain.child import Child
from app_model.domain.parents import Parents
from app_model.variables import LARGE_FONT, label_parent_list, CONF_D_W, CONF, DEFAULT_PARENT_BORN_YEAR, \
    DEFAULT_BORN_MONTH, DEFAULT_BORN_DAY
from app_view.gui_input_window import Gui
from app_view_model.functions.document_entries import document_entries
from app_view_model.functions.functions import on_validate_input, create_labels_in_grid, next_entries, buttons_add_new, \
    select_from_db, select_date, fill_combobox, find_child, get_key, validate_combobox, check_if_exists
from app_view_model.functions.parent_create import parent_create
from app_view_model.new_address import AddressWin


class NewParent(Gui):
    def __init__(self, parents: Parents = None, width: str = '650', height: str = '500', child: Child = None,
                 comment: str = None):
        super().__init__(width, height)
        self.parents = parents
        self.child = child
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))
        self.comment = comment

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        vcmd = self.root.register(on_validate_input)

        tk.Label(frame, text="Ввод родитель/представитель", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W,
                                                                                  columnspan=4, sticky="nsew")
        child_select_label = ttk.Label(frame, text='Выберите ФИО ребенка*', foreground='red')
        child_select_label.grid(row=2, column=0, cnf=CONF_D_W)

        create_labels_in_grid(frame, label_parent_list)
        child_dict = fill_combobox(db, 'child_list', None, None)
        child_select = find_child(frame, child_dict, 2, 1, CONF_D_W)

        status_id = select_from_db(frame, db, status, DB_DICT[status][0], DB_DICT[status][1], 3, 1, CONF_D_W, width=25)

        self.last_name = ttk.Entry(frame, validate='key', validatecommand=(vcmd, "%S"))
        self.last_name.grid(row=4, column=1, cnf=CONF_D_W)
        self.first_name = ttk.Entry(frame, validate='key', validatecommand=(vcmd, "%S"))
        self.first_name.grid(row=6, column=1, cnf=CONF_D_W)
        self.patronymic = ttk.Entry(frame, validate='key', validatecommand=(vcmd, "%S"))
        self.patronymic.grid(row=8, column=1, cnf=CONF_D_W)
        gender_id = select_from_db(frame, db, gender, DB_DICT[gender][0], DB_DICT[gender][1], 10, 1, CONF_D_W, width=15)
        self.date_of_birth = select_date(frame, DEFAULT_PARENT_BORN_YEAR, DEFAULT_BORN_MONTH, DEFAULT_BORN_DAY, 10, 3,
                                         CONF_D_W)

        citizenship_id, document_type_id, document_series, document_number, document_issued_by, document_date_of_issue = (
            document_entries(
                frame, (18, 1)))
        document_date_of_expire = select_date(frame, 2100, 1, 1, 26, 1, CONF_D_W)

        phone_number = ttk.Entry(frame)
        phone_number.grid(row=30, column=1, cnf=CONF_D_W)
        email_name = ttk.Entry(frame)
        email_name.grid(row=32, column=1, cnf=CONF_D_W)
        sniils = ttk.Entry(frame)
        sniils.grid(row=34, column=1, cnf=CONF_D_W)

        buttons_add_new(self, frame, 40)

        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (
            validate_combobox(child_select, child_select_label), parent_create(db,
                                                                               get_key(
                                                                                   child_select.get(),
                                                                                   child_dict),
                                                                               status_id.get(),
                                                                               self.last_name.get(),
                                                                               self.first_name.get(),
                                                                               self.patronymic.get(),
                                                                               gender_id.get(),
                                                                               self.date_of_birth.get(),
                                                                               citizenship_id.get(),
                                                                               document_type_id.get(),
                                                                               document_series.get(),
                                                                               document_number.get(),
                                                                               document_issued_by.get(),
                                                                               document_date_of_issue.get(),
                                                                               document_date_of_expire.get(),
                                                                               phone_number.get(),
                                                                               email_name.get(),
                                                                               sniils.get(),
                                                                               )))
        next_entries(frame)

    def validate_input_btn_ok(*args):
        all_entries_filled = all(entry.get() for entry in entry_list)
        all_comboboxes_selected = all(combobox.get() for combobox in combobox_list)

        if all_entries_filled and all_comboboxes_selected:
            btn_ok.config(state=tk.NORMAL, background='red', fg='white')
        else:
            btn_ok.config(state=tk.DISABLED, background='LightGray', fg='white')

    def create_address_window(self):
        self.person_id = check_if_exists(db, person, self.last_name.get(), self.first_name.get(), self.patronymic.get(),
                                         self.date_of_birth.get())
        print(f'{self.person_id=}')
        if self.person_id:
            AddressWin(self.person_id)


if __name__ == '__main__':
    pass
