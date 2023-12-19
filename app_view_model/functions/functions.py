import re
from datetime import datetime
from functools import partial
from os import path
import tkinter as tk
from tkinter import ttk, messagebox

from tkcalendar import DateEntry

from app_model.db.db_query import query_insert_into, REFERRAL_SAVE, CHECK_PERSON_CHILD, CHECK_PARENT, DB_DICT, gender, \
    child, \
    referral, parents, query_check_person, query_check_document, document, building, person, query_find_id, \
    query_insert_into_table_return_id, team, age, focus, mode, benefit
from app_model.variables import CONF_D_W, CONF


def position_center(win, width, height):
    """
    centers a tkinter window
    :param height: height of main window
    :param width: width of main window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    x_coordinate = int((win.winfo_screenwidth() - int(width)) / 2)
    y_coordinate = int((win.winfo_screenheight() - int(height)) / 2)
    return win.geometry(f"+{x_coordinate}+{y_coordinate}")


def path_to_file(dir_file, file):
    return path.abspath(path.join(dir_file, file))


# def fill_combobox_child(db, tbl_name, field_id, field_data):
#     dict_combo = {}
#     with db as cur:
#         cur.execute(
#             """SELECT child.child_id, person.last_name, person.first_name, person.patronymic FROM person
#             INNER JOIN child ON person.person_id = child.person_id WHERE (((child.is_visible)=True))
#             ORDER BY PERSON.last_name, PERSON.first_name, PERSON.patronymic;""")
#
#         # " SELECT %s, %s FROM %s WHERE is_visible ORDER BY %s;" % (field_id, field_data, tbl_name, field_id))
#         [dict_combo.update({row[0]: ' '.join((row[1], row[2], row[3]))}) for row in cur.fetchall()]
#         return dict_combo


def fill_combobox(db, tbl_name, field_id, field_data):
    dict_combo = {}
    with db as cur:
        if tbl_name == 'child_list_show':
            cur.execute(
                """SELECT child.child_id, person.last_name, person.first_name, person.patronymic, person.date_of_birth, 
                gender.gender_name
                FROM gender INNER JOIN (person INNER JOIN child ON person.person_id = child.person_id) 
                ON gender.gender_id = person.gender_id
                WHERE (((child.is_visible)=True))
                ORDER BY person.last_name, person.first_name, person.patronymic;""")
            [dict_combo.update({row[0]: (' '.join((row[1], row[2], row[3])), row[4], row[5])}) for row in cur.fetchall()]
        elif tbl_name == 'child_list':
            cur.execute(
                """SELECT child.child_id, person.last_name, person.first_name, person.patronymic FROM person 
                INNER JOIN child ON person.person_id = child.person_id WHERE (((child.is_visible)=True))
                ORDER BY PERSON.last_name, PERSON.first_name, PERSON.patronymic;""")
            [dict_combo.update({row[0]: ' '.join((row[1], row[2], row[3]))}) for row in cur.fetchall()]
        else:
            cur.execute(
                " SELECT %s, %s FROM %s WHERE is_visible ORDER BY %s;" % (field_id, field_data, tbl_name, field_id))
            [dict_combo.update({row[0]: row[1]}) for row in cur.fetchall()]
        return dict_combo


def find_id(db, tbl_name, field_id, field_data, field_value):
    for k, v in fill_combobox(db, tbl_name, field_id, field_data).items():
        if v == field_value:
            return k
    return False


def check_if_exists(db, tbl_name, field_1: str, field_2: str, field_3: str, field_4: datetime):
    if tbl_name == 'person':
        query = (query_check_person % tbl_name)
    if tbl_name == 'document':
        query = (query_check_document % tbl_name)
    with db as cur:
        try:
            cur.execute(query, (field_1, field_2, field_3, field_4))
            check_res = cur.fetchone()
            if check_res:
                return check_res[0]
            return False
        except Exception:
            print('Ошибка в check_if_exists')


def find_person(db, tbl_name, person_id):
    query = (query_find_id % tbl_name)
    with db as cur:
        try:
            cur.execute(query, (person_id,))
            result = cur.fetchone()
            if result:
                return result[0]
            return False
        except Exception:
            print('Ошибка в find_person')


def current_timestamp():
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    return date_time.strftime("%d.%m.%Y %H:%M")


