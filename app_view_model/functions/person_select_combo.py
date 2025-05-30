import tkinter as tk
from tkinter import ttk

from app_model.variables import CONF_D_W


def person_select_combo(db, window_frame, row, column, person=""):
    # Создание Combobox для выбора персоны
    combo = ttk.Combobox(window_frame, width=45)
    combo.grid(row=row, column=column, columnspan=3, cnf=CONF_D_W)
    combo['values'] = get_person_names(db, person)

    def update_info(event):
        person_name = combo.get()
        try:
            with db as cur:
                if len(person_name.split()) == 5 and person_name.split()[3] == 'д.р.:':
                    last_name, first_name, patronymic, _txt, date_of_birth = person_name.split()
                    cur.execute(
                        "SELECT person_id FROM person "
                        "WHERE (last_name = ? AND first_name = ? AND patronymic = ? AND date_of_birth = ? "
                        "AND is_visible = TRUE)",
                        (last_name, first_name, patronymic, date_of_birth))
                    person = cur.fetchone()
                    if person:
                        person_id_var.set(person[0])
                else:
                    print(f'Error len(person_name.split()) not equal 4 and person_name.split()[3] != д.р.:')

        except Exception as e:
            print(f'Error Exception def update_info  - {e}')

    def update_combo_options(event):
        typed_text = combo.get()

        if typed_text == "":
            filtered_values = get_person_names(db, person)  # Показать все варианты, если нет введенного текста
        else:
            filtered_values = [value for value in get_person_names(db, person) if
                               typed_text.lower() in str(value).lower()]  # Фильтрация вариантов по введенному тексту

        combo['values'] = filtered_values

    # Строковые переменные для отображения person_id
    person_id_var = tk.StringVar()

    combo.bind("<<ComboboxSelected>>", update_info)

    # Привязка функции update_combo_options к событию ввода текста в combobox
    combo.bind("<KeyRelease>", update_combo_options)
    return person_id_var


def get_person_names(db, person):
    match person:
        case 'parents':
            query = """ SELECT last_name, first_name, patronymic, date_of_birth
                        FROM person p
                        JOIN parents pa ON p.person_id = pa.person_id
                        WHERE p.IS_VISIBLE = True
                        ORDER BY last_name, first_name, patronymic"""
        case 'children':
            query = """ SELECT last_name, first_name, patronymic, date_of_birth
                        FROM person p
                        JOIN child c ON p.person_id = c.person_id
                        WHERE p.IS_VISIBLE = True
                        ORDER BY last_name, first_name, patronymic"""
        case _:
            query = """ SELECT last_name, first_name, patronymic, date_of_birth
                        FROM person
                        WHERE PERSON.IS_VISIBLE = True
                        ORDER BY last_name, first_name, patronymic"""

    with db as cur:
        cur.execute(query)
        persons = [(person[0],
                    person[1] if person[1] else '-',
                    person[2] if person[2] else '-',
                    'д.р.:', person[3].strftime('%d.%m.%Y'))
                   for person in cur.fetchall()]
        return persons


if __name__ == '__main__':
    pass
