from app_model.db.db_connect import DB
from app_model.db.db_query import query_insert_into_table_return_id, person, DB_DICT, child, query_find_id, building, \
    benefit, document, query_child_person_id, address, query_insert_into, person_address
from app_model.variables import CONF_D_W
from app_view_model.functions.find_address import find_full_addresses
from app_view_model.functions.format_address import format_address
from app_view_model.functions.functions import current_timestamp, check_if_exists, find_person, find_id, select_from_db, \
    fill_combobox, get_key, find_child

db = DB('C:/Users/anton/PycharmProjects/first_mate/app_model/db/DB_PROD.FDB')
# with db as cur:
# query_add_address = query_insert_into_table_return_id(address, address) % DB_DICT[address]
# print(query_add_address)

# query_person_address = query_insert_into(person_address) % DB_DICT[person_address]
# print(query_person_address)
# document_assembly_record = None
# # Add document of parent to table DOCUMENT and return document_id for table PERSON
# query_add_doc = query_insert_into_table_return_id(document, document) % DB_DICT[document]
# print(query_add_doc)
# cur.execute(query_add_doc, ('0000', '123456', 'document_issued_by', '10.10.2005',
#                             '10.10.2050', 1, current_timestamp(), document_assembly_record))
# # document_id from table DOCUMENT
# document_id = cur.fetchone()[0]
# print(document_id)

# cur.execute(query_child_person_id, (22,))
# person_id = cur.fetchone()[0]
# print(f'{person_id=}')

# query = query_insert_into_person(person) % DB_DICT[person]
# print(query)
# with db as cur:
#     cur.execute(query, ('13name', 't_name', 'ronymic', '01.01.2019', 1, current_timestamp()))
#     person_id = cur.fetchone()[0]
#     print(person_id)
#     query_add_child = query_insert_into_person(child) % DB_DICT[child]
#     print(query_add_child, person_id)
#     cur.execute(query_add_child, (person_id, current_timestamp()))
#     child_id = cur.fetchone()[0]
#     print(child_id)

# person_id2 = check_if_exists(db, person, '13name', 't_name', 'ronymic', '01.01.2019')
# print(person_id2)

# query = (query_find_id % child)
# print(query)
# with db as cur:
#     # cur.execute("""SELECT * FROM child WHERE (person_id = 14);""")
#     cur.execute(query, (14,))
#     a = cur.fetchone()
#     print(a[0])

# person_id2 = 14
# child_id2 = find_person(db, child, person_id2)
# print(person_id2, child_id2)

# print(DB_DICT[building][0], DB_DICT[building][1])
# building_id = find_id(db, building, DB_DICT[building][0], DB_DICT[building][1], buildings)
############################
# import tkinter as tk
# from tkinter import ttk
#
# def on_combobox_keyrelease(event):
#     value = event.widget.get()
#     if value == '':
#         combobox['values'] = value_from_db
#         combobox.set('')
#     else:
#         value = value.lower()
#         filtered_values = [x for x in value_from_db if value in x.lower()]
#         combobox['values'] = filtered_values
#         if len(filtered_values) > 0:
#             combobox.set(filtered_values[0])
#
#
# root = tk.Tk()
# value_from_db = [v for v in fill_combobox(db,  benefit, DB_DICT[benefit][0], DB_DICT[benefit][1]).values()]
#
# # benefit_id = select_from_db(root, db, benefit, DB_DICT[benefit][0], DB_DICT[benefit][1], 20, 1, CONF_D_W, 2)
# # original_values = ['Apple', 'Banana', 'bannana','Cherry', 'Durian', 'Elderberry', 'Fig', 'Grape']
# combobox = ttk.Combobox(root, values=value_from_db)
# combobox.pack()
# combobox.bind('<KeyRelease>', on_combobox_keyrelease)
#
# root.mainloop()
###############################
import tkinter as tk
from tkinter import ttk

