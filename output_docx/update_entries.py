import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

from tkcalendar import DateEntry


class UserDataApp:
    def __init__(self):
        self.conn = sqlite3.connect('test_db.db')
        self.cursor = self.conn.cursor()
        self.root = tk.Tk()
        self.root.title("Пользователи")
        self.combobox = ttk.Combobox(self.root, width=30)
        self.combobox.grid(row=0, column=0, columnspan=2)
        self.refresh_combobox_data('persons')
        self.combobox.bind('<<ComboboxSelected>>', lambda event: self.on_combobox_select(None, 'person'))
        self.key_name = 'person'
        self.fields_names = {
            'person': (("Фамилия", 'last_name', 0, 'person'),
                          ("Имя", 'first_name', 0, 'person'),
                          ("Отчество", 'patronymic', 0, 'person'),
                          ("Пол", 'gender_id', 'Combobox', 'person'),
                          ("Дата рождения", 'date_of_birth', 'DateEntry', 'person'),
                          ("Гражданство", 'citizenship_id', 'Combobox', 'person'),
                          ("Тип документа", 'document_type_id', 'Combobox', 'person'),
                          ("Место рождения", 'place_of_birth', 0, 'document'),
                          ('№ актовой записи (для Св-ва о рожд.)', 'document_assembly_record', 0, 'document'),
                          ("Серия", 'document_series', 0, 'document'),
                          ("Номер", 'document_number', 0, 'document'),
                          ("Кем выдан", 'document_issued_by', 0, 'document'),
                          ("Дата выдачи", 'document_date_of_issue', 'DateEntry', 'document'),
                          ("СНИЛС", 'sniils', 0, 'person')),
        }

        self.labels = []
        self.create_labels()
        self.root.mainloop()

    def refresh_combobox_data(self, table_name):
        self.cursor.execute(f"SELECT id, last_name, first_name, patronymic FROM {table_name}")
        rows = self.cursor.fetchall()
        user_data = ["{} {} {} - {}".format(row[1], row[2], row[3], row[0]) for row in rows]
        self.combobox['values'] = user_data

    def update_user_data(self, table_name, user_id, field, new_value):
        self.cursor.execute(f'UPDATE {table_name} SET {field} = ? WHERE id = ?', (new_value, user_id))
        self.conn.commit()

    def on_combobox_select(self, event, table_name):
        combo_selection = self.combobox.get().split(' - ')
        if len(combo_selection) < 2:
            return
        user_id = combo_selection[-1]
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (user_id,))
        user = self.cursor.fetchone()
        if user:
            for i, label in enumerate(self.labels):
                label.config(text=f"{user[i + 1]}")

    def create_labels(self):
        for i, field in enumerate(self.fields_names[self.key_name]):
            tk.Label(self.root, text=field[0]).grid(row=i * 2 + 2, column=0, sticky='W')
            label = ttk.Label(self.root, text="-", background="white", width=20)
            label.grid(row=i * 2 + 2, column=1, sticky='W')

            # Use default argument for lambda function to capture the current value of i
            label.bind("<Double-1>",
                       lambda event, idx=i, table_name=field[3], field=field[1], field_type=field[2],
                              label=label: self.on_label_double_click(event, idx, table_name, field, field_type,
                                                                      label))

            self.labels.append(label)

    def on_label_double_click(self, event, idx, table_name, field, field_type, label):
        user_id = self.combobox.get().split(' - ')[-1]
        if field_type == 'Combobox':
            top = tk.Toplevel(self.root)
            top.title("Выбор отдела")

            new_department = tk.StringVar()
            new_department.set(label.cget("text"))

            combobox = ttk.Combobox(top, textvariable=new_department, values=["Первый", "Второй", "Третий"])
            combobox.pack(pady=10)

            button = ttk.Button(top, text="Сохранить",
                                command=lambda: self.save_department(table_name, user_id, field, new_department.get(), top))
            button.pack()
        elif field_type == 'DateEntry':
            # Окно для изменения даты
            top = tk.Toplevel(self.root)
            top.title("Дата рождения")

            new_date = DateEntry(top, width=12, background='dark', foreground='white', borderwidth=2)
            user_data = self.cursor.execute(f"SELECT {field} FROM {table_name} WHERE id = ?", (user_id,)).fetchone()
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


if __name__ == "__main__":
    UserDataApp()