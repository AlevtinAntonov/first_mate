import tkinter as tk
from datetime import date
# import pathlib
# from pathlib import Path
MAIN_TITLE = "Помощник 3.23.12.01 "


ICO_DIRECTORY = ''
MAIN_ICO = "app_model/ico/mate.ico"
START_IMAGE = 'app_model/ico/girl.png'
ADD_PNG = 'app_model/ico/add.png'
DELETE_PNG = 'app_model/ico/delete.png'
EDIT_PNG = 'app_model/ico/edit.png'
REFRESH_PNG = 'app_model/ico/refresh.png'
SEARCH_PNG = 'app_model/ico/search.png'

DB_DIR = 'app_model'
DB_SUB_DIR = 'db'
DB_NAME = 'DB_PROD.FDB'
ORGANIZATION_SHORT_NAME = "ГБДОУ дс № ХХ"

LARGE_FONT = ("Verdana", 12)
CONF = {'padx': 5, 'pady': 2, 'sticky': 'W'}
CONF_DATA = {'bg': 'white', 'relief': tk.GROOVE}
CONF_D_W = {'padx': 5, 'pady': 2, 'sticky': 'W'}
CURRENT_YEAR = date.today().year
CURRENT_MONTH = date.today().month
CURRENT_DAY = date.today().day
DEFAULT_REFERRAL_NUMBER = "-23-к"
DEFAULT_CONTRACT_BEGIN_DATE = '01.09.2023'
DEFAULT_YEAR = 2023
DEFAULT_MONTH = 9
DEFAULT_DAY = 1
DEFAULT_BORN_YEAR = 2015
DEFAULT_BORN_MONTH = 1
DEFAULT_BORN_DAY = 1
DEFAULT_PARENT_BORN_YEAR = 2000

ADDRESS_GEOMETRY = '800x450'

label_referral_list = [
    {'text': 'Направление № ', 'row': 2, 'column': 0},
    {'text': 'Фамилия', 'row': 4, 'column': 0},
    {'text': 'Имя', 'row': 4, 'column': 2},
    {'text': 'Отчество', 'row': 6, 'column': 0},
    {'text': 'Пол', 'row': 8, 'column': 0},
    {'text': 'Дата рождения', 'row': 8, 'column': 2},
    {'text': 'Площадка №', 'row': 10, 'column': 0},
    {'text': 'Возрастная группа', 'row': 12, 'column': 0},
    {'text': 'Направленность', 'row': 14, 'column': 0},
    {'text': 'Режим работы', 'row': 16, 'column': 0},
    {'text': 'Дата начала обучения', 'row': 18, 'column': 0},
    {'text': 'Льгота по направлению', 'row': 20, 'column': 0},
    {'text': 'Группа план', 'row': 22, 'column': 0},
    {'text': 'Примечание', 'row': 24, 'column': 0},
]

label_parent_list = [
    # {'text': 'ФИО ребенка', 'row': 2, 'column': 0},
    {'text': 'Степень родства', 'row': 3, 'column': 0},
    {'text': 'Фамилия', 'row': 4, 'column': 0},
    {'text': 'Имя', 'row': 6, 'column': 0},
    {'text': 'Отчество', 'row': 8, 'column': 0},
    {'text': 'Пол', 'row': 10, 'column': 0},
    {'text': 'Дата рождения', 'row': 10, 'column': 2},
    {'text': 'Гражданство', 'row': 14, 'column': 0},
    {'text': 'Тип документа', 'row': 16, 'column': 0},
    {'text': 'Серия', 'row': 18, 'column': 0},
    {'text': 'Номер', 'row': 20, 'column': 0},
    {'text': 'Кем выдан', 'row': 22, 'column': 0},
    {'text': 'Дата выдачи', 'row': 24, 'column': 0},
    {'text': 'Действует до (при наличии)', 'row': 26, 'column': 0},
    # {'text': '№ актовой записи (для Св-ва о рожд.)', 'row': 28, 'column': 0},
    {'text': 'Телефон', 'row': 30, 'column': 0},
    {'text': 'Email', 'row': 32, 'column': 0},
    {'text': 'СНИИЛС', 'row': 34, 'column': 0},
    # {'text': 'Адрес регистрации', 'row': 42, 'column': 0},
    # {'text': 'Адрес фактический', 'row': 44, 'column': 0},
    # {'text': 'Адрес рег. по месту пребывания', 'row': 46, 'column': 0},
]

label_address_list = [
    {'text': 'Адрес', 'row': 0, 'column': 1},
    {'text': 'Выберите тип адреса*', 'row': 4, 'column': 0},
    {'text': 'Индекс', 'row': 6, 'column': 0},
    {'text': 'Субъект(республика, край, область)', 'row': 8, 'column': 0},
    {'text': 'Район области', 'row': 10, 'column': 0},
    {'text': 'Город', 'row': 12, 'column': 0},
    {'text': 'Населенный пункт', 'row': 14, 'column': 0},
    {'text': 'Улица', 'row': 16, 'column': 0},
    {'text': 'Дом', 'row': 18, 'column': 0},
    {'text': 'Корпус', 'row': 20, 'column': 0},
    {'text': 'Литера', 'row': 22, 'column': 0},
    {'text': 'Строение', 'row': 24, 'column': 0},
    {'text': 'Квартира', 'row': 26, 'column': 0},
]

label_child_list = [
    # {'text': 'Фамилия', 'row': 2, 'column': 0},
    # {'text': 'Имя', 'row': 4, 'column': 0},
    # {'text': 'Отчество', 'row': 6, 'column': 0},
    # {'text': 'Пол', 'row': 6, 'column': 0},
    # {'text': 'Дата рождения', 'row': 8, 'column': 0},
    # {'text': 'ФИО отца', 'row': 10, 'column': 0},
    # {'text': 'ФИО матери', 'row': 12, 'column': 0},
    {'text': 'Гражданство', 'row': 14, 'column': 0},
    {'text': 'Тип документа', 'row': 16, 'column': 0},
    {'text': 'Место рождения', 'row': 18, 'column': 0},
    {'text': '№ актовой записи (для Св-ва о рожд.)', 'row': 20, 'column': 0},
    {'text': 'Серия', 'row': 22, 'column': 0},
    {'text': 'Номер', 'row': 24, 'column': 0},
    {'text': 'Кем выдан', 'row': 26, 'column': 0},
    {'text': 'Дата выдачи', 'row': 28, 'column': 0},

    {'text': 'СНИИЛС', 'row': 30, 'column': 0},
    # {'text': 'Адрес регистрации', 'row': 42, 'column': 0},
    # {'text': 'Адрес фактический', 'row': 44, 'column': 0},
    # {'text': 'Адрес рег. по месту пребывания', 'row': 46, 'column': 0},
]