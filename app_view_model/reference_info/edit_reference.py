import tkinter as tk
from tkinter import ttk

from app_view_model.reference_info.reference_page import ReferencePage


class EditReference(ReferencePage):
    def __init__(self, width: str, height: str, data_dict: dict):
        super().__init__(width, height)
        self.data_dict = data_dict
        self.show_tree(self.data_dict)

    def show_tree(self, data_dict):

        columns = [f"column_{i}" for i in range(3)]
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for i, (column_key, (column_name, column_width)) in enumerate(data_dict.items()):
            self.tree.heading(columns[i], text=column_name)
            self.tree.column(columns[i], width=column_width)
        self.tree.grid(row=5, columnspan=5)
