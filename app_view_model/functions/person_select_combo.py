import tkinter as tk
from tkinter import ttk


def person_select_combo(window, row, column):
    # Создание комбобокса для выбора персоны
    combo = ttk.Combobox(window, width=35)
    combo.grid(row=row, column=column)


def update_info(db, combo, event):
    person_name = combo.get()
    with db as cur:
        if len(person_name.split()) == 4:
            last_name, first_name, patronymic, date_of_birth = person_name.split()
            cur.execute(
                "SELECT * FROM PERSON WHERE (LAST_NAME = ? and FIRST_NAME = ? and PATRONYMIC = ? and DATE_OF_BIRTH = ?)",
                (last_name, first_name, patronymic, date_of_birth))
            person = cur.fetchone()
            # print(person)
            if person:
                last_name_var.set(person[1])
                first_name_var.set(person[2])
                patronymic_var.set(person[3])
                date_of_birth_var.set(person[4])
                gender_id_var.set(person[5])
                document_id_var.set(person[6])
        else:
            print(f'Error len(person_name.split()) not equal 4.')


# Строковые переменные для отображения информации в entry
last_name_var = tk.StringVar()
first_name_var = tk.StringVar()
patronymic_var = tk.StringVar()
date_of_birth_var = tk.StringVar()
gender_id_var = tk.StringVar()
document_id_var = tk.StringVar()
