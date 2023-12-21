import tkinter as tk
from tkinter import ttk, BOTH

from app_model.variables import LARGE_FONT, ICO_DIRECTORY, ADD_PNG, EDIT_PNG, DELETE_PNG, SEARCH_PNG, REFRESH_PNG
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, path_to_file


class EditBenefit(Gui):
    def __init__(self, width: str = '400', height: str = '400', project_title: str = None, tbl_name: str = None,
                 field_id: str = None, sort_col: str = None, label_1: str = None, label_2: str = None, field_1=None,
                 field_2=None, tree_columns: dict = None):
        super().__init__(width, height)
        self.root.geometry('x'.join((self.width, self.height)))
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
        self.add_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, ADD_PNG))
        self.update_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, EDIT_PNG))
        self.delete_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, DELETE_PNG))
        self.search_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, SEARCH_PNG))
        self.refresh_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, REFRESH_PNG))
        col_names = tuple(self.tree_columns)
        self.tree = ttk.Treeview(self.root, columns=col_names, height=15, show='headings')

        tk.Label(self.root, text=project_title, font=LARGE_FONT).pack(pady=5, padx=5)

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)

        tk.Label(frame, text="Льготная категория", font=LARGE_FONT).pack()

        tk.Button(frame, text="Назад в меню приема", bg='DarkSlateGray', fg='white',
                  command=lambda: self.return_to_start_page(), width=25, height=1).pack()
