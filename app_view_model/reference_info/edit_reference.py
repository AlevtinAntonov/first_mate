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

            btn_ok = ttk.Button(top, text='Сохранить')
            btn_ok.place(x=150, y=130)
            if lambda_function.__name__ == 'save_data':
                btn_ok.bind('<Button-1>',
                            lambda event: (self.save_data(var_column_1.get(), var_column_2.get()), top.destroy()))

            if lambda_function.__name__ == 'update_data':
                var_column_0 = ttk.Entry(top)
                btn_ok.bind('<Button-1>',
                            lambda event: (
                                self.update_data(var_column_1.get(), var_column_2.get(), var_column_0.get()),
                                top.destroy()))
                column_1, column_2, column_0 = get_edit_record(self, db, self.table_name)
                var_column_0.insert(0, column_0)
                var_column_1.insert(0, column_1)
                var_column_2.insert(0, column_2)
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

        button_cancel(top)
        next_entries(top)
        top.grab_set()
        top.focus_set()

    def add_data(self):
        self.open_toplevel_window('Добавить', self.save_data)

    def save_data(self, var_column_1, var_column_2):
        with db as cur:
            column_names = get_column_names(cur, self.table_name)
            query = " INSERT INTO %s(%s, %s) VALUES ( ?, ?); " % (self.table_name, column_names[1], column_names[2])
            cur.execute(query, (var_column_1, var_column_2))
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

    def update_data(self, var_column_1, var_column_2, var_column_0):
        with db as cur:
            column_names = get_column_names(cur, self.table_name)
            query = " UPDATE %s SET %s=?, %s=? WHERE (%s=?); " % (
                self.table_name, column_names[1], column_names[2], column_names[0])
            cur.execute(query, (var_column_1, var_column_2, var_column_0))
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