# Пример словаря
# data = {
#     1: ('Иванов', 'Иван', 'Иванович'),
#     2: ('Петров', 'Петр', 'Петрович'),
#     3: ('Сидоров', 'Сидор', 'Сидорович'),
#     4: ('Сидоров', 'виктор', 'Сидорович')
# }

# def select_from_db(frame, db, tbl_name, field_id, field_data, row, column, cnf, columnspan=1, width=30):
#     value_from_db = [v for v in fill_combobox(db, tbl_name, field_id, field_data).values()]
#     value_selected = ttk.Combobox(frame, values=value_from_db, state='readonly', width=width)
#     if value_selected and tbl_name != 'child_list':
#         value_selected.current(0)
#         # print(f'{value_selected=} {value_selected.current(0)=} {value_selected.current()}')
#     value_selected.grid(row=row, column=column, cnf=cnf, columnspan=columnspan)
#     return value_selected


# def find_child(child_dict):

# def on_combobox_key(event):
#     value = event.widget.get()
#     if value == '':
#         combobox_var['values'] = ['']
#     else:
#         value = value.lower()
#         filtered_values = [f"{v}" for k, v in child_dict.items() if value in v.lower()]
#         combobox_var['values'] = filtered_values
#
#
# def on_combobox_select(event):
#     selected_value = combobox_var.get()
#     for key, value in child_dict.items():
#         if selected_value == f"{value}":
#             return key

# def get_key(val, my_dict):
#     for key, value in my_dict.items():
#         if val == value:
#             return key
#     return "Значение не найдено"
#
# root = tk.Tk()
# combobox_var = ttk.Combobox(root)
# combobox_var.pack()
# child_dict = fill_combobox(db, 'child_list', None, None)
#
# aaa = find_child(combobox_var, child_dict)
# print(get_key(aaa, child_dict))
# print(f'{keyword=}')
# combobox_var.bind('<Enter>', print(f'{keyword=}'))

# combobox_var.bind('<KeyRelease>', on_combobox_key)
# combobox_var.bind('<<ComboboxSelected>>', lambda event: (on_combobox_select, print(f'{get_key(combobox_var.get(), child_dict)=}')))

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
# def create_combobox(data, combobox):
#     def on_combobox_key(event):
#         value = event.widget.get()
#         if value == '':
#             combobox['values'] = ['']
#         else:
#             value = value.lower()
#             filtered_values = [f"{v[0]} {v[1]} {v[2]}" for k, v in data.items() if value in ' '.join(v).lower()]
#             combobox['values'] = filtered_values
#
#     def on_combobox_select(event):
#         selected_value = combobox.get()
#         for key, value in data.items():
#             if selected_value == f"{value[0]} {value[1]} {value[2]}":
#                 return key
#
#     combobox.bind('<KeyRelease>', on_combobox_key)
#
#     def on_select(event):
#         person_id = on_combobox_select(event)
#         print(f"Person_id: {person_id}")
#         return person_id
#
#     def on_select_and_print(event):  # Добавление нового обработчика события
#         person_id = on_select(event)
#         print(f"Selected person id: {person_id}")  # Вывод значения person_id за пределами функции
#
#     combobox.bind('<<ComboboxSelected>>', on_select_and_print)  # Привязка нового обработчика события
#
# root = tk.Tk()
#
# data = {
#     1: ('Иванов', 'Иван', 'Иванович'),
#     2: ('Петров', 'Петр', 'Петрович'),
#     3: ('Сидоров', 'Сидор', 'Сидорович')
# }
#
# combobox = ttk.Combobox(root)
# combobox.pack()
#
# create_combobox(data, combobox)
#
# root.mainloop()
# import tkinter as tk
# from tkinter import ttk
#
#
# def search_person(data, combobox):
#     def on_combobox_key(event):
#         value = event.widget.get().lower()
#         if value == '':
#             combobox['values'] = list(data.keys())
#         else:
#             filtered_values = [f"{v[0]} {v[1]} {v[2]}" for k, v in data.items() if value in ' '.join(v).lower()]
#             combobox['values'] = filtered_values
#
#     def on_combobox_select(event):
#         selected_value = combobox.get()
#         for key, value in data.items():
#             if selected_value == f"{value[0]} {value[1]} {value[2]}":
#                 return key
#
#     combobox.bind('<KeyRelease>', on_combobox_key)
#
#     def on_select_and_print(event):
#         person_id = on_combobox_select(event)
#         print(f"Selected person id: {person_id}")
#         return person_id
#
#     combobox.bind('<<ComboboxSelected>>', on_select_and_print)
#
#
#
#
# root = tk.Tk()
#
# data = {
#     1: ('Иванов', 'Иван', 'Иванович'),
#     2: ('Петров', 'Петр', 'Петрович'),
#     3: ('Сидоров', 'Сидор', 'Сидорович')
# }
#
# combobox = ttk.Combobox(root)
# combobox.pack()
#
# search_person(data, combobox)
# person_id = on_combobox_select(event)
#
# root.mainloop()