def capitalize_double_surname(input_name):
    if ' ' in input_name and '-' in input_name:
        input_name = input_name.replace(' ', '')
    if ' ' in input_name:
        separator = ' '
    elif '-' in input_name:
        separator = '-'
    else:
        return input_name.capitalize()

    parts = input_name.split(separator, maxsplit=1)
    capitalized_parts = [part.capitalize() for part in parts]
    return separator.join(capitalized_parts)


def referral_save(db, referral_number, referral_date, referral_begin_date, referral_comment, child_last_name: str,
                  child_first_name: str, child_patronymic: str, child_male, child_date_of_birth, mode_get, building_get,
                  team_get, age_get, focus_get, benefit_get):
    flag = True
    child_last_name = capitalize_double_surname(child_last_name)
    child_first_name = capitalize_double_surname(child_first_name)
    child_patronymic = capitalize_double_surname(child_patronymic)

    gender_id = find_id(db, gender, DB_DICT[gender][0], DB_DICT[gender][1], child_male)
    team_id = find_id(db, team, DB_DICT[team][0], DB_DICT[team][1], team_get)
    if not check_if_exists(db, person, child_last_name, child_first_name, child_patronymic,
                           child_date_of_birth):
        with db as cur:
            query = query_insert_into_table_return_id(person, person) % DB_DICT[person]
            cur.execute(query,
                        (child_last_name, child_first_name, child_patronymic, child_date_of_birth, gender_id,
                         current_timestamp()))
            person_id = cur.fetchone()[0]
            query_add_child = query_insert_into_table_return_id(child, child) % DB_DICT[child]
            cur.execute(query_add_child, (person_id, current_timestamp()))
            child_id = cur.fetchone()[0]

    person_id = check_if_exists(db, person, child_last_name, child_first_name, child_patronymic,
                                child_date_of_birth)
    child_id = find_person(db, child, person_id)
    building_id = find_id(db, building, DB_DICT[building][0], DB_DICT[building][1], building_get)
    age_id = find_id(db, age, DB_DICT[age][0], DB_DICT[age][1], age_get)
    focus_id = find_id(db, focus, DB_DICT[focus][0], DB_DICT[focus][1], focus_get)
    mode_id = find_id(db, mode, DB_DICT[mode][0], DB_DICT[mode][1], mode_get)
    benefit_id = find_id(db, benefit, DB_DICT[benefit][0], DB_DICT[benefit][1], benefit_get)
    referral_id = find_id(db, referral, DB_DICT[referral][0], DB_DICT[referral][1], referral_number)
    if not referral_id:
        with db as cur:
            query = query_insert_into(referral) % DB_DICT[referral]
            cur.execute(query,
                        (referral_number, referral_date, referral_begin_date, referral_comment, child_id, mode_id,
                         building_id, team_id, age_id, focus_id, benefit_id))
    else:
        print('referral ID exist')


# def validate_russian_names(input):
#     return bool(re.search('[а-яА-Я -]', input))


def check_russian_letters(input_str):
    import re
    return bool(re.search("[а-яА-Я -]", input_str))


def on_validate_input(new_text):
    return check_russian_letters(new_text)


# def on_validate_input(new_text):
#
#     if check_russian_letters(new_text):
#         # Разрешено ввести только цифры
#         return check_russian_letters(new_text)
#     else:
#         # Недопустимый символ, отобразить ttk.Entry с красной рамкой
#         entry_widget.config(style='Red.TEntry')
#         return False


# def parent_save(db, last_name: str, first_name: str, patronymic: str, date_of_birth, parent_male, citizenship,
#                 document_type, document_series, document_number, document_date_of_issue, document_issued_by,
#                 document_date_of_expire, address_id=None):
#     last_name, first_name, patronymic = last_name.capitalize(), first_name.capitalize(), patronymic.capitalize()
#     gender_id = find_id(db, gender, DB_DICT[gender][0], DB_DICT[gender][1], parent_male)
#     citizenship_id = find_id(db, 'citizenship', 'citizenship_id', 'citizenship_short_name',
#                              citizenship)
#     document_type_id = find_id(db, 'document_type', 'document_type_id', 'document_type_name',
#                                document_type)
#     if not check_if_exists(db, document, document_series, document_number, document_date_of_issue, document_type_id):
#         query = query_insert_into(document) % DB_DICT[document]
#         with db as cur:
#             cur.execute(query, (
#                 document_series, document_number, document_issued_by, document_date_of_issue, document_date_of_expire,
#                 document_type_id, current_timestamp()))
#     document_id = check_if_exists(db, document, document_series, document_number, document_date_of_issue,
#                                   document_type_id)
#     if not check_if_exists(db, parents, last_name, first_name, patronymic, date_of_birth):
#         query = query_insert_into(parents) % DB_DICT[parents]
#         with db as cur:
#             cur.execute(query,
#                         (last_name, first_name, patronymic, date_of_birth, gender_id, citizenship_id, document_id,
#                          address_id, current_timestamp()))


