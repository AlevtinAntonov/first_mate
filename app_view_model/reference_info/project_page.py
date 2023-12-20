import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.variables import ICO_DIRECTORY, ADD_PNG, EDIT_PNG, DELETE_PNG, SEARCH_PNG, REFRESH_PNG, LARGE_FONT
from app_view_model.functions.functions import path_to_file, position_center, go_to_next_entry


class ProjectPage(tk.Frame):

    def __init__(self, parent, controller, project_title: str = None, tbl_name: str = None, field_id: str = None,
                 sort_col: str = None, label_1: str = None, label_2: str = None, field_1=None, field_2=None,
                 tree_columns: dict = None):
        tk.Frame.__init__(self, parent)
        if tree_columns is None:
            tree_columns = {'col_0': ['XXX', 0, 0], 'col_1': ['XXXXX', 250, 250],
                            'col_2': ['XXXX', 250, 250]}
        self.tree_columns = tree_columns
        self.tbl_name = tbl_name
        self.field_id = field_id
        self.field_1 = field_1
        self.field_2 = field_2
        self.sort_col = sort_col
        self.project_title = project_title
        self.label_1 = label_1
        self.label_2 = label_2
        self.controller = controller
        self.add_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, ADD_PNG))
        self.update_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, EDIT_PNG))
        self.delete_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, DELETE_PNG))
        self.search_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, SEARCH_PNG))
        self.refresh_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, REFRESH_PNG))
        col_names = tuple(self.tree_columns)

        self.tree = ttk.Treeview(self, columns=col_names, height=15, show='headings')

        tk.Label(self, text=project_title, font=LARGE_FONT).pack(pady=5, padx=5)
        tk.Button(self, text="Назад к справочникам", bg='blue', fg='white',
                  command=lambda: controller.show_frame("AddReferencesData"), width=25, height=1).pack(padx=5, pady=15)

    def init_main(self):
        toolbar = tk.Frame(self, bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP,
                  image=self.add_img).pack(side=tk.LEFT, padx=15)

        tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0, image=self.update_img, compound=tk.TOP,
                  command=self.open_update_dialog).pack(side=tk.LEFT, padx=15)

        tk.Button(toolbar, text='Удалить', bg='#d7d8e0', bd=0, image=self.delete_img, compound=tk.TOP,
                  command=self.delete_records).pack(side=tk.LEFT, padx=15)

        tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img, compound=tk.TOP,
                  command=self.open_search_dialog).pack(side=tk.LEFT, padx=15)

        tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img, compound=tk.TOP,
                  command=self.view_records).pack(side=tk.LEFT, padx=15)

        for col, col_txt in self.tree_columns.items():
            self.tree.column(col, minwidth=col_txt[1], width=col_txt[2], anchor=tk.CENTER)
            self.tree.heading(col, text=col_txt[0])

        self.tree.pack(side=tk.LEFT)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

        self.tree.bind("<Double-1>", self.OnDoubleClick)

    def OnDoubleClick(self, event):
        self.tree.set(self.tree.selection()[0], '#1')
        self.open_update_dialog()

    def view_records(self):
        with db as cur:
            cur.execute(" SELECT * FROM %s WHERE is_visible ORDER BY %s ASC;" % (self.tbl_name, self.sort_col))
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cur.fetchall()]

    def records(self, id_, var_field_1, var_field_2):
        with db as cur:
            query = " INSERT INTO %s(%s, %s) VALUES ( ?, ?); " % (self.tbl_name, self.field_1, self.field_2)
            cur.execute(query, (var_field_1, var_field_2))
            cur.execute(" SELECT * FROM %s " % self.tbl_name)
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cur.fetchall()]
        self.view_records()

    def update_record(self, var_field_1, var_field_2, var_field_id):
        with db as cur:
            query = " UPDATE %s SET %s=?, %s=? WHERE (%s=?); " % (
                self.tbl_name, self.field_1, self.field_2, self.field_id)
            cur.execute(query, (var_field_1, var_field_2, var_field_id))
        self.view_records()

    def delete_records(self):
        with db as cur:
            for selection_item in self.tree.selection():
                cur.execute('''UPDATE %s SET is_visible=? WHERE (%s=?)''' % (self.tbl_name, self.field_id),
                            (False, self.tree.set(selection_item, '#1'),))
        self.view_records()

    def search_records(self, chars_search):
        chars_search = ('%' + chars_search + '%',)
        with db as cur:
            cur.execute("SELECT * FROM %s WHERE (%s LIKE ? AND is_visible)" % (self.tbl_name, self.field_1),
                        chars_search)
            [self.tree.delete(i) for i in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in cur.fetchall()]

    def open_search_dialog(self):
        top = tk.Toplevel()
        top.title('Поиск')
        top.geometry('350x110')
        position_center(top)
        top.resizable(False, False)

        label_search = tk.Label(top, text='Поиск')
        label_search.place(x=50, y=20)

        entry_search = ttk.Entry(top)
        entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(top, text='Закрыть', command=top.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(top, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.search_records(entry_search.get()))
        entry_search.bind('<Return>', lambda event: (self.search_records(entry_search.get()), top.destroy()))
        btn_search.bind('<Button-1>', lambda event: top.destroy(), add='+')

    def open_dialog(self):
        top = tk.Toplevel()

        top.geometry('500x170')
        position_center(top)
        top.title('Добавить')

        top.resizable(False, False)

        tk.Label(top, text=self.label_1).place(x=50, y=30)
        tk.Label(top, text=self.label_2).place(x=50, y=60)

        var_field_1 = ttk.Entry(top, width=45)
        var_field_1.place(x=200, y=30)

        var_field_2 = ttk.Entry(top, width=45)
        var_field_2.place(x=200, y=60)

        self.button_cancel(top)

        btn_ok = ttk.Button(top, text='Сохранить')
        btn_ok.place(x=150, y=130)
        btn_ok.bind('<Button-1>',
                    lambda event: (self.records(self, var_field_1.get(), var_field_2.get()), top.destroy()))

        entries = [child for child in top.winfo_children() if isinstance(child, ttk.Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx_=idx: go_to_next_entry(e, entries, idx_))

        top.grab_set()
        top.focus_set()

    def button_cancel(self, top):
        btn_cancel = ttk.Button(top, text='Закрыть', command=lambda: top.destroy())
        btn_cancel.place(x=250, y=130)

    def open_update_dialog(self):
        top = tk.Toplevel()
        top.geometry('500x170')
        position_center(top)
        top.title('Редактирование')
        top.resizable(False, False)

        with db as cur:
            tk.Label(top, text=self.label_1).place(x=50, y=30)
            tk.Label(top, text=self.label_2).place(x=50, y=60)
            var_field_id = ttk.Entry(top)
            var_field_1 = ttk.Entry(top, width=45)
            var_field_1.place(x=200, y=30)
            var_field_2 = ttk.Entry(top, width=45)
            var_field_2.place(x=200, y=60)
            self.button_cancel(top)
            # btn_cancel = ttk.Button(top, text='Закрыть', command=lambda: top.destroy())
            # btn_cancel.place(x=250, y=130)
            btn_edit = ttk.Button(top, text='Сохранить')
            btn_edit.place(x=150, y=130)
            btn_edit.bind('<Button-1>', lambda event: (self.update_record(var_field_1.get(),
                                                                          var_field_2.get(),
                                                                          var_field_id.get(), ), top.destroy()))
            cur.execute(" SELECT * FROM %s WHERE (%s=?) " % (self.tbl_name, self.field_id),
                        (self.tree.set(self.tree.selection()[0], '#1'),))
            row = cur.fetchone()
            var_field_1.insert(0, row[1])
            var_field_2.insert(0, row[2])
            var_field_id.insert(0, row[0])

            entries = [child for child in top.winfo_children() if isinstance(child, ttk.Entry)]
            for idx, entry in enumerate(entries):
                entry.bind('<Return>', lambda e, idx_=idx: go_to_next_entry(e, entries, idx_))
