import tkinter as tk
from datetime import date
from tkinter import ttk, simpledialog

from tkcalendar import DateEntry

from app_model.db.db_connect import db
from app_model.db.db_query import DB_DICT
from app_model.variables import fields_names
from app_view_model.functions.functions import position_center, fill_combobox, find_id
from app_view_model.functions.update_datas import query_date_entry_child, update_user_data, query_date_entry_parents, \
    query_date_entry_movement, query_date_entry_referral, query_date_entry_compensation


class UpdateDataApp:
    def __init__(self, tab, key_name, query_read_data, update_id_query, table_name):
        self.update_id_query = update_id_query
        self.query_read_data = query_read_data
        self.tab = tab
        self.labels = []
        self.key_name = key_name
        self.table_name = table_name
        self.create_labels(self.tab)

        # Заголовок перед Combobox
        label = tk.Label(self.tab, text="Выберите ФИО :")
        label.grid(row=2, column=0, padx=10, pady=10)

        # Combobox для выбора ФИО ребенка
        self.combobox = ttk.Combobox(self.tab, width=40)
        self.combobox.grid(row=2, column=1, padx=10, pady=10)
        if (self.key_name == 'birth_certificate' or self.key_name == 'addresses' or self.key_name == 'agreement'
                or self.key_name == 'child_referral' or self.key_name == 'child_compensation'):
            self.table_name = 'child'
            label.config(text="Выберите ФИО ребенка: ")
        if self.key_name == 'addresses_parent' or self.key_name == 'parent_document':
            self.table_name = 'parents'
            label.config(text="Выберите ФИО родителя: ")

        self.refresh_combobox_data(self.table_name)
        self.combobox.bind('<<ComboboxSelected>>',
                           lambda event: self.on_combobox_select(None, self.query_read_data))

    def refresh_combobox_data(self, table_name):
        if table_name == 'child':
            query = (f"SELECT CHILD.CHILD_ID, PERSON.LAST_NAME, PERSON.FIRST_NAME, PERSON.PATRONYMIC FROM {table_name} "
                     f"JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID order by  PERSON.LAST_NAME, PERSON.FIRST_NAME, "
                     f"PERSON.PATRONYMIC;")
        if table_name == 'parents':
            query = (
                f"SELECT PERSON.person_id, PERSON.LAST_NAME, PERSON.FIRST_NAME, PERSON.PATRONYMIC FROM {table_name} "
                " JOIN PERSON on parents.PERSON_ID = person.person_id AND PERSON.is_visible = TRUE "
                " order by  PERSON.LAST_NAME, PERSON.FIRST_NAME, PERSON.PATRONYMIC;")
        with db as cur:
            cur.execute(query)
            rows = cur.fetchall()
            user_data = ["{} {} {} - {}".format(row[1], row[2], row[3], row[0]) for row in rows]
            self.combobox['values'] = user_data

    def on_combobox_select(self, event, query):
        combo_selection = self.combobox.get().split(' - ')
        if len(combo_selection) < 2:
            return
        self.child_id = combo_selection[-1]
        with db as cur:
            cur.execute(query, (self.child_id,))
            child_selected = cur.fetchone()
            if child_selected:
                for i, label in enumerate(self.labels):
                    if not isinstance(child_selected[i], int) and child_selected[i] and isinstance(child_selected[i],
                                                                                                   date):
                        label.config(text=f"{child_selected[i].strftime("%d.%m.%Y")}")
                    elif not isinstance(child_selected[i], int) and child_selected[i] and 85 < len(
                            child_selected[i]) < 171:
                        label.config(
                            text=f"{child_selected[i][:85]}\n{child_selected[i][85:170]}\n{child_selected[i][170:255]}")
                    elif not isinstance(child_selected[i], int) and child_selected[i] and 85 < len(
                            child_selected[i]) < 171:
                        label.config(text=f"{child_selected[i][:85]}\n{child_selected[i][85:]}")

                    else:
                        label.config(text=f"{child_selected[i]}")
            else:
                for i, label in enumerate(self.labels):
                    label.config(text="-")

    def create_labels(self, tab):
        for i, field in enumerate(fields_names[self.key_name]):
            tk.Label(tab, text=field[0]).grid(row=i * 2 + 3, column=0, sticky='W', padx=20)
            label = ttk.Label(tab, text="-", background="white", width=86)
            label.grid(row=i * 2 + 3, column=1, sticky='W', padx=10)

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
            top = tk.Toplevel(self.tab)
            top.withdraw()
            top.title("Выбор из справочника")
            top.geometry('300x100')
            position_center(top, 250, 100)
            top.deiconify()
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
            top = tk.Toplevel(self.tab)
            top.withdraw()
            top.title("Редактирование даты")
            top.geometry('300x100')
            position_center(top, 300, 100)
            top.deiconify()
            top.grab_set()

            new_date = DateEntry(top, foreground='black', normalforeground='black', selectforeground='red',
                                 background='white', selectmode='day', locale='ru_RU', date_pattern='dd.mm.YYYY')
            if self.key_name == 'birth_certificate':
                query_date_entry = query_date_entry_child
            elif self.key_name == 'agreement':
                query_date_entry = query_date_entry_movement
            elif self.key_name == 'child_referral':
                query_date_entry = query_date_entry_referral
            elif self.key_name == 'child_compensation':
                query_date_entry = query_date_entry_compensation
            else:
                query_date_entry = query_date_entry_parents

            with db as cur:
                query = f'SELECT {table_name}.{field} '
                query += query_date_entry
                user_data = cur.execute(query, (user_id,)).fetchone()
                default_date = user_data[0].strftime("%d.%m.%Y") if user_data[0] else '01.01.1970'
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
                update_user_data(table_name, user_id, field, new_value, self.update_id_query)
                self.refresh_combobox_data(self.table_name)
                self.on_combobox_select(None, self.query_read_data)

    def save_data_from_top(self, table_name, user_id, field, new_data, top):
        update_user_data(table_name, user_id, field, new_data, self.update_id_query)
        top.destroy()
        self.refresh_combobox_data(self.table_name)
        self.on_combobox_select(None, self.query_read_data)
