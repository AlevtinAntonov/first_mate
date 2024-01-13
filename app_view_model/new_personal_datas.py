import tkinter as tk
from datetime import date
from tkinter import ttk, simpledialog
from tkinter.simpledialog import Dialog

from tkcalendar import DateEntry

from app_model.db.db_connect import db
from app_model.db.db_query import query_read_birth_certificate, DB_DICT
from app_model.variables import LARGE_FONT, CONF, fields_names
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import position_center, select_from_db, fill_combobox, current_timestamp, \
    find_id
from app_view_model.functions.tab_address_datas import show_address_datas
from app_view_model.functions.tab_agreement_datas import show_agreement_datas
from app_view_model.functions.tab_compensation import show_compensation_labels
from app_view_model.functions.tab_family import show_family_labels
from app_view_model.functions.tab_personal_datas import show_child_datas
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
        style.configure('TNotebook.Tab', font=("Verdana", 11), padding=[5, 5])
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill="both")

        self.tab_birth_certificate = ttk.Frame(tab_control)
        tab_referral = ttk.Frame(tab_control)
        tab_personal_datas = ttk.Frame(tab_control)
        tab_compensation = ttk.Frame(tab_control)
        tab_family = ttk.Frame(tab_control)

        # Создание рамок внутри вкладки "Личное дело"
        frame_birth_certificate = ttk.Frame(tab_personal_datas)
        frame_birth_certificate.pack(side="left", expand=True)

        frame_address = ttk.Frame(tab_personal_datas)
        frame_address.pack(side="left", expand=True)

        frame_contract_data = ttk.Frame(tab_personal_datas)
        # frame_contract_data.grid(row=0, column=1, sticky="nsew")
        frame_contract_data.pack(side="left", expand=True)

        tab_control.add(self.tab_birth_certificate, text='Св-во о рождении')
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
        self.key_name = 'birth_certificate'
        self.create_labels(self.tab_birth_certificate)

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

    def update_user_data(self, table_name, child_id, field, new_value):
        with db as cur:

            cur.execute(f'SELECT person.person_id, gender.gender_id, document.document_id FROM CHILD '
                        f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                        f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                        f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
                        f'WHERE CHILD.CHILD_ID = ?;', (child_id,))
            modify_date = f", date_of_modify = '{current_timestamp()}'"
            if table_name == 'person':
                data_id = cur.fetchone()[0]
            elif table_name == 'gender':
                data_id = cur.fetchone()[1]
                modify_date = ''
            elif table_name == 'document':
                data_id = cur.fetchone()[2]
            print(f'UPDATE {table_name} SET {field} = ? {modify_date} WHERE {table_name}_id = ?', (new_value, data_id))
            cur.execute(f'UPDATE {table_name} SET {field} = ? {modify_date} WHERE {table_name}_id = ?',
                        (new_value, data_id))

    def on_combobox_select(self, event, table_name):
        combo_selection = self.combobox.get().split(' - ')
        if len(combo_selection) < 2:
            return
        self.child_id = combo_selection[-1]
        with db as cur:
            cur.execute(query_read_birth_certificate, (self.child_id,))
            child_selected = cur.fetchone()
            if child_selected:
                for i, label in enumerate(self.labels):
                    if child_selected[i] and isinstance(child_selected[i], date):
                        label.config(text=f"{child_selected[i].strftime("%d.%m.%Y")}")
                    elif child_selected[i] and 85 < len(child_selected[i]) < 171:
                        label.config(
                            text=f"{child_selected[i][:85]}\n{child_selected[i][85:170]}\n{child_selected[i][170:255]}")
                    elif child_selected[i] and 85 < len(child_selected[i]) < 171:
                        label.config(text=f"{child_selected[i][:85]}\n{child_selected[i][85:]}")

                    else:
                        label.config(text=f"{child_selected[i]}")

    def create_labels(self, tab):
        for i, field in enumerate(fields_names[self.key_name]):
            tk.Label(tab, text=field[0]).grid(row=i * 2 + 2, column=0, sticky='W', padx=20)
            label = ttk.Label(tab, text="-", background="white", width=86)
            label.grid(row=i * 2 + 2, column=1, sticky='W', padx=10)

            # Use default argument for lambda function to capture the current value of i
            label.bind("<Double-1>",
                       lambda event, idx=i, table_name=field[3], table_dict=field[4], field=field[1],
                              field_type=field[2], label=label: self.on_label_double_click(event, idx, table_name,
                                                                                           table_dict, field,
                                                                                           field_type, label))

            self.labels.append(label)

    def on_label_double_click(self, event, idx, table_name, table_dict, field, field_type, label):
        user_id = self.combobox.get().split(' - ')[-1]
        if field_type == 'Combobox':
            top = tk.Toplevel(self.tab_birth_certificate)
            top.title("Выбор из справочника")
            top.geometry('300x100')
            position_center(top, 250, 100)
            top.grab_set()

            new_data = tk.StringVar()
            new_data.set(label.cget("text"))
            value_from_db = [v for v in
                             fill_combobox(db, table_dict, DB_DICT[table_dict][0], DB_DICT[table_dict][1]).values()]

            combobox = ttk.Combobox(top, textvariable=new_data, values=value_from_db, width=30)
            combobox.pack(pady=10)

            button = ttk.Button(top, text="Сохранить",
                                command=lambda: self.save_data_from_top(table_name, user_id, field,
                                                                        find_id(db, table_dict, DB_DICT[table_dict][0],
                                                                                DB_DICT[table_dict][1], new_data.get()),
                                                                        top))
            button.pack()
        elif field_type == 'DateEntry':
            # Окно для изменения даты
            top = tk.Toplevel(self.tab_birth_certificate)
            top.title("Редактирование даты")
            top.geometry('300x100')
            position_center(top, 300, 100)
            top.grab_set()

            new_date = DateEntry(top, foreground='black', normalforeground='black', selectforeground='red',
                                 background='white', selectmode='day', locale='ru_RU', date_pattern='dd.mm.YYYY')
            with db as cur:
                user_data = cur.execute(f'SELECT {table_name}.{field} FROM CHILD '
                                        f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
                                        f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
                                        f'WHERE CHILD.CHILD_ID = ?;', (user_id,)).fetchone()
                default_date = user_data[0].strftime("%d.%m.%Y") if user_data else ''
                new_date.set_date(default_date)
                new_date.pack(pady=10)

            button = ttk.Button(top, text="Сохранить",
                                command=lambda: self.save_data_from_top(table_name, user_id, field, new_date.get(),
                                                                         top))
            button.pack()

        else:
            new_value = simpledialog.askstring("Редактирование",
                                               f"{' ' * 40}Введите новое значение{' ' * 40}",
                                               initialvalue=label.cget("text"))
            if new_value:
                label.config(text=new_value)
                self.update_user_data(table_name, user_id, field, new_value)
                print(table_name)
                self.refresh_combobox_data('child')
                self.on_combobox_select(None, 'child')

    def save_data_from_top(self, table_name, user_id, field, new_data, top):
        self.update_user_data(table_name, user_id, field, new_data)
        top.destroy()
        self.refresh_combobox_data('child')
        self.on_combobox_select(None, 'child')

