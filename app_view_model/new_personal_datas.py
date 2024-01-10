import tkinter as tk
from tkinter import ttk

from app_model.variables import LARGE_FONT
from app_view.gui_input_window import Gui
from app_view_model.functions.tab_compensation import show_compensation_labels
from app_view_model.functions.tab_family import show_family_labels
from app_view_model.functions.tab_personal_datas import show_child_labels
from app_view_model.functions.tab_referral import show_referral


class NewPersonalDatas(Gui):
    def __init__(self, width: str = '800', height: str = '600'):
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
        style = ttk.Style()
        # Настройка шрифта для текста вкладки
        style.configure('TNotebook.Tab', font=("Verdana", 11))
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill="both")

        tab_referral = ttk.Frame(tab_control)
        tab_personal_datas = ttk.Frame(tab_control)
        tab_compensation = ttk.Frame(tab_control)
        tab_family = ttk.Frame(tab_control)

        # Создание рамок внутри вкладки "Личное дело"
        frame_birth_certificate = ttk.Frame(tab_personal_datas)
        # frame_birth_certificate.pack(side="left", fill="both", expand=True)
        frame_birth_certificate.grid(row=0, column=0, sticky="nsew")

        frame_contract_data = ttk.Frame(tab_personal_datas)
        # frame_contract_data.pack(side="left", fill="both", expand=True)
        frame_contract_data.grid(row=0, column=1, sticky="nsew")
        frame_address = ttk.Frame(tab_personal_datas)
        # frame_address.pack(side="left", fill="both", expand=True)
        frame_address.grid(row=1, column=0, columnspan=2, sticky="nsew")

        tab_control.add(tab_personal_datas, text='Личное дело')
        tab_control.add(tab_compensation, text='Компенсация')
        tab_control.add(tab_family, text='Семья')
        tab_control.add(tab_referral, text='Направление')

        # for tab in [tab_referral, tab_personal_datas, tab_compensation, tab_family]:
        #     self.cancel_button = tk.Button(tab, text="Закрыть", bg='DarkSlateGray', fg='white',
        #                                    command=self.return_to_start_page)
        #     self.cancel_button.grid(row=60, column=2)

        # Добавление заголовков над рамками
        label_birth_certificate = tk.Label(frame_birth_certificate, text="Свидетельство о рождении")
        label_birth_certificate.grid(row=0, column=0, columnspan=2)
        show_child_labels(frame_birth_certificate)

        label_contract_data = tk.Label(frame_contract_data, text="Данные договора")
        label_contract_data.grid(row=0, column=0, columnspan=2)

        label_address = tk.Label(frame_address, text="Адрес")
        label_address.grid(row=0, column=0, columnspan=2)

        label_street = tk.Label(frame_address, text="Улица")
        label_street.grid(row=2, column=0)

        # Метка "Дом" в 1 ряду, колонка 1
        label_house = tk.Label(frame_address, text="Дом")
        label_house.grid(row=2, column=1)

        # Метка "Квартира" в 2 ряду, колонка 1
        label_apartment = tk.Label(frame_address, text="Квартира")
        label_apartment.grid(row=4, column=1)
        # label_street.pack(side="left", padx=5, pady=5)
        # label_house.pack(side="left", padx=5, pady=5)
        # label_apartment.pack(side="left", padx=5, pady=5)
        show_referral(tab_referral)
        show_compensation_labels(tab_compensation)
        show_family_labels(tab_family)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        self.close_button = tk.Button(buttons_frame, text="Закрыть", bg='DarkSlateGray', fg='white',
                                      command=self.return_to_start_page)
        self.close_button.pack(padx=10, pady=10)
