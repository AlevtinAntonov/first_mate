import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.db.db_query import query_insert_into, organization, DB_DICT, get_total_table_records
from app_model.variables import CONF_GRID_WIDTH, LARGE_FONT
from app_view.gui_input_window import Gui
from app_view.referral_labels import OrganizationLabels
from app_view_model.functions.functions import next_entries, save_access, clear_text


class NewPersonalDatas(Gui):
    def __init__(self, width: str = '800', height: str = '600'):
        super().__init__(width, height)
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))


    def create_widgets(self):
        # tk.Label(self.root, text="Личные дела воспитанников", font=LARGE_FONT).pack()
        self.child_name_var = tk.StringVar()
        # label = tk.Label(self.root, text="Выберите ФИО")
        # label.pack(side="left")
        # child_name_combobox = ttk.Combobox(self.root, textvariable=self.child_name_var,
        #                                    values=["Child 1", "Child 2", "Child 3"])
        # child_name_combobox.pack()
        # Frame для размещения заголовка окна
        title_frame = tk.Frame(self.root)
        title_frame.pack()

        # Заголовок окна
        title_label = tk.Label(title_frame, text="Личные дела воспитанников", font=LARGE_FONT)
        title_label.pack()

        # Frame для размещения метки и комбобокса в одной строке
        combobox_frame = tk.Frame(self.root)
        combobox_frame.pack()

        # Заголовок перед комбобоксом
        label = tk.Label(combobox_frame, text="Выберите ФИО ребенка:")
        label.pack(side="left", padx=10, pady=10)

        # Combobox для выбора ФИО ребенка
        child_combobox = ttk.Combobox(combobox_frame, textvariable=self.child_name_var,
                                      values=["Child 1", "Child 2", "Child 3"], width=50)
        child_combobox.pack(side="left", padx=10, pady=10)
        # Создание вкладок
        self.tab_control = ttk.Notebook(self.root)
        self.tab_referral = ttk.Frame(self.tab_control)
        self.tab_personal_datas = ttk.Frame(self.tab_control)
        self.tab_compensation = ttk.Frame(self.tab_control)
        self.tab_family = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_personal_datas, text='Личное дело')
        self.tab_control.add(self.tab_compensation, text='Компенсация')
        self.tab_control.add(self.tab_family, text='Семья')
        self.tab_control.add(self.tab_referral, text='Направление')
        self.tab_control.pack(expand=1, fill="both")

        for tab in [self.tab_referral, self.tab_personal_datas, self.tab_compensation, self.tab_family]:
            self.cancel_button = tk.Button(tab, text="Закрыть", bg='DarkSlateGray', fg='white',
                                           command=self.return_to_start_page)
            self.cancel_button.grid(row=60, column=2)