def insert_into_table(db, table_name, fields, values):
    # Формирование SQL-запроса для вставки данных
    placeholders = ', '.join(['?'] * len(fields))
    query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({placeholders})"
    # Подключение к базе данных
    with db as cur:
        cur.execute(query, values)


def update_record(table_name, fields, values):
    # Подключаемся к базе данных
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Формируем SQL-запрос для обновления записей
    sql = f"UPDATE {table_name} SET "
    sql += ", ".join(f"{field} = ?" for field in fields)
    sql += " WHERE condition_column = ?"  # Укажите условие для обновления записей

    # Выполняем SQL-запрос
    cursor.execute(sql, values + [condition_value])  # condition_value - значение для условия

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()


def save_access():
    messagebox.showinfo(title="", message="Данные записаны успешно!")


def click():
    result = messagebox.askyesnocancel(title="Внимание!",
                                       message="Не все данные введены. Хотите продолжить без записи?")
    if result == None:
        pass
    elif result:
        messagebox.showinfo("Результат", "Операция подтверждена")
    else:
        messagebox.showinfo("Результат", "Операция отменена")


def validate_string(input_data):
    try:
        if input_data != '':
            return True
        flag = True
    except Exception:
        flag = False


def check_and_highlight(entry):
    # Получаем текст из поля ввода
    value = entry.get()

    # Проверяем, пусто ли поле
    if not value:
        # Если поле пусто, выделяем его красной рамкой
        entry.config(highlightbackground="#ff0000", highlightcolor="#ff0000", highlightthickness=2)
        return False
    else:
        # Если поле не пусто, сбрасываем выделение
        entry.config(highlightbackground="SystemWindowFrame", highlightcolor="SystemWindowFrame", highlightthickness=1)
        return True


def validate_combobox(combobox, label):
    if combobox.get() == '':
        label.config(borderwidth=2, relief="solid", foreground='red')
        # button.config(state=tk.DISABLED, background='LightGray', fg='white')
    else:
        label.config(borderwidth=0, relief="flat", foreground='black')
        # button.config(state=tk.NORMAL, background='red', fg='white')


def validate_input_btn_ok(*args):
    all_entries_filled = all(entry.get() for entry in entry_list)

    if all_entries_filled:
        btn_ok.config(state=tk.NORMAL, background='red', fg='white')
    else:
        btn_ok.config(state=tk.DISABLED, background='LightGray', fg='white')


# def validate_combobox_event(event):
#     if combobox.get() == '':
#         label.config(foreground='red')
#     else:
#         label.config(foreground='black')
# def check_if_all_data_entered(frame):
#     for widget in frame.winfo_children():
#         if not isinstance(widget, tkinter.Entry):
#             messagebox.askyesnocancel(title="Внимание!", message="Не все данные введены. Хотите продолжить без записи?")
#         if not isinstance(widget, tkinter.ttk.Combobox):
#             messagebox.askyesnocancel(title="Внимание!", message="Не все данные введены. Хотите продолжить без записи?")
def get_key(val, my_dict):
    if val:
        for key, value in my_dict.items():
            if val == value:
                return key
        return "Значение не найдено"

# def get_key(val, my_dict):
#     if hasattr(val, '__len__') and len(val) > 1:
#         val_to_check = val[0] if val else None
#     else:
#         val_to_check = val
#         for key, value in my_dict.items():
#             if val_to_check == value:
#                 return key
#         return "Значение не найдено"


def find_child(frame, child_dict, row, column, cnf=None, width=25):
    selected_name = tk.StringVar()
    combobox_var = ttk.Combobox(frame, textvariable=selected_name, values=list(child_dict.values()), width=width)
    combobox_var.grid(row=row, column=column, columnspan=2, sticky='we', cnf=cnf)

    def on_combobox_key(event):
        value = event.widget.get()
        if value == '':
            combobox_var['values'] = ['']
        else:
            value = value.lower()
            filtered_values = [f"{v}" for k, v in child_dict.items() if value in v.lower()]
            combobox_var['values'] = filtered_values

    def on_combobox_select(event):
        selected_name = combobox_var.get()
        for key, value in child_dict.items():
            if selected_name == f"{value}":
                return key

    combobox_var.bind('<KeyRelease>', on_combobox_key)
    combobox_var.bind('<<ComboboxSelected>>', on_combobox_select)
    return selected_name


