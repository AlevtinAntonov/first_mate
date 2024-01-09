import tkinter as tk
from tkinter import ttk
import sqlite3

def check_and_display_data():
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Запрос данных из базы данных
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()

    # Отображение данных в ttk.Entry
    for index, entry_data in enumerate(data):
        entry_values[index].delete(0, tk.END)  # Очистка содержимого ttk.Entry
        entry_values[index].insert(0, entry_data)  # Вставка данных из базы данных в ttk.Entry

    conn.close()

def update_database(event):
    # Обновление данных в базе данных при изменении ttk.Entry
    # Напишите здесь код для обновления базы данных

root = tk.Tk()

# Создание ttk.Entry
entry_values = []
for i in range(5):  # Пример: 5 ttk.Entry
    entry = ttk.Entry(root)
    entry_values.append(entry)
    entry_values[i].grid(row=i, column=0)

# Проверка и отображение данных при запуске приложения
check_and_display_data()

# Связывание события <<Modified>> с функцией обновления базы данных
for entry in entry_values:
    entry.bind("<<Modified>>", update_database)

root.mainloop()


import tkinter as tk
from tkinter import ttk
import sqlite3

def check_and_display_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()

    for index, entry_data in enumerate(data):
        entry_values[index].delete(0, tk.END)
        entry_values[index].insert(0, entry_data)

    # Проверка значения в Combobox
    combobox_value = combobox.get()
    if combobox_value:  # Проверяем, что значение выбрано
        if (combobox_value, ) in data:  # Проверяем наличие значения в базе данных
            print(f"{combobox_value} найдено в базе данных")
        else:
            print(f"{combobox_value} не найдено в базе данных")

    conn.close()

def update_database(event):
    # Обновление данных в базе данных при изменении ttk.Entry
    # Реализация обновления базы данных

root = tk.Tk()

entry_values = []
for i in range(5):
    entry = ttk.Entry(root)
    entry_values.append(entry)
    entry_values[i].grid(row=i, column=0)

# Добавление ttk.Combobox
options = ["Option 1", "Option 2", "Option 3"]  # Пример значений для Combobox
combobox = ttk.Combobox(root, values=options)
combobox.grid(row=6, column=0)

check_and_display_data()

# Связывание события <<Modified>> с функцией обновления базы данных
for entry in entry_values:
    entry.bind("<<Modified>>", update_database)

root.mainloop()