# import tkint

# import tkinter as tk
# from tkinter import ttk
#
# def validate_combobox(combobox, label):
#     if combobox.get() == '':
#         label.config(borderwidth=2, relief="solid", foreground='red')
#     else:
#         label.config(borderwidth=0, relief="flat", foreground='black')
#
# root = tk.Tk()
#
# label1 = ttk.Label(root, text="Выберите значение из списка:")
# label1.pack()
#
# combobox1 = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'])
# combobox1.pack()
#
# button = tk.Button(root, text="Проверить", command=lambda: validate_combobox(combobox1, label1))
# button.pack()
#
# root.mainloop()

# import tkinter as tk
# from tkinter import ttk
#
# def validate_combobox(event):
#     if combobox.get() == '':
#         label.config(foreground='red')
#     else:
#         label.config(foreground='black')
#
# root = tk.Tk()
#
# label = ttk.Label(root, text="Выберите значение из списка:", foreground='red')
# label.pack()
#
# combobox = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'])
# combobox.bind("<<ComboboxSelected>>", validate_combobox)
# combobox.pack()
#
# root.mainloop()
# def format_address_specific(address_dict):
#     ignored_keys = ['address_type_id', 'is_registration', 'is_fact', 'is_residence']
#     values = [str(value).strip() for key, value in address_dict.items() if key not in ignored_keys and str(value).strip()]
#     formatted_address = ', '.join(values)
#     return formatted_address
#
# # Пример словаря
# address = {'address_type_id': 1, 'zipcode': '123456', 'region': 'РФ', 'region_type_id': 1, 'district': '', 'town': 'Москва', 'town_type_id': 1, 'locality': '', 'locality_type_id': 0, 'street': 'Ленина', 'street_type_id': 1, 'house': '1', 'house_body': '2', 'house_liter': 'в', 'house_building': '   25', 'flat': '  656', 'is_registration': True, 'is_fact': False, 'is_residence': False}
# formatted = format_address_specific(address)
# print(formatted)  # Вывод: "123456, РФ, Москва, Ленина, 1, 2в, 25, 656"
#
# address_type_id
# zipcode
# region
# region_type_id
# district
# town
# town_type_id
# locality
# locality_type_id
# street
# street_type_id
# house
# house_body
# house_liter
# house_building
# flat
# is_registration
# is_fact
# is_residence
# is_visible
query = """
SELECT 
    a.zipcode, 
    a.region, 
    rt.region_type_name_short, 
    a.district, 
    a.town, 
    tt.town_type_name_short, 
    a.locality, 
    lt.locality_type_name_short, 
    a.street, 
    st.street_type_name_short, 
    a.house, 
    a.house_body, 
    a.house_liter, 
    a.house_building, 
    a.flat
FROM 
    PERSON_ADDRESS pa
JOIN 
    ADDRESS a ON pa.ADDRESS_ID = a.ADDRESS_ID
JOIN 
    ADDRESS_TYPE ad ON a.ADDRESS_TYPE_ID = ad.ADDRESS_TYPE_ID
JOIN 
    REGION_TYPE rt ON a.REGION_TYPE_ID = rt.REGION_TYPE_ID
JOIN 
    TOWN_TYPE tt ON a.TOWN_TYPE_ID = tt.TOWN_TYPE_ID
JOIN 
    LOCALITY_TYPE lt ON a.LOCALITY_TYPE_ID = lt.LOCALITY_TYPE_ID
JOIN 
    STREET_TYPE st ON a.STREET_TYPE_ID = st.STREET_TYPE_ID
WHERE 
    pa.PERSON_ID = ?
    AND pa.IS_VISIBLE = True
    AND a.%s  = True;"""
