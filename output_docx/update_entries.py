import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog


class UserDataApp:
    def __init__(self):
        self.conn = sqlite3.connect('test_db.db')
        self.cursor = self.conn.cursor()
        self.root = tk.Tk()
        self.root.title("Пользователи")
        self.combobox = ttk.Combobox(self.root)
        self.combobox.grid(row=0, column=0, columnspan=2)
        self.refresh_combobox_data()
        self.combobox.bind('<<ComboboxSelected>>', self.on_combobox_select)
        self.fields_names = {
            'persons': (("Фамилия", 'last_name'), ("Имя", 'first_name'), ("Отчество", 'patronymic'),
                        ("Дата рождения", 'date_of_birth'), ("Отдел", 'department')),
        }
        self.labels = []
        self.create_labels()
        self.root.mainloop()

    def refresh_combobox_data(self):
        self.cursor.execute("SELECT id, last_name, first_name, patronymic FROM persons")
        rows = self.cursor.fetchall()
        user_data = ["{} {} {} - {}".format(row[1], row[2], row[3], row[0]) for row in rows]
        self.combobox['values'] = user_data

    def update_user_data(self, user_id, field, new_value):
        self.cursor.execute(f'UPDATE persons SET {field} = ? WHERE id = ?', (new_value, user_id))
        self.conn.commit()

    def on_combobox_select(self, event):
        combo_selection = self.combobox.get().split(' - ')
        if len(combo_selection) < 2:
            return
        user_id = combo_selection[-1]
        self.cursor.execute("SELECT * FROM persons WHERE id = ?", (user_id,))
        user = self.cursor.fetchone()
        if user:
            for i, label in enumerate(self.labels):
                label.config(text=f"{user[i + 1]}")

    def create_labels(self):
        for i, field in enumerate(self.fields_names['persons']):
            tk.Label(self.root, text=field[0]).grid(row=i * 2 + 2, column=0, sticky='W')
            label = ttk.Label(self.root, text="-", background="white", width=20)
            label.grid(row=i * 2 + 2, column=1, sticky='W')

            # Use default argument for lambda function to capture the current value of i
            label.bind("<Double-1>",
                       lambda event, idx=i, field=field[1], label=label: self.on_label_double_click(event, idx, field,
                                                                                                    label))

            self.labels.append(label)

    def on_label_double_click(self, event, idx, field, label):
        user_id = self.combobox.get().split(' - ')[-1]
        if field == 'department':
            top = tk.Toplevel(self.root)
            top.title("Выбор отдела")

            new_department = tk.StringVar()
            new_department.set(label.cget("text"))

            combobox = ttk.Combobox(top, textvariable=new_department, values=["Первый", "Второй", "Третий"])
            combobox.pack(pady=10)

            button = ttk.Button(top, text="Сохранить",
                                command=lambda: self.save_department(user_id, new_department.get(), top))
            button.pack()
        else:
            new_value = simpledialog.askstring("Редактирование", f"Введите новое значение",
                                               initialvalue=label.cget("text"))
            if new_value:
                label.config(text=new_value)
                self.update_user_data(user_id, field, new_value)
                self.refresh_combobox_data()
                self.on_combobox_select(None)

    def save_department(self, user_id, new_department, top):
        self.update_user_data(user_id, 'department', new_department)
        top.destroy()
        self.refresh_combobox_data()
        self.on_combobox_select(None)


if __name__ == "__main__":
    UserDataApp()
