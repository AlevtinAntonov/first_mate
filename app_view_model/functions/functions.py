import re
from datetime import datetime
from functools import partial
from os import path
import tkinter as tk
from tkinter import ttk, messagebox

from tkcalendar import DateEntry

from app_model.db.db_query import query_insert_into, DB_DICT, gender, child, referral, query_check_person, \
    query_check_document, building, person, query_find_id, \
    query_insert_into_table_return_id, team, age, focus, mode, benefit
from app_model.variables import CONF


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


# Функция возвращает абсолютный путь к файлу.
def path_to_file(dir_file, file):
    return path.abspath(path.join(dir_file, file))


def fill_combobox_users(db, combobox):
    with db as cur:
        cur.execute("SELECT LAST_NAME, INITIALS FROM USERS")
        data = cur.fetchall()
        values = [f"{initials}{last_name}" for last_name, initials in data]  # объединение фамилии с инициалами
        combobox['values'] = values


# Функция возвращает значения из таблиц базы для комбобокса.
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
            [dict_combo.update({row[0]: (' '.join((row[1], row[2], row[3])), row[4], row[5])}) for row in
             cur.fetchall()]
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


# Функция возвращает id или False
def find_id(db, tbl_name, field_id, field_data, field_value):
    for k, v in fill_combobox(db, tbl_name, field_id, field_data).items():
        if v == field_value:
            return k
    return False


# Функция проверяет есть ли такая запись в базе данных
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


# Функция возвращает id человека или False.
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


# Формат текущей даты и времени для записи в базу данных
def current_timestamp():
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    return date_time.strftime("%d.%m.%Y %H:%M")


#  Форматирует написание ФИО с заглавной буквы
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




def check_russian_letters(input_str):
    import re
    return bool(re.search("[а-яА-Я -]", input_str))


def on_validate_input(new_text):
    return check_russian_letters(new_text)


def insert_into_table(db, table_name, fields, values):
    # Формирование SQL-запроса для вставки данных
    placeholders = ', '.join(['?'] * len(fields))
    query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({placeholders})"
    # Подключение к базе данных
    with db as cur:
        cur.execute(query, values)


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


#  Get key from dictionary via entering value
def get_key(val, my_dict):
    if val:
        for key, value in my_dict.items():
            if val == value:
                return key
        return "Значение не найдено"


#  Find child in database table
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
              command=lambda: self.return_to_start_page(), width=25, height=1).grid(row=row, column=0, columnspan=1,
                                                                                    sticky='e')
    tk.Button(frame, text="Очистить форму", bg='grey', fg='white',
              command=lambda: clear_text(frame), width=15, height=1).grid(row=row, column=1)


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


def button_cancel(win, x=250, y=130):
    btn_cancel = ttk.Button(win, text='Закрыть', command=lambda: win.destroy())
    btn_cancel.place(x=x, y=y)


def show_entries(win):
    var_field_1 = ttk.Entry(win, width=45)
    var_field_1.place(x=200, y=30)
    var_field_2 = ttk.Entry(win, width=45)
    var_field_2.place(x=200, y=60)
    return var_field_1, var_field_2


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


if __name__ == '__main__':
    pass
