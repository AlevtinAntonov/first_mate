import tkinter as tk
from datetime import datetime
from tkinter import ttk

from app_model.db.db_query import query_full_addresses
# from app_model.db.db_connect import DB
from app_model.variables import CONF_D_W
from app_view_model.functions.find_address import find_full_addresses


def person_select_combo(db, window_frame, row, column):
    # Создание Combobox для выбора персоны
    combo = ttk.Combobox(window_frame, width=45)
    combo.grid(row=row, column=column, columnspan=3, cnf=CONF_D_W)
    combo['values'] = get_person_names(db)

    def update_info(event):
        person_name = combo.get()
        print(f'{person_name=}')
        try:
            with db as cur:
                if len(person_name.split()) == 5 and person_name.split()[3] == 'д.р.:':
                    last_name, first_name, patronymic, _txt, date_of_birth = person_name.split()
                    print(last_name, first_name, patronymic, date_of_birth)
                    cur.execute(
                        "SELECT person_id FROM person "
                        "WHERE (last_name = ? AND first_name = ? AND patronymic = ? AND date_of_birth = ? "
                        "AND is_visible = TRUE)",
                        (last_name, first_name, patronymic, date_of_birth))
                    person = cur.fetchone()
                    if person:
                        addresses_from_db_dict = find_full_addresses(db, person[0])
                        person_id_var.set(person[0])
                        # last_name_var.set(person[1])
                        # first_name_var.set(person[2])
                        # patronymic_var.set(person[3])
                        # date_of_birth_var.set(person[4])
                else:
                    print(len(person_name.split()), person_name[3])
                    print(f'Error len(person_name.split()) not equal 4 and person_name.split()[3] != д.р.:')

        except Exception as e:
            print(f'Error Exception - {e}')

    def update_combo_options(event):
        typed_text = combo.get()

        if typed_text == "":
            filtered_values = get_person_names(db)  # Показать все варианты, если нет введенного текста
        else:
            filtered_values = [value for value in get_person_names(db) if
                               typed_text.lower() in str(value).lower()]  # Фильтрация вариантов по введенному тексту

        combo['values'] = filtered_values

    # Строковые переменные для отображения информации в entry
    person_id_var = tk.StringVar()
    # last_name_var = tk.StringVar()
    # first_name_var = tk.StringVar()
    # patronymic_var = tk.StringVar()
    # date_of_birth_var = tk.StringVar()

    combo.bind("<<ComboboxSelected>>", update_info)

    # Привязка функции update_combo_options к событию ввода текста в combobox
    combo.bind("<KeyRelease>", update_combo_options)


def get_person_names(db):
    with db as cur:
        cur.execute("SELECT last_name, first_name, patronymic, date_of_birth "
                    "FROM person ORDER BY last_name, first_name, patronymic")
        persons = [(person[0],
                    person[1] if person[1] else '-',
                    person[2] if person[2] else '-',
                    'д.р.:', person[3].strftime('%d.%m.%Y'))
                   for person in cur.fetchall()]
        return persons


if __name__ == '__main__':
    # db = DB('C:/Users/anton/PycharmProjects/first_mate/app_model/db/DB_PROD.FDB')
    window = tk.Tk()
    window.title("Выбор персоны")
    person_select_combo(window, 2, 2)

    window.mainloop()
