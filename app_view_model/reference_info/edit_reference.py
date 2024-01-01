import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.variables import LARGE_FONT, CONF_D_W, references_dict, MAIN_ICO
from app_view_model.functions.functions import position_center, next_entries, button_cancel
from app_view_model.reference_info.functions import get_column_names, get_edit_record
from app_view_model.reference_info.reference_page import ReferencePage


class EditReference(ReferencePage):
    def __init__(self, width: str, height: str, data_dict: dict, table_name: str):
        super().__init__(width, height)
        self.table_name = table_name
        self.data_dict = data_dict
        self.max_columns = 3
        if self.table_name == 'age':
            self.max_columns = 6  # Максимальное количество столбцов, которые можно использовать в запросе
        elif self.table_name == 'users':
            self.max_columns = 7
        self.show_tree(self.data_dict)
        self.view_records()

    def show_tree(self, data_dict):
        tk.Label(self.root, text=references_dict[self.table_name][0], font=LARGE_FONT).grid(row=0, column=0,
                                                                                            cnf=CONF_D_W,
                                                                                            columnspan=5,
                                                                                            sticky="nsew")
        # Добавление Treeview
        columns = [f"column_{i}" for i in range(len(data_dict))]
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for i, (column_key, (column_name, column_width)) in enumerate(data_dict.items()):
            self.tree.heading(columns[i], text=column_name)
            self.tree.column(columns[i], minwidth=0, width=column_width)
        self.tree.grid(row=5, columnspan=5)

        # Добавление Scrollbar
        tree_scroll_y = tk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        tree_scroll_y.grid(row=5, column=5, sticky="ns")
        self.tree.configure(yscrollcommand=tree_scroll_y.set)

        self.tree.bind("<Double-1>", self.OnDoubleClick)

    def OnDoubleClick(self, event):
        self.tree.set(self.tree.selection()[0], '#1')
        self.edit_data()

    def view_records(self):
        with db as cur:
            column_names = get_column_names(cur, self.table_name)
            cur.execute(
                "SELECT * FROM %s WHERE is_visible ORDER BY %s ASC;" % (self.table_name, column_names[0]))
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cur.fetchall()]

    def open_toplevel_window(self, window_title, lambda_function):
        top = tk.Toplevel()
        if self.table_name == 'users':
            top.geometry('500x340')
        else:
            top.geometry('500x170')
        position_center(top, 500, 170)
        top.title(window_title)
        top.iconbitmap(MAIN_ICO)

        top.resizable(False, False)

        if lambda_function.__name__ == 'save_data' or lambda_function.__name__ == 'update_data':
            tk.Label(top, text=self.data_dict['column_1'][0]).place(x=50, y=30)
            tk.Label(top, text=self.data_dict['column_2'][0]).place(x=50, y=60)
            var_column_1 = ttk.Entry(top, width=45)
            var_column_1.place(x=200, y=30)
            var_column_2 = ttk.Entry(top, width=45)
            var_column_2.place(x=200, y=60)

            if self.table_name == 'age':
                tk.Label(top, text=self.data_dict['column_3'][0]).place(x=50, y=90)
                tk.Label(top, text=self.data_dict['column_4'][0]).place(x=200, y=90)
                tk.Label(top, text=self.data_dict['column_5'][0]).place(x=350, y=90)
                var_column_0 = ttk.Entry(top)
                var_column_3 = ttk.Entry(top, width=5)
                var_column_3.place(x=150, y=90)
                var_column_4 = ttk.Entry(top, width=5)
                var_column_4.place(x=300, y=90)
                var_column_5 = ttk.Entry(top, width=5)
                var_column_5.place(x=450, y=90)
            elif self.table_name == 'users':
                var_column_0 = ttk.Entry(top)
                tk.Label(top, text=self.data_dict['column_3'][0]).place(x=50, y=90)
                tk.Label(top, text=self.data_dict['column_4'][0]).place(x=50, y=120)
                tk.Label(top, text=self.data_dict['column_5'][0]).place(x=50, y=150)
                tk.Label(top, text=self.data_dict['column_6'][0]).place(x=50, y=180)
                var_column_3 = ttk.Entry(top, width=45)
                var_column_3.place(x=200, y=90)
                var_column_4 = ttk.Entry(top, width=45)
                var_column_4.place(x=200, y=120)
                var_column_5 = ttk.Entry(top, width=45)
                var_column_5.place(x=200, y=150)
                var_column_6 = ttk.Entry(top, width=45)
                var_column_6.place(x=200, y=180)

            btn_ok = ttk.Button(top, text='Сохранить')
            if self.table_name == 'users':
                btn_ok.place(x=150, y=300)
            else:
                btn_ok.place(x=150, y=130)
            if lambda_function.__name__ == 'save_data' and self.max_columns == 3:
                btn_ok.bind('<Button-1>',
                            lambda event: (self.save_data(var_column_1.get(), var_column_2.get()), top.destroy()))
            elif lambda_function.__name__ == 'save_data' and self.max_columns == 6:
                btn_ok.bind('<Button-1>',
                            lambda event: (self.save_data(var_column_1.get(), var_column_2.get(), var_column_3.get(),
                                                          var_column_4.get(), var_column_5.get()), top.destroy()))
            elif lambda_function.__name__ == 'save_data' and self.max_columns == 7:
                btn_ok.bind('<Button-1>',
                            lambda event: (self.save_data(var_column_1.get(), var_column_2.get(), var_column_3.get(),
                                                          var_column_4.get(), var_column_5.get(), var_column_6.get()),
                                           top.destroy()))

            if lambda_function.__name__ == 'update_data' and self.max_columns == 3:
                var_column_0 = ttk.Entry(top)
                btn_ok.bind('<Button-1>',
                            lambda event: (
                                self.update_data(var_column_1.get(), var_column_2.get(), var_column_0.get()),
                                top.destroy()))
                values = get_edit_record(self, db, self.table_name)[:self.max_columns]
                for i in range(len(values)):
                    vars()[f'var_column_{i}'].insert(0, values[i])
            elif lambda_function.__name__ == 'update_data' and self.max_columns == 6:
                btn_ok.bind('<Button-1>',
                            lambda event: (self.update_data(var_column_1.get(), var_column_2.get(), var_column_3.get(),
                                                            var_column_4.get(), var_column_5.get(), var_column_0.get()),
                                           top.destroy()))
                values = get_edit_record(self, db, self.table_name)[:self.max_columns]
                for i in range(len(values)):
                    vars()[f'var_column_{i}'].insert(0, values[i])
            elif lambda_function.__name__ == 'update_data' and self.max_columns == 7:
                btn_ok.bind('<Button-1>',
                            lambda event: (self.update_data(var_column_1.get(), var_column_2.get(), var_column_3.get(),
                                                            var_column_4.get(), var_column_5.get(), var_column_6.get(),
                                                            var_column_0.get()),
                                           top.destroy()))
                values = get_edit_record(self, db, self.table_name)[:self.max_columns]
                for i in range(len(values)):
                    vars()[f'var_column_{i}'].insert(0, values[i])
        if lambda_function.__name__ == 'looking_for':
            label_search = tk.Label(top, text='Поиск')
            label_search.place(x=50, y=45)
            entry_search = ttk.Entry(top)
            entry_search.place(x=200, y=45, width=200)

            btn_search = ttk.Button(top, text='Поиск')
            btn_search.place(x=150, y=130)
            btn_search.bind('<Button-1>', lambda event: self.looking_for(entry_search.get()))
            entry_search.bind('<Return>', lambda event: (self.looking_for(entry_search.get()), top.destroy()))
            btn_search.bind('<Button-1>', lambda event: top.destroy(), add='+')

        if self.table_name == 'users':
            button_cancel(top, 250, 300)
        else:
            button_cancel(top)
        next_entries(top)
        top.grab_set()
        top.focus_set()

    def add_data(self):
        self.open_toplevel_window('Добавить', self.save_data)

    def save_data(self, *args):
        with db as cur:
            column_names = get_column_names(cur, self.table_name)[:self.max_columns]
            placeholders = ', '.join(['?' for _ in range(len(args))])  # Генерация плейсхолдеров для значений
            # Генерация строки с названиями столбцов, начиная с column_names[1]
            columns_string = ', '.join([column_names[i] for i in range(1, len(args) + 1)])
            query = f"INSERT INTO {self.table_name} ({columns_string}) VALUES ({placeholders});"
            cur.execute(query, args)  # Передача значений как параметров запроса
            cur.execute(" SELECT * FROM %s " % self.table_name)
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cur.fetchall()]
        self.view_records()

    def delete_data(self):
        with db as cur:
            column_names = get_column_names(cur, self.table_name)
            for selection_item in self.tree.selection():
                cur.execute('''UPDATE %s SET is_visible=? WHERE (%s=?)''' % (self.table_name, column_names[0]),
                            (False, self.tree.set(selection_item, '#1'),))
        self.view_records()

    def edit_data(self):
        self.open_toplevel_window('Редактировать', self.update_data)

    def update_data(self, *args):
        with db as cur:
            # Получение только первых self.max_columns названий столбцов
            column_names = get_column_names(cur, self.table_name)[:self.max_columns]
            set_clause = ', '.join([f"{column}=?" for column in column_names[1:]])  # Формирование части запроса SET
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE ({column_names[0]}=?);"  # Формирование полного запроса
            cur.execute(query, args)  # Передача значений как параметров запроса
        self.view_records()

    def search_data(self):
        self.open_toplevel_window('Поиск', self.looking_for)

    def looking_for(self, chars_search):
        chars_search = ('%' + chars_search + '%',)
        with db as cur:
            column_names = get_column_names(cur, self.table_name)
            cur.execute(
                "SELECT * FROM %s WHERE (LOWER(%s) LIKE LOWER(?) AND is_visible)" % (self.table_name, column_names[2]),
                chars_search)
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cur.fetchall()]

    def refresh_data(self):
        self.view_records()


if __name__ == '__main__':
    pass