with db as cur:
    try:
        adrs = cur.execute(query % ('is_fact',), (29,)).fetchone()
        print(type(list(adrs)), adrs)
    except Exception as e:
        print(f'Ошибка! - {e}')


# def format_address(address_list):
#     if address_list[0] != "" and address_list[0] is not None:
#         formatted_list = address_list[0]
#     if address_list[1] != "" and address_list[1] is not None:
#         formatted_list += ', ' + address_list[1]
#         if address_list[2] != "" and address_list[2] is not None:
#             formatted_list += ' ' + address_list[2]
#     if address_list[3] != "" and address_list[3] is not None:
#         formatted_list += ', ' + address_list[3] + 'р-н'
#     if address_list[4] != "" and address_list[4] is not None:
#         formatted_list += ', ' + address_list[4] + ' ' + address_list[5]
#     if address_list[6] != "" and address_list[6] is not None:
#         formatted_list += ', ' + address_list[6] + ' ' + address_list[7]
#     if address_list[8] != "" and address_list[8] is not None:
#         formatted_list += ', ' + address_list[8] + ' ' + address_list[9]
#     if address_list[10] != "" and address_list[10] is not None:
#         formatted_list += ', д.' + address_list[10]
#     if address_list[11] != "" and address_list[11] is not None:
#         formatted_list += ', корп.' + address_list[11]
#     if address_list[12] != "" and address_list[12] is not None:
#         formatted_list += ', лит.' + address_list[12]
#     if address_list[13] != "" and address_list[13] is not None:
#         formatted_list += ', стр.' + address_list[13]
#     if address_list[14] != "" and address_list[14] is not None:
#         formatted_list += ', кв.' + address_list[14]
#     return formatted_list


# address_without_empty = [elem for elem in list(address_tuple) if elem and elem != "" and elem is not None]
# print(address_without_empty)
# formatted = ', '.join(address_without_empty)
print(format_address(adrs))  # Вывод: "197375, Санкт-Петербург, Вербная ул. 20/3, А, кв. 300"
address_list2 = (
'197375', 'Санкт-Петербург', None, '', 'Санкт-Петербург', 'г.', '', None, 'Вербная', 'ул.', '20/3', '', 'А', '', '300')
formatted = format_address(adrs)
print(formatted)

dict_address = {
    'д.': None,
    'корп.': None,
    'лит.': None,
    'стр.': None,
    'кв.': None,
}


def dict_to_string(dictionary):
    result = ""
    for key, value in dictionary.items():
        if value != '' and value is not None:
            result += f"{key} {value}, "
    return result.rstrip(", ")

print(dict_to_string(dict_address))

def assign_values(dictionary, lst):
    keys = list(dictionary.keys())
    values = lst[-5:]
    for i in range(5):
        dictionary[keys[i]] = values[i] if values[i] != '' and values[i] is not None else None
    return dictionary

lst = ['г.', '', None, 'Вербная', 'ул.', '20/3', '', 'А', '', '300']
dict_address = {
    'д.': None,
    'корп.': None,
    'лит.': None,
    'стр.': None,
    'кв.': None,
}

# dict_address = assign_values(dict_address, lst)
# print(dict_address)
# print(dict_to_string(dict_address))

p = find_full_addresses(db, 29)
for k, v in p.items():
    if v[1]:
        print(k, v)
