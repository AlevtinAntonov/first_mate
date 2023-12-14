import tkinter as tk
from tkinter import ttk
import sqlite3

# Создание окна
window = tk.Tk()
window.title("Выбор персоны")

# Подключение к базе данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы PERSON, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS PERSON (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    LAST_NAME TEXT,
    FIRST_NAME TEXT,
    PATRONYMIC TEXT,
    DATE_OF_BIRTH TEXT,
    GENDER_ID INTEGER,
    DOCUMENT_ID INTEGER
)''')

conn.commit()

# Создание комбобокса для выбора персоны
combo = ttk.Combobox(window, width=35)
combo.grid(row=0, column=0)


# Функция для обновления информации при выборе персоны
# Функция для обновления информации при выборе персоны
def update_info(event):
    person_name = combo.get()
    try:
        if len(person_name.split()) == 4:
            last_name, first_name, patronymic, date_of_birth = person_name.split()
            cursor.execute(
                "SELECT * FROM PERSON WHERE (LAST_NAME = ? and FIRST_NAME = ? and PATRONYMIC = ? and DATE_OF_BIRTH = ?)",
                (last_name, first_name, patronymic, date_of_birth))
            person = cursor.fetchone()
            print(person)
            if person:
                last_name_var.set(person[1])
                first_name_var.set(person[2])
                patronymic_var.set(person[3])
                date_of_birth_var.set(person[4])
                gender_id_var.set(person[5])
                document_id_var.set(person[6])
        else:
            print(f'Error len(person_name.split()) not equal 4.')

    except Exception as e:
        print(f'Error Exception - {e}')



# Строковые переменные для отображения информации в entry
last_name_var = tk.StringVar()
first_name_var = tk.StringVar()
patronymic_var = tk.StringVar()
date_of_birth_var = tk.StringVar()
gender_id_var = tk.StringVar()
document_id_var = tk.StringVar()

# Создание entry для отображения информации о персоне
last_name_label = tk.Label(window, text="Фамилия:")
last_name_label.grid(row=1, column=0)
last_name_entry = tk.Entry(window, textvariable=last_name_var)
last_name_entry.grid(row=1, column=1)

first_name_label = tk.Label(window, text="Имя:")
first_name_label.grid(row=2, column=0)
first_name_entry = tk.Entry(window, textvariable=first_name_var)
first_name_entry.grid(row=2, column=1)

patronymic_label = tk.Label(window, text="Отчество:")
patronymic_label.grid(row=3, column=0)
patronymic_entry = tk.Entry(window, textvariable=patronymic_var)
patronymic_entry.grid(row=3, column=1)

date_of_birth_label = tk.Label(window, text="Дата рождения:")
date_of_birth_label.grid(row=4, column=0)
date_of_birth_entry = tk.Entry(window, textvariable=date_of_birth_var)
date_of_birth_entry.grid(row=4, column=1)

gender_id_label = tk.Label(window, text="Пол:")
gender_id_label.grid(row=5, column=0)
gender_id_entry = tk.Entry(window, textvariable=gender_id_var)
gender_id_entry.grid(row=5, column=1)

document_id_label = tk.Label(window, text="ID документа:")
document_id_label.grid(row=6, column=0)
document_id_entry = tk.Entry(window, textvariable=document_id_var)
document_id_entry.grid(row=6, column=1)


# Функция для сохранения данных в базе
def save_data():
    last_name = last_name_var.get()
    first_name = first_name_var.get()
    patronymic = patronymic_var.get()
    date_of_birth = date_of_birth_var.get()
    gender_id = gender_id_var.get()
    document_id = document_id_var.get()
    cursor.execute(
        "INSERT INTO PERSON (LAST_NAME, FIRST_NAME, PATRONYMIC, DATE_OF_BIRTH, GENDER_ID, DOCUMENT_ID) VALUES (?, ?, ?, ?, ?, ?)",
        (last_name, first_name, patronymic, date_of_birth, gender_id, document_id))
    conn.commit()
    combo['values'] = get_person_names()


# Кнопка для сохранения данных
save_button = tk.Button(window, text="Сохранить", command=save_data)
save_button.grid(row=7, column=0)


# Получение и отображение имен персон из базы данных
def get_person_names():
    cursor.execute("SELECT LAST_NAME, FIRST_NAME, PATRONYMIC, DATE_OF_BIRTH FROM PERSON")
    persons = [person for person in cursor.fetchall()]
    return persons


combo['values'] = get_person_names()


# Функция для обновления вариантов в combobox при вводе текста
def update_combo_options(event):
    typed_text = combo.get()

    if typed_text == "":
        filtered_values = get_person_names()  # Показать все варианты, если нет введенного текста
    else:
        filtered_values = [value for value in get_person_names() if
                           typed_text.lower() in value.lower()]  # Фильтрация вариантов по введенному тексту

    combo['values'] = filtered_values


combo.bind("<<ComboboxSelected>>", update_info)
# Привязка функции update_combo_options к событию ввода текста в combobox
combo.bind("<KeyRelease>", update_combo_options)

# Запуск основного цикла окна
window.mainloop()
