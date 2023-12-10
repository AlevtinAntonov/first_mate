# import tkinter as tk
# from tkinter import ttk
#
# def validate_input(*args):
#     if entry1.get() and entry2.get() and combobox.get():
#         button.config(state=tk.NORMAL, style='active.TButton')
#     else:
#         button.config(state=tk.DISABLED, style='inactive.TButton')
#
# root = tk.Tk()
# root.title("Проверка ввода данных")
#
# frame = ttk.Frame(root, padding="10")
# frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
# label1 = ttk.Label(frame, text="Введите данные:")
# label1.grid(row=0, column=0, sticky=tk.W)
#
# entry1 = ttk.Entry(frame, width=20)
# entry1.grid(row=1, column=0, sticky=tk.W)
# entry1.bind("<KeyRelease>", validate_input)
#
# entry2 = ttk.Entry(frame, width=20)
# entry2.grid(row=2, column=0, sticky=tk.W)
# entry2.bind("<KeyRelease>", validate_input)
#
# label2 = ttk.Label(frame, text="Выберите значение из списка:")
# label2.grid(row=3, column=0, sticky=tk.W)
#
# combobox = ttk.Combobox(frame, values=['Option 1', 'Option 2', 'Option 3'], width=17)
# combobox.grid(row=4, column=0, sticky=tk.W)
# combobox.bind("<<ComboboxSelected>>", validate_input)
#
# style = ttk.Style()
# style.configure('inactive.TButton', background='gray')
# style.configure('active.TButton', background='red')
#
# button = ttk.Button(frame, text="Сохранить", state=tk.DISABLED, style='inactive.TButton')
# button.grid(row=5, column=0, sticky=tk.W, pady=(10, 0))
#
# root.mainloop()
# import tkinter as tk
# from tkinter import ttk
#
# def validate_input(*args):
#     if entry1.get() and entry2.get() and combobox.get():
#         button.config(state=tk.NORMAL, style='active.TButton')
#     else:
#         button.config(state=tk.DISABLED, style='inactive.TButton')
#
# root = tk.Tk()
# root.title("Проверка ввода данных")
#
# frame = ttk.Frame(root, padding=10)
# frame.grid(row=0, column=0, sticky="nsew")
#
# label1 = ttk.Label(frame, text="Введите данные:")
# label1.grid(row=0, column=0, sticky="w")
#
# entry1 = ttk.Entry(frame, width=20)
# entry1.grid(row=1, column=0, sticky="w")
# entry1.bind("<KeyRelease>", validate_input)
#
# entry2 = ttk.Entry(frame, width=20)
# entry2.grid(row=2, column=0, sticky="w")
# entry2.bind("<KeyRelease>", validate_input)
#
# label2 = ttk.Label(frame, text="Выберите из списка:")
# label2.grid(row=3, column=0, sticky="w")
#
# combobox = ttk.Combobox(frame, values=['Option 1', 'Option 2', 'Option 3'], width=17)
# combobox.grid(row=4, column=0, sticky="w")
# combobox.bind("<<ComboboxSelected>>", validate_input)
#
# style = ttk.Style()
# style.map('TButton',
#     background=[('active', 'red'), ('disabled', 'gray')]
# )
#
# button = ttk.Button(frame, text="Сохранить", state=tk.DISABLED, style='inactive.TButton')
# button.grid(row=5, column=0, sticky="w", pady=(10, 0))
#
# root.mainloop()
import tkinter as tk
from tkinter import ttk

# def validate_input(*args):
#     if args.get():
#         button.config(state=tk.NORMAL, background='red', fg='white')
#     else:
#         button.config(state=tk.DISABLED, background='LightGray', fg='white')


