import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.variables import LARGE_FONT, CONF
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import create_labels_in_grid, fill_combobox
from app_view_model.functions.tab_address_datas import show_address_datas
from app_view_model.functions.tab_agreement_datas import show_agreement_datas
from app_view_model.functions.tab_compensation import show_compensation_labels
from app_view_model.functions.tab_family import show_family_labels
from app_view_model.functions.tab_personal_datas import show_child_datas
from app_view_model.functions.tab_referral import show_referral


class NewPersonalDatas(Gui):
    def __init__(self, width: str = '1400', height: str = '600'):
        super().__init__(width, height)
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        self.child_name_var = tk.StringVar()
        # Frame для размещения заголовка окна
        title_frame = tk.Frame(self.root)
        title_frame.pack()

        # Заголовок окна
        title_label = tk.Label(title_frame, text="Личные дела воспитанников", font=LARGE_FONT)
        title_label.pack()

        # Frame для размещения Label и Combobox в одной строке
        combobox_frame = tk.Frame(self.root)
        combobox_frame.pack()

        # Заголовок перед Combobox
        label = tk.Label(combobox_frame, text="Выберите ФИО ребенка:")
        label.pack(side="left", padx=10, pady=10)

        # Combobox для выбора ФИО ребенка
        # child_combobox = ttk.Combobox(combobox_frame, textvariable=self.child_name_var,
        #                               values=["Child 1", "Child 2", "Child 3"], width=50)
        # child_combobox.pack(side="left", padx=10, pady=10)

        self.data = fill_combobox(db, 'child_list_show', None, None)
        self.child_select = ttk.Combobox(combobox_frame, width=50)
        self.child_select["values"] = [person_info[0] for person_info in self.data.values()]
        self.child_select.pack(side="left", padx=10, pady=10)
        # self.child_select.grid(row=2, column=1, columnspan=2, sticky=tk.W)
        self.child_id = self.child_select.bind("<<ComboboxSelected>>", self.display_info)
        self.child_select.bind("<KeyRelease>", self.update_combobox_values)



        # Создание вкладок
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Verdana", 11))
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill="both")

        tab_referral = ttk.Frame(tab_control)
        tab_personal_datas = ttk.Frame(tab_control)
        tab_compensation = ttk.Frame(tab_control)
        tab_family = ttk.Frame(tab_control)

        # Создание рамок внутри вкладки "Личное дело"
        frame_birth_certificate = ttk.Frame(tab_personal_datas)
        # frame_birth_certificate.grid(row=0, column=0, sticky="nsew")
        frame_birth_certificate.pack(side="left", expand=True)


        frame_address = ttk.Frame(tab_personal_datas)
        # frame_address.grid(row=0, column=2, columnspan=2, sticky="nsew")
        frame_address.pack(side="left", expand=True)

        frame_contract_data = ttk.Frame(tab_personal_datas)
        # frame_contract_data.grid(row=0, column=1, sticky="nsew")
        frame_contract_data.pack(side="left", expand=True)

        tab_control.add(tab_personal_datas, text='Личное дело')
        tab_control.add(tab_compensation, text='Компенсация')
        tab_control.add(tab_family, text='Семья')
        tab_control.add(tab_referral, text='Направление')

        # Добавление заголовков над рамками
        label_birth_certificate = ttk.Label(frame_birth_certificate, text="Свидетельство о рождении", font=CONF)
        label_birth_certificate.grid(row=0, column=0, columnspan=2)
        show_child_datas(frame_birth_certificate)


        label_contract_data = ttk.Label(frame_contract_data, text="Данные договора", font=CONF)
        label_contract_data.grid(row=0, column=0, columnspan=2)
        show_agreement_datas(frame_contract_data)

        label_address = ttk.Label(frame_address, text="Адрес", font=CONF)
        label_address.grid(row=0, column=0, columnspan=2)
        show_address_datas(frame_address)



        show_referral(tab_referral)
        show_compensation_labels(tab_compensation)
        show_family_labels(tab_family)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        self.close_button = tk.Button(buttons_frame, text="Закрыть", bg='DarkSlateGray', fg='white',
                                      command=self.return_to_start_page)
        self.close_button.pack(padx=10, pady=10)

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