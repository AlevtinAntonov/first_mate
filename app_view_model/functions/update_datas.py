import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

from tkcalendar import DateEntry

from app_model.db.db_connect import db
from app_model.db.db_query import query_read_birth_certificate
from app_model.variables import fields_names


class UpdateDataApp:
    def __init__(self, tab, child_id):
        # self.conn = sqlite3.connect('test_db.db')
        # self.cursor = self.conn.cursor()
        # self.root = tk.Tk()
        # self.root.title("Пользователи")
        self.child_id = child_id = 31
        self.tab = tab
        # self.combobox = ttk.Combobox(self.tab, width=30)
        # self.combobox.grid(row=0, column=0, columnspan=2)
        # self.refresh_combobox_data('persons')
        # self.combobox.bind('<<ComboboxSelected>>', lambda event: self.on_combobox_select(None, 'persons'))
        self.key_name = 'birth_certificate'
        self.fields_names = fields_names

        self.labels = []
        self.create_labels()
        # self.root.mainloop()

    def refresh_combobox_data(self, table_name):
        with db as cur:
            cur.execute(f"SELECT id, last_name, first_name, patronymic FROM {table_name}")
            rows = cur.fetchall()
            user_data = ["{} {} {} - {}".format(row[1], row[2], row[3], row[0]) for row in rows]
            self.combobox['values'] = user_data

    def update_user_data(self, table_name, user_id, field, new_value):
        with db as cur:
            cur.execute(f'UPDATE {table_name} SET {field} = ? WHERE id = ?', (new_value, user_id))

    def on_combobox_select(self, event, table_name):
        # combo_selection = self.combobox.get().split(' - ')
        # if len(combo_selection) < 2:
        #     return
        # user_id = combo_selection[-1]
        user_id = self.child_id
        user_id = 31
        with db as cur:
            cur.execute(query_read_birth_certificate, (user_id,))
            # cur.execute(f"SELECT * FROM {table_name} WHERE id = ?", (user_id,))
            user = cur.fetchone()
            if user:
                for i, label in enumerate(self.labels):
                    label.config(text=f"{user[i + 1]}")

    def create_labels(self):
        for i, field in enumerate(self.fields_names[self.key_name]):
            tk.Label(self.tab, text=field[0]).grid(row=i * 2 + 2, column=0, sticky='W')
            label = ttk.Label(self.tab, text="-", background="white", width=20)
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
                                command=lambda: self.save_department(table_name, user_id, field, new_department.get(), top))
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
                                command=lambda: self.save_date_of_birth(table_name, user_id, field, new_date.get(), top))
            button.pack()
        else:
            new_value = simpledialog.askstring("Редактирование", f"Введите новое значение",
                                               initialvalue=label.cget("text"))
            if new_value:
                label.config(text=new_value)
                self.update_user_data(table_name, user_id, field, new_value)
                # self.refresh_combobox_data(table_name)
                self.on_combobox_select(None, table_name)

    def save_department(self, table_name, user_id, field, new_department, top):
        self.update_user_data(table_name, user_id, field, new_department)
        top.destroy()
        # self.refresh_combobox_data(table_name)
        self.on_combobox_select(None, table_name)

    def save_date_of_birth(self, table_name, user_id, field, new_date, top):
        self.update_user_data(table_name, user_id, field, new_date)
        top.destroy()
        # self.refresh_combobox_data(table_name)
        self.on_combobox_select(None, table_name)


if __name__ == "__main__":
    UpdateDataApp()
