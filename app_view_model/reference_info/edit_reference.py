import tkinter as tk
from tkinter import ttk

from app_model.variables import LARGE_FONT, CONF_D_W
from app_view_model.reference_info.reference_page import ReferencePage


class EditReference(ReferencePage):
    def __init__(self, width: str, height: str, data_dict: dict, window_title_key: str):
        super().__init__(width, height)
        self.window_title_key = window_title_key
        self.data_dict = data_dict
        self.show_tree(self.data_dict)

    def show_tree(self, data_dict):
        tk.Label(self.root, text=data_dict[self.window_title_key][0], font=LARGE_FONT).grid(row=0, column=0, cnf=CONF_D_W, columnspan=4,
                                                                    sticky="nsew")

        columns = [f"column_{i}" for i in range(3)]
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for i, (column_key, (column_name, column_width)) in enumerate(data_dict.items()):
            self.tree.heading(columns[i], text=column_name)
        self.tree.column(columns[i], width=column_width)
        self.tree.grid(row=5, columnspan=5)
