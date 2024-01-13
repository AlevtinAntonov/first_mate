import tkinter as tk
from tkinter import ttk

from app_model.db.db_query import query_read_birth_certificate, query_read_address_reg
from app_model.variables import LARGE_FONT, fields_names
from app_view.gui_input_window import Gui

from app_view_model.functions.update_child import ChildDataApp
from app_view_model.functions.update_datas import query_tab_birth_certificate, query_child_doc_move_reg_adr


class NewPersonalDatas(Gui):
    def __init__(self, width: str = '800', height: str = '600'):
        super().__init__(width, height)
        self.root.geometry(f"{width}x{height}")

    def create_widgets(self):
        self.child_name_var = tk.StringVar()
        # Frame для размещения заголовка окна
        title_frame = tk.Frame(self.root)
        title_frame.pack()

        # Заголовок окна
        title_label = tk.Label(title_frame, text="Личные дела воспитанников", font=LARGE_FONT)
        title_label.pack()


        # Создание вкладок
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Verdana", 11), padding=[5, 5])
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill="both")

        self.tab_birth_certificate = ttk.Frame(tab_control)
        self.tab_address = ttk.Frame(tab_control)
        tab_referral = ttk.Frame(tab_control)
        tab_personal_datas = ttk.Frame(tab_control)
        tab_compensation = ttk.Frame(tab_control)
        tab_family = ttk.Frame(tab_control)

        tab_control.add(self.tab_birth_certificate, text='Св-во о рождении')
        tab_control.add(self.tab_address, text='Адрес')
        tab_control.add(tab_personal_datas, text='Личное дело')
        tab_control.add(tab_compensation, text='Компенсация')
        tab_control.add(tab_family, text='Семья')
        tab_control.add(tab_referral, text='Направление')

        # вкладка tab_birth_certificate
        ChildDataApp(self.tab_birth_certificate, 'birth_certificate', query_read_birth_certificate, query_tab_birth_certificate)

        # вкладка tab_address
        ChildDataApp(self.tab_address, 'addresses', query_read_address_reg, query_child_doc_move_reg_adr)


        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        self.close_button = tk.Button(buttons_frame, text="Закрыть", bg='DarkSlateGray', fg='white',
                                      command=self.return_to_start_page)
        self.close_button.pack(padx=10, pady=10)

    # def refresh_combobox_data(self, table_name):
    #     if table_name == 'child':
    #         query = (f"SELECT CHILD.CHILD_ID, PERSON.LAST_NAME, PERSON.FIRST_NAME, PERSON.PATRONYMIC FROM {table_name} "
    #                  f"JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID ")
    #     with db as cur:
    #         cur.execute(query)
    #         rows = cur.fetchall()
    #         user_data = ["{} {} {} - {}".format(row[1], row[2], row[3], row[0]) for row in rows]
    #         self.combobox['values'] = user_data
    #
    # def on_combobox_select(self, event, query):
    #     combo_selection = self.combobox.get().split(' - ')
    #     if len(combo_selection) < 2:
    #         return
    #     self.child_id = combo_selection[-1]
    #     with db as cur:
    #         cur.execute(query, (self.child_id,))
    #         child_selected = cur.fetchone()
    #         if child_selected:
    #             for i, label in enumerate(self.labels):
    #                 if child_selected[i] and isinstance(child_selected[i], date):
    #                     label.config(text=f"{child_selected[i].strftime("%d.%m.%Y")}")
    #                 elif child_selected[i] and 85 < len(child_selected[i]) < 171:
    #                     label.config(
    #                         text=f"{child_selected[i][:85]}\n{child_selected[i][85:170]}\n{child_selected[i][170:255]}")
    #                 elif child_selected[i] and 85 < len(child_selected[i]) < 171:
    #                     label.config(text=f"{child_selected[i][:85]}\n{child_selected[i][85:]}")
    #
    #                 else:
    #                     label.config(text=f"{child_selected[i]}")
    #
    # # def update_user_data(self, table_name, child_id, field, new_value):
    # #     with db as cur:
    # #
    # #         cur.execute(f'SELECT person.person_id, gender.gender_id, document.document_id FROM CHILD '
    # #                     f'JOIN PERSON ON CHILD.PERSON_ID = PERSON.PERSON_ID '
    # #                     f'JOIN DOCUMENT ON PERSON.DOCUMENT_ID = DOCUMENT.DOCUMENT_ID '
    # #                     f'JOIN GENDER ON PERSON.GENDER_ID = GENDER.GENDER_ID '
    # #                     f'WHERE CHILD.CHILD_ID = ?;', (child_id,))
    # #         query = f'UPDATE {table_name} SET {field} = ?'
    # #         if table_name == 'person':
    # #             data_id = cur.fetchone()[0]
    # #             query += f", date_of_modify = '{current_timestamp()}'"
    # #         elif table_name == 'document':
    # #             data_id = cur.fetchone()[2]
    # #             query += f", date_of_modify = '{current_timestamp()}'"
    # #         elif table_name == 'gender':
    # #             data_id = cur.fetchone()[1]
    # #         query += f" WHERE {table_name}_id = ?;"
    # #         print(query, new_value, data_id)
    # #         cur.execute(query, (new_value, data_id))
    #
    # def on_combobox_select(self, event, table_name):
    #     combo_selection = self.combobox.get().split(' - ')
    #     if len(combo_selection) < 2:
    #         return
    #     self.child_id = combo_selection[-1]
    #     with db as cur:
    #         cur.execute(query_read_birth_certificate, (self.child_id,))
    #         child_selected = cur.fetchone()
    #         if child_selected:
    #             for i, label in enumerate(self.labels):
    #                 if child_selected[i] and isinstance(child_selected[i], date):
    #                     label.config(text=f"{child_selected[i].strftime("%d.%m.%Y")}")
    #                 elif child_selected[i] and 85 < len(child_selected[i]) < 171:
    #                     label.config(
    #                         text=f"{child_selected[i][:85]}\n{child_selected[i][85:170]}\n{child_selected[i][170:255]}")
    #                 elif child_selected[i] and 85 < len(child_selected[i]) < 171:
    #                     label.config(text=f"{child_selected[i][:85]}\n{child_selected[i][85:]}")
    #
    #                 else:
    #                     label.config(text=f"{child_selected[i]}")
    #
    # def create_labels(self, tab):
    #     for i, field in enumerate(fields_names[self.key_name]):
    #         tk.Label(tab, text=field[0]).grid(row=i * 2 + 2, column=0, sticky='W', padx=20)
    #         label = ttk.Label(tab, text="-", background="white", width=86)
    #         label.grid(row=i * 2 + 2, column=1, sticky='W', padx=10)
    #
    #         # Use default argument for lambda function to capture the current value of i
    #         label.bind("<Double-1>",
    #                    lambda event, idx=i, table_name=field[3], table_dict=field[4], field=field[1],
    #                           field_type=field[2], label=label: self.on_label_double_click(event, idx, table_name,
    #                                                                                        table_dict, field,
    #                                                                                        field_type, label))
    #
    #         self.labels.append(label)
    #
    # def on_label_double_click(self, event, idx, table_name, table_dict, field, field_type, label):
    #     user_id = self.combobox.get().split(' - ')[-1]
    #     if field_type == 'Combobox':
    #         top = tk.Toplevel(self.tab_birth_certificate)
    #         top.title("Выбор из справочника")
    #         top.geometry('300x100')
    #         position_center(top, 250, 100)
    #         top.grab_set()
    #
    #         new_data = tk.StringVar()
    #         new_data.set(label.cget("text"))
    #         value_from_db = [v for v in
    #                          fill_combobox(db, table_dict, DB_DICT[table_dict][0], DB_DICT[table_dict][1]).values()]
    #
    #         combobox = ttk.Combobox(top, textvariable=new_data, values=value_from_db, width=30)
    #         combobox.pack(pady=10)
    #
    #         button = ttk.Button(top, text="Сохранить",
    #                             command=lambda: self.save_data_from_top(table_name, user_id, field,
    #                                                                     find_id(db, table_dict, DB_DICT[table_dict][0],
    #                                                                             DB_DICT[table_dict][1], new_data.get()),
    #                                                                     top))
    #         button.pack()
    #     elif field_type == 'DateEntry':
    #         # Окно для изменения даты
    #         top = tk.Toplevel(self.tab_birth_certificate)
    #         top.title("Редактирование даты")
    #         top.geometry('300x100')
    #         position_center(top, 300, 100)
    #         top.grab_set()
    #
    #         new_date = DateEntry(top, foreground='black', normalforeground='black', selectforeground='red',
    #                              background='white', selectmode='day', locale='ru_RU', date_pattern='dd.mm.YYYY')
    #         with db as cur:
    #             query = f'SELECT {table_name}.{field} '
    #             query += query_date_entry_child
    #             user_data = cur.execute(query, (user_id,)).fetchone()
    #             default_date = user_data[0].strftime("%d.%m.%Y") if user_data else ''
    #             new_date.set_date(default_date)
    #             new_date.pack(pady=10)
    #
    #         button = ttk.Button(top, text="Сохранить",
    #                             command=lambda: self.save_data_from_top(table_name, user_id, field, new_date.get(),
    #                                                                     top))
    #         button.pack()
    #
    #     else:
    #         new_value = simpledialog.askstring("Редактирование",
    #                                            f"{' ' * 40}Введите новое значение{' ' * 40}",
    #                                            initialvalue=label.cget("text"))
    #         if new_value:
    #             label.config(text=new_value)
    #             update_user_data(table_name, user_id, field, new_value, self.query)
    #             print(table_name)
    #             self.refresh_combobox_data('child')
    #             self.on_combobox_select(None, 'child')
    #
    # def save_data_from_top(self, table_name, user_id, field, new_data, top):
    #     update_user_data(table_name, user_id, field, new_data, self.query)
    #     top.destroy()
    #     self.refresh_combobox_data('child')
    #     self.on_combobox_select(None, 'child')
