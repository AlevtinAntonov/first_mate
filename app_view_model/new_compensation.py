import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import compensation, DB_DICT
from app_model.domain.child import Child
from app_model.variables import LARGE_FONT, CONF_D_W, CONF, label_compensation, CURRENT_YEAR, \
    CURRENT_MONTH, CURRENT_DAY, CONF_GRID_WIDTH
from app_view.gui_input_window import Gui
from app_view_model.functions.compensation_create import compensation_create
from app_view_model.functions.functions import on_validate_input, create_labels_in_grid, buttons_add_new, \
    fill_combobox, next_entries, select_date, select_from_db
from app_view_model.functions.person_select_combo import person_select_combo


class NewCompensation(Gui):
    def __init__(self, width: str = '650', height: str = '600', child: Child = None):
        super().__init__(width, height)
        self.child = child
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        vcmd = self.root.register(on_validate_input)

        tk.Label(frame, text="Компенсация родительской платы", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W,
                                                                                     columnspan=4, sticky="nsew")
        child_select_label = ttk.Label(frame, text='Выберите ФИО ребенка*', foreground='red')
        child_select_label.grid(row=2, column=0, cnf=CONF_D_W)

        create_labels_in_grid(frame, label_compensation)
        person_select = person_select_combo(db, frame, 6, 1, 'parents')
        self.data = fill_combobox(db, 'child_list_show', None, None)
        self.child_select = ttk.Combobox(frame, width=30)
        self.child_select["values"] = [person_info[0] for person_info in self.data.values()]
        self.child_select.grid(row=2, column=1, columnspan=2, sticky=tk.W)
        self.child_id = self.child_select.bind("<<ComboboxSelected>>", self.display_info)
        self.child_select.bind("<KeyRelease>", self.update_combobox_values)

        self.date_of_birth = ttk.Label(frame, text='Дата рождения: ')
        self.date_of_birth.grid(row=4, column=0, cnf=CONF_D_W)
        self.gender_label = ttk.Label(frame, text="Пол: ")
        self.gender_label.grid(row=4, column=2, cnf=CONF_D_W)
        self.number_application_compensation = ttk.Entry(frame)
        self.number_application_compensation.grid(row=7, column=1, cnf=CONF_D_W)
        self.date_application_compensation = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 8, 1,
                                                         CONF_D_W)

        self.compensation_name = select_from_db(frame, db, compensation, DB_DICT[compensation][0],
                                                DB_DICT[compensation][1], 10, 1, CONF_D_W, width=25)
        self.date_start_compensation = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 12, 1, CONF_D_W)
        self.date_end_compensation = select_date(frame, CURRENT_YEAR, 12, 31, 14, 1, CONF_D_W)

        self.add_document_name_1 = ttk.Entry(frame)
        self.add_document_name_1.grid(row=16, column=1, cnf=CONF_GRID_WIDTH)
        self.add_document_data_1 = ttk.Entry(frame)
        self.add_document_data_1.grid(row=18, column=1, cnf=CONF_GRID_WIDTH)

        self.add_document_name_2 = ttk.Entry(frame)
        self.add_document_name_2.grid(row=20, column=1, cnf=CONF_GRID_WIDTH)
        self.add_document_data_2 = ttk.Entry(frame)
        self.add_document_data_2.grid(row=22, column=1, cnf=CONF_GRID_WIDTH)

        self.add_document_name_3 = ttk.Entry(frame)
        self.add_document_name_3.grid(row=24, column=1, cnf=CONF_GRID_WIDTH)
        self.add_document_data_3 = ttk.Entry(frame)
        self.add_document_data_3.grid(row=26, column=1, cnf=CONF_GRID_WIDTH)

        self.add_document_name_4 = ttk.Entry(frame)
        self.add_document_name_4.grid(row=28, column=1, cnf=CONF_GRID_WIDTH)
        self.add_document_data_4 = ttk.Entry(frame)
        self.add_document_data_4.grid(row=30, column=1, cnf=CONF_GRID_WIDTH)

        self.add_document_name_5 = ttk.Entry(frame)
        self.add_document_name_5.grid(row=32, column=1, cnf=CONF_GRID_WIDTH)
        self.add_document_data_5 = ttk.Entry(frame)
        self.add_document_data_5.grid(row=34, column=1, cnf=CONF_GRID_WIDTH)

        self.add_document_name_6 = ttk.Entry(frame)
        self.add_document_name_6.grid(row=36, column=1, cnf=CONF_GRID_WIDTH)
        self.add_document_data_6 = ttk.Entry(frame)
        self.add_document_data_6.grid(row=38, column=1, cnf=CONF_GRID_WIDTH)

        buttons_add_new(self, frame, 40)

        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=40, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>', lambda event: (compensation_create(db,
                                                                     self.child_id,
                                                                     person_select.get(),
                                                                     self.number_application_compensation.get(),
                                                                     self.date_application_compensation.get(),
                                                                     self.date_start_compensation.get(),
                                                                     self.date_end_compensation.get(),
                                                                     self.compensation_name.get(),
                                                                     self.add_document_name_1.get(),
                                                                     self.add_document_data_1.get(),
                                                                     self.add_document_name_2.get(),
                                                                     self.add_document_data_2.get(),
                                                                     self.add_document_name_3.get(),
                                                                     self.add_document_data_3.get(),
                                                                     self.add_document_name_4.get(),
                                                                     self.add_document_data_4.get(),
                                                                     self.add_document_name_5.get(),
                                                                     self.add_document_data_5.get(),
                                                                     self.add_document_name_6.get(),
                                                                     self.add_document_data_6.get(),
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


if __name__ == '__main__':
    pass
