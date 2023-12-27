import tkinter as tk
from app_view_model.reference_info.reference_page import ReferencePage


class EditBenefit(ReferencePage):

    def add_columns_with_widths(self, data_dict):
        self.data_dict = data_dict
        columns = list(data_dict.keys())

        for col in columns:
            width = data_dict[col]
            self.tree.column(col, width=width, anchor=tk.CENTER)
            self.tree.heading(col, text=col, anchor=tk.CENTER)
