import tkinter as tk
from datetime import date
from tkinter import ttk, simpledialog

from tkcalendar import DateEntry

from app_model.db.db_connect import db
from app_model.db.db_query import query_read_birth_certificate
from app_model.variables import LARGE_FONT, CONF, fields_names
from app_view.gui_input_window import Gui
from app_view_model.functions.tab_address_datas import show_address_datas
from app_view_model.functions.tab_agreement_datas import show_agreement_datas
from app_view_model.functions.tab_compensation import show_compensation_labels
from app_view_model.functions.tab_family import show_family_labels
from app_view_model.functions.tab_personal_datas import show_child_datas
from app_view_model.functions.tab_referral import show_referral


class NewPersonalDatas(Gui):
    def __init__(self, width: str = '850', height: str = '600'):
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
        self.combobox_frame = tk.Frame(self.root)
        self.combobox_frame.pack()

        # Заголовок перед Combobox
        label = tk.Label(self.combobox_frame, text="Выберите ФИО ребенка:")
        label.pack(side="left", padx=10, pady=10)

        # Combobox для выбора ФИО ребенка
        self.combobox = ttk.Combobox(self.combobox_frame, width=30)
        self.combobox.pack(side="left", padx=10, pady=10)
        self.refresh_combobox_data('child')
        self.combobox.bind('<<ComboboxSelected>>', lambda event: self.on_combobox_select(None, 'child'))

        # Создание вкладок
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Verdana", 11))
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill="both")

        tab_birth_certificate = ttk.Frame(tab_control)
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

        tab_control.add(tab_birth_certificate, text='Св-во о рождении')
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

        # вкладка tab_birth_certificate
        self.labels = []
        self.create_labels(tab_birth_certificate, fields_names, 'birth_certificate')

        show_referral(tab_referral)
        show_compensation_labels(tab_compensation)
        show_family_labels(tab_family)

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        self.close_button = tk.Button(buttons_frame, text="Закрыть", bg='DarkSlateGray', fg='white',
                                      command=self.return_to_start_page)
        self.close_button.pack(padx=10, pady=10)

    def refresh_combobox_data(self, table_name):
        if table_name == 'child':
            query = (f"SELECT CHILD.CHILD_ID, PERSON.LAST_NAME, PERSON.FIRST_NAME, PERSON.PATRONYMIC FROM {table_name} "
                     f"JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID ")
        with db as cur:
            cur.execute(query)
            rows = cur.fetchall()
            user_data = ["{} {} {} - {}".format(row[1], row[2], row[3], row[0]) for row in rows]
            self.combobox['values'] = user_data

    def update_user_data(self, table_name, user_id, field, new_value):
        with db as cur:
            cur.execute(f'UPDATE {table_name} SET {field} = ? WHERE id = ?', (new_value, user_id))

    def on_combobox_select(self, event, table_name):
        combo_selection = self.combobox.get().split(' - ')
        if len(combo_selection) < 2:
            return
        user_id = combo_selection[-1]
        with db as cur:
            cur.execute(query_read_birth_certificate, (user_id,))
            user = cur.fetchone()
            if user:
                for i, label in enumerate(self.labels):
                    if user[i] and isinstance(user[i], date):
                        label.config(text=f"{user[i].strftime("%d.%m.%Y")}")
                    elif user[i] and len(user[i]) > 100:
                        label.config(text=f"{user[i][:95]}\n{user[i][95:]}")

                    else:
                        label.config(text=f"{user[i]}")

    def create_labels(self, tab, fields_name, key_name):
        for i, field in enumerate(fields_name[key_name]):
            tk.Label(tab, text=field[0]).grid(row=i * 2 + 2, column=0, sticky='W')
            label = ttk.Label(tab, text="-", background="white", width=100)
            label.grid(row=i * 2 + 2, column=1, sticky='W')

            # Use default argument for lambda function to capture the current value of i
            label.bind("<Double-1>",
                       lambda event, idx=i, table_name=field[3], field=field[1], field_type=field[2],
                              label=label: self.on_label_double_click(event, idx, table_name, field, field_type,
                                                                      label))

            self.labels.append(label)

    def on_label_double_click(self, event, idx, table_name, field, field_type, label):
        # user_id = self.combobox.get().split(' - ')[-1]
        user_id = 31
        if field_type == 'Combobox':
            top = tk.Toplevel(self.tab)
            top.title("Выбор из справочника")

            new_department = tk.StringVar()
            new_department.set(label.cget("text"))

            combobox = ttk.Combobox(top, textvariable=new_department, values=["Первый", "Второй", "Третий"])
            combobox.pack(pady=10)

            button = ttk.Button(top, text="Сохранить",
                                command=lambda: self.save_department(table_name, user_id, field, new_department.get(),
                                                                     top))
            button.pack()
        elif field_type == 'DateEntry':
            # Окно для изменения даты
            top = tk.Toplevel(self.tab)
            top.title("Редактирование даты")

            new_date = DateEntry(top, width=12, background='dark', foreground='white', borderwidth=2)
            with db as cur:
                user_data = cur.execute(f"SELECT {field} FROM {table_name} WHERE id = ?", (user_id,)).fetchone()
                default_date = user_data[0] if user_data else ''
                new_date.set_date(default_date)
                new_date.pack(pady=10)

            button = ttk.Button(top, text="Сохранить",
                                command=lambda: self.save_date_of_birth(table_name, user_id, field, new_date.get(),
                                                                        top))
            button.pack()
        else:
            new_value = simpledialog.askstring("Редактирование", f"Введите новое значение",
                                               initialvalue=label.cget("text"))
            if new_value:
                label.config(text=new_value)
                self.update_user_data(table_name, user_id, field, new_value)
                self.refresh_combobox_data(table_name)
                self.on_combobox_select(None, table_name)

    def save_department(self, table_name, user_id, field, new_department, top):
        self.update_user_data(table_name, user_id, field, new_department)
        top.destroy()
        self.refresh_combobox_data(table_name)
        self.on_combobox_select(None, table_name)

    def save_date_of_birth(self, table_name, user_id, field, new_date, top):
        self.update_user_data(table_name, user_id, field, new_date)
        top.destroy()
        self.refresh_combobox_data(table_name)
        self.on_combobox_select(None, table_name)

    # def display_info(self, *args):
    #     selected_name = self.child_select.get()
    #     for person, person_info in self.data.items():
    #         if person_info[0] == selected_name:
    #             self.date_of_birth.config(text="Дата рождения: " + person_info[1].strftime("%d.%m.%Y"))
    #             self.gender_label.config(text="Пол: " + person_info[2])
    #             self.child_id = person
    #             return self.child_id
    #
    # def update_combobox_values(self, event=None):
    #     search_text = self.child_select.get()
    #     matching_values = [person_info[0] for person_info in self.data.values() if
    #                        search_text.lower() in person_info[0].lower()]
    #     self.child_select["values"] = matching_values