def buttons_add_new(self, frame, row):
    tk.Button(frame, text="Назад в меню приема", bg='DarkSlateGray', fg='white',
              command=lambda: self.return_to_start_page(), width=25, height=1).grid(row=row, column=0, columnspan=2,
                                                                                    sticky='e')
    tk.Button(frame, text="Очистить форму", bg='grey', fg='white',
              command=lambda: clear_text(frame), width=15, height=1).grid(row=row, column=2)


def clear_text(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, 'end')
        if isinstance(widget, tk.ttk.Combobox):
            widget.set('')


def select_from_db(frame, db, tbl_name, field_id, field_data, row, column, cnf, columnspan=1, width=30, current=0):
    value_from_db = [v for v in fill_combobox(db, tbl_name, field_id, field_data).values()]
    value_selected = ttk.Combobox(frame, values=value_from_db, state='readonly', width=width)
    if value_selected and tbl_name != 'child_list':
        value_selected.current(current)
        # print(f'{value_selected=} {value_selected.current(0)=} {value_selected.current()}')
    value_selected.grid(row=row, column=column, cnf=cnf, columnspan=columnspan)
    return value_selected


def select_date(frame, year, month, day, row, column, cnf, selectmode='day'):
    date_selected = DateEntry(frame, foreground='black', normalforeground='black', selectforeground='red',
                              background='white', selectmode=selectmode, year=year, month=month, day=day,
                              locale='ru_RU', date_pattern='dd.mm.YYYY')
    date_selected.grid(row=row, column=column, cnf=cnf)
    return date_selected


def check_type_address(registration, fact, residence, fact_as_register, residence_as_fact):
    is_registration = registration and (
            not (fact_as_register or residence_as_fact) or fact_as_register or residence_as_fact)
    is_fact = fact and (not (fact_as_register or residence_as_fact) or residence_as_fact or fact_as_register)
    is_residence = residence and (not (fact_as_register or residence_as_fact) or residence_as_fact or fact_as_register)

    if fact_as_register:
        if is_registration:
            is_fact = is_registration
        elif is_fact:
            is_registration = is_fact

    if residence_as_fact:
        if is_residence:
            is_fact = is_residence
        elif is_fact:
            is_residence = is_fact

    if fact_as_register and residence_as_fact and (registration or fact or residence):
        is_registration, is_fact, is_residence = True, True, True

    return is_registration, is_fact, is_residence


def button_cancel(win):
    btn_cancel = ttk.Button(win, text='Закрыть', command=lambda: win.destroy())
    btn_cancel.place(x=250, y=130)


def show_entries(win):
    var_field_1 = ttk.Entry(win, width=45)
    var_field_1.place(x=200, y=30)
    var_field_2 = ttk.Entry(win, width=45)
    var_field_2.place(x=200, y=60)
    return var_field_1, var_field_2


# def go_to_next_entry(event, entry_list, this_index):
#     next_index = (this_index + 1) % len(entry_list)
#     entry_list[next_index].focus_set()
#
#
# def next_entries(frame):
#     entries = [child for child in frame.winfo_children() if isinstance(child, ttk.Entry)]
#     for idx, entry in enumerate(entries):
#         entry.bind('<Return>', lambda e, idx_=idx: go_to_next_entry(e, entries, idx_))

def go_to_next_entry(event, entry_list, this_index):
    next_index = this_index + 1
    if next_index < len(entry_list):
        entry_list[next_index].focus_set()


def next_entries(frame):
    entries = [child for child in frame.winfo_children() if isinstance(child, ttk.Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', partial(go_to_next_entry, entry_list=entries, this_index=idx))


def create_labels_in_grid(win, label_info_list):
    for label_info in label_info_list:
        text = label_info.get('text', 'Ярлык не задан')
        row = label_info.get('row', 0)
        column = label_info.get('column', 0)

        ttk.Label(win, text=text).grid(row=row, column=column, cnf=CONF)



# if __name__ == '__main__':
#     insert_into_table(building, DB_DICT[building], ['aa', 'bb'])


if __name__ == '__main__':
    pass
