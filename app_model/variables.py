import tkinter as tk
from datetime import date

MAIN_TITLE = "Помощник 3.24.01.01 "

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
FONT = ("Verdana", 10)
CONF = {'padx': 5, 'pady': 2, 'sticky': 'W'}
CONF_EW = {'padx': 5, 'pady': 2, 'sticky': 'nsew'}
CONF_DATA = {'bg': 'white', 'relief': tk.GROOVE}
CONF_D_W = {'padx': 5, 'pady': 2, 'sticky': 'W'}
CONF_GRID_WIDTH = {'padx': 5, 'pady': 2, 'sticky': 'ew', 'columnspan': 2}
CONF_0 = {'padx': 0, 'pady': 0}
CURRENT_YEAR = date.today().year
CURRENT_MONTH = date.today().month
CURRENT_DAY = date.today().day
DEFAULT_REFERRAL_NUMBER = "-24-к"
DEFAULT_CONTRACT_BEGIN_DATE = '01.09.2024'
DEFAULT_YEAR = 2024
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
    {'text': 'СНИИЛС (11 цифр)', 'row': 34, 'column': 0},
    # {'text': 'Адрес регистрации', 'row': 42, 'column': 0},
    # {'text': 'Адрес фактический', 'row': 44, 'column': 0},
    # {'text': 'Адрес рег. по месту пребывания', 'row': 46, 'column': 0},
]

label_address_list = [
    # {'text': 'Адрес', 'row': 0, 'column': 1},
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
    {'text': 'Район Санкт-Петербурга', 'row': 28, 'column': 0},
]
town_districts = {
    'Адмиралтейский': 1,
    'Василеостровский': 2,
    'Выборгский': 3,
    'Калининский': 4,
    'Кировский': 5,
    'Колпинский': 6,
    'Красногвардейский': 7,
    'Красносельский': 8,
    'Кронштадтский': 9,
    'Курортный': 10,
    'Ломоносовский': 11,
    'Московский': 12,
    'Невский': 13,
    'Павловский': 14,
    'Петроградский': 15,
    'Петродворцовый': 16,
    'Приморский': 17,
    'Пушкинский': 18,
    'Фрунзенский': 19,
    'Центральный': 20,
}

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

    {'text': 'СНИИЛС (11 цифр)', 'row': 30, 'column': 0},
    # {'text': 'Адрес регистрации', 'row': 42, 'column': 0},
    # {'text': 'Адрес фактический', 'row': 44, 'column': 0},
    # {'text': 'Адрес рег. по месту пребывания', 'row': 46, 'column': 0},
]

references_dict = {
    "focus": (
        "Направленность обучения", (['', 0], ['Направленность кратко', 290], ['Полное наименование', 290]), [50, 200],
        [30, 60]),
    "document_type": (
        "Тип документа", (['', 0], ['Тип документа кратко', 290], ['Полное наименование', 290]), [50, 200],
        [30, 60]),
    "age": ("Возрастная группа", (
        ['ID', 50], ['Группа', 130], ['Наименование возраста', 210], ['Мин.лет', 60],
        ['Макс.лет', 60], ['Срок договора', 70])),
    "users": ("Пользователи", (
        ['', 0], ['Логин', 70], ['Пароль', 70], ['Фамилия', 120], ['Имя', 120], ['Отчество', 120], ['Админ', 80]
    )),
    "mode": ("Режим пребывания", (['', 0], ['Режим кратко', 290], ['Полное наименование', 290])),
    "benefit": ("Льгота по направлению", [['', 0], ['Льгота кратко', 290], ['Полное наименование', 290]]),
    "citizenship": ("Гражданство", (['', 0], ['Гражданство кратко', 250], ['Полное наименование', 330])),
    "building": (
        "Здание/площадка", (['', 0], ['Номер площадки', 250], ['Название площадки', 330]), [50, 200], [30, 60]),
    "team": (
        "Группа", (['', 0], ['Название группы', 180], ['Возраст ID', 100], ['Организация ID', 100],
                   ['Здание ID', 100])),
}

label_compensation = [
    {'text': 'ФИО заявителя', 'row': 6, 'column': 0},
    {'text': 'Номер заявления', 'row': 7, 'column': 0},
    {'text': 'Дата подачи заявления', 'row': 8, 'column': 0},
    {'text': 'Основание компенсации', 'row': 10, 'column': 0},
    {'text': 'Дата начала компенсации', 'row': 12, 'column': 0},
    {'text': 'Дата окончания компенсации', 'row': 14, 'column': 0},
    {'text': 'Наименование документа 1', 'row': 16, 'column': 0},
    {'text': 'Реквизиты документа 1', 'row': 18, 'column': 0},
    {'text': 'Наименование документа 2', 'row': 20, 'column': 0},
    {'text': 'Реквизиты документа 2', 'row': 22, 'column': 0},
    {'text': 'Наименование документа 3', 'row': 24, 'column': 0},
    {'text': 'Реквизиты документа 3', 'row': 26, 'column': 0},
    {'text': 'Наименование документа 4', 'row': 28, 'column': 0},
    {'text': 'Реквизиты документа 4', 'row': 30, 'column': 0},
    {'text': 'Наименование документа 5', 'row': 32, 'column': 0},
    {'text': 'Реквизиты документа 5', 'row': 34, 'column': 0},
    {'text': 'Наименование документа 6', 'row': 36, 'column': 0},
    {'text': 'Реквизиты документа 6', 'row': 38, 'column': 0},
]

label_agreement = [
    # {'text': 'Номер направления', 'row': 6, 'column': 0},
    {'text': 'ФИО родителя в договоре', 'row': 14, 'column': 0},
    {'text': 'Группа план', 'row': 15, 'column': 0},
    {'text': 'Номер заявления о приеме', 'row': 16, 'column': 0},
    {'text': 'Дата заявления о приеме', 'row': 18, 'column': 0},
    {'text': 'Плановая дата прихода в группу', 'row': 20, 'column': 0},
    {'text': 'Номер договора', 'row': 22, 'column': 0},
    {'text': 'Дата договора', 'row': 24, 'column': 0},
    {'text': 'Дата начала договора', 'row': 26, 'column': 0},
    {'text': 'Приказ о зачислении №', 'row': 28, 'column': 0},
    {'text': 'Приказ о зачислении дата', 'row': 30, 'column': 0},
    {'text': 'Приказ об отчислении №', 'row': 32, 'column': 0},
    {'text': 'Приказ об отчислении дата', 'row': 34, 'column': 0},
]