# def validate_input(*args):
#     all_entries_filled = all(entry.get() for entry in entry_list)
#     # all_comboboxes_selected = all(combobox.get() for combobox in combobox_list)
#
#     if all_entries_filled:
#         button.config(state=tk.NORMAL, background='red', fg='white')
#     else:
#         button.config(state=tk.DISABLED, background='LightGray', fg='white')
#
#
# root = tk.Tk()
# root.title("Проверка ввода данных")
#
# frame = ttk.Frame(root, padding="10")
# frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
# label1 = ttk.Label(frame, text="Введите данные:")
# label1.grid(row=0, column=0, sticky=tk.W)
#
# entry1 = ttk.Entry(frame, width=20)
# entry1.grid(row=1, column=0, sticky=tk.W)
# entry1.bind("<KeyRelease>", validate_input)
#
# entry2 = ttk.Entry(frame, width=20)
# entry2.grid(row=2, column=0, sticky=tk.W)
# entry2.bind("<KeyRelease>", validate_input)
#
# label2 = ttk.Label(frame, text="Выберите значение из списка:")
# label2.grid(row=3, column=0, sticky=tk.W)
#
# combobox = ttk.Combobox(frame, values=['Option 1', 'Option 2', 'Option 3'], width=17)
# combobox.grid(row=4, column=0, sticky=tk.W)
# combobox.bind("<<ComboboxSelected>>", validate_input)
# entry_list = [entry1, entry2, combobox]
# # combobox_list = [combobox, ]
# button = tk.Button(frame, text="Сохранить", state=tk.DISABLED, command=root.destroy)
# button.grid(row=5, column=0, sticky=tk.W, pady=(10, 0))
#
# root.mainloop()
# validate_input_btn_ok
# import tkinter as tk
# from tkinter import ttk
#
# def display_info(*args):
#     selected_name = combobox.get()
#     if selected_name in data:
#         dob_label.config(text="Дата рождения: " + data[selected_name][0])
#         gender_label.config(text="Пол: " + data[selected_name][1])
#     else:
#         dob_label.config(text="Дата рождения: ")
#         gender_label.config(text="Пол: ")
#
# root = tk.Tk()
# root.title("Информация о людях")
#
# data = {
#     "Иванов Иван Иванович": ("10.10.1980", "М"),
#     "Петров Петр Петрович": ("05.05.1995", "М"),
#     "Сидорова Елена Петровна": ("15.12.1978", "Ж")
# }
#
# frame = ttk.Frame(root, padding=10)
# frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
# label = ttk.Label(frame, text="Выберите ФИО:")
# label.grid(row=0, column=0, columnspan=2, sticky='we')
#
# combobox = ttk.Combobox(frame, values=list(data.keys()))
# combobox.grid(row=1, column=0, columnspan=2, sticky='we')
# combobox.bind("<<ComboboxSelected>>", display_info)
#
# dob_label = ttk.Label(frame, text="Дата рождения: ")
# dob_label.grid(row=2, column=0, sticky=tk.W)
#
# gender_label = ttk.Label(frame, text="Пол: ")
# gender_label.grid(row=2, column=3, sticky=tk.W)
#
# root.mainloop()
#
# import
# import tkinter as tk
# from tkinter import ttk
#
# from app_model.db.db_connect import DB
# from app_view_model.functions.functions import fill_combobox
#
#
#
# def update_combobox_values(event=None):
#     search_text = combobox.get()
#     matching_values = [person_info[0] for person_info in data.values() if search_text.lower() in person_info[0].lower()]
#     combobox["values"] = matching_values
#
#
# def display_info(*args):
#     selected_name = combobox.get()
#     for person, person_info in data.items():
#         if person_info[0] == selected_name:
#             dob_label.config(text="Дата рождения: " + person_info[1].strftime("%d.%m.%Y"))
#             gender_label.config(text="Пол: " + person_info[2])
#             break
#     else:
#         dob_label.config(text="Дата рождения: ")
#         gender_label.config(text="Пол: ")
#
#
# root = tk.Tk()
# root.title("Информация о людях")
# db = DB('C:/Users/anton/PycharmProjects/first_mate/app_model/db/DB_PROD.FDB')
#
# data = fill_combobox(db, 'child_list_show', None, None)
# for k, v in data.items():
#     print(k, v)
#     #
# #     {
# #     1: ("Ианов Иван Ианович", "10.10.1980", "М"),
# #     2: ("Петров Петр Петрович", "01.05.1995", "М"),
# #     3: ("идорова Елена Петрова", "15.12.1978", "Ж"),
# # }
#
# frame = ttk.Frame(root, padding=10)
# frame.grid(row=0, column=0, sticky='we')
#
# label = ttk.Label(frame, text="Выберите ФИО:")
# label.grid(row=0, column=0, sticky=tk.W)
#
# combobox = ttk.Combobox(frame)
# combobox["values"] = [person_info[0] for person_info in data.values()]
# combobox.grid(row=1, column=0, sticky=tk.W)
# combobox.bind("<<ComboboxSelected>>", display_info)
# combobox.bind("<KeyRelease>", update_combobox_values)
#
# dob_label = ttk.Label(frame, text="Дата рождения: ")
# dob_label.grid(row=2, column=0, sticky=tk.W)
#
# gender_label = ttk.Label(frame, text="Пол: ")
# gender_label.grid(row=3, column=0, sticky=tk.W)
#
# root.mainloop()

import tkinter as tk

# Создаем окно
root = tk.Tk()
root.title("Адреса")

# Словарь с данными
addresses = {1: ('is_registration', 'Адрес регистрации', "123456, Санкт-Петербург г., Вербная ул., д. 18, корп. 1, лит. А, кв. 1"),
2: ('is_fact', 'Адрес фактический', "123456, Санкт-Петербург г., Вербная ул., д. 18, корп. 1, лит. А, кв. 1"),
3: ('is_residence', 'Адрес рег. по м.преб.', "197375, Санкт-Петербург, Санкт-Петербург г., Вербная ул., д. 20/3, лит. А, кв. 300")}

# Функция для печати адресов
def print_addresses():
    for key, value in addresses.items():
        label = tk.Label(root, text=f"{value[1]}: {value[2]}")
        label.pack()

# Кнопка для печати адресов
print_button = tk.Button(root, text="Печать адресов", command=print_addresses)
print_button.pack()

root.mainloop()