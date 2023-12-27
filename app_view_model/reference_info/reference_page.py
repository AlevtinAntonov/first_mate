import tkinter as tk
from tkinter import ttk, BOTH
from PIL import Image, ImageTk

from app_model.variables import LARGE_FONT, ICO_DIRECTORY, ADD_PNG, EDIT_PNG, DELETE_PNG, SEARCH_PNG, REFRESH_PNG
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, path_to_file


class ReferencePage(Gui):
    def __init__(self, width: str, height: str, data_dict: dict = None):
        super().__init__(width, height)
        self.data_dict = data_dict
        self.tree = ttk.Treeview(self)

    def create_widgets(self):
        # super().create_widgets()


        # Создание treeview
        columns = list(self.data_dict.keys())
        self.tree["columns"] = columns
        for col in columns:
            width = self.data_dict[col]
            self.tree.column(col, width=width, anchor="center")
            self.tree.heading(col, text=col, anchor="center")

        self.tree.grid(row=5, column=0, columnspan=5)


        self.add_button = tk.Button(self.root, text="Добавить", command=self.add_data, width=80)
        self.add_button.grid(row=2, column=0)

        self.edit_button = tk.Button(self.root, text="Редактировать", command=self.edit_data, width=80)
        self.edit_button.grid(row=2, column=1)

        self.delete_button = tk.Button(self.root, text="Удалить", command=self.delete_data, width=80)
        self.delete_button.grid(row=2, column=2)

        self.search_button = tk.Button(self.root, text="Поиск", command=self.search_data, width=80)
        self.search_button.grid(row=2, column=3)

        self.refresh_button = tk.Button(self.root, text="Обновить", command=self.refresh_data, width=80)
        self.refresh_button.grid(row=2, column=4)

        add_img = Image.open(path_to_file(ICO_DIRECTORY, ADD_PNG))  # путь к изображению
        add_img = ImageTk.PhotoImage(add_img)
        self.add_button.config(image=add_img, compound="top")
        self.add_button.image = add_img  # сохраняем ссылку на изображение

        edit_img = Image.open(path_to_file(ICO_DIRECTORY, EDIT_PNG))  # путь к изображению
        edit_img = ImageTk.PhotoImage(edit_img)
        self.edit_button.config(image=edit_img, compound="top")
        self.edit_button.image = edit_img  # сохраняем ссылку на изображение

        delete_img = Image.open(path_to_file(ICO_DIRECTORY, DELETE_PNG))  # путь к изображению
        delete_img = ImageTk.PhotoImage(delete_img)
        self.delete_button.config(image=delete_img, compound="top")
        self.delete_button.image = delete_img  # сохраняем ссылку на изображение

        search_img = Image.open(path_to_file(ICO_DIRECTORY, SEARCH_PNG))  # путь к изображению
        search_img = ImageTk.PhotoImage(search_img)
        self.search_button.config(image=search_img, compound="top")
        self.search_button.image = search_img  # сохраняем ссылку на изображение

        refresh_img = Image.open(path_to_file(ICO_DIRECTORY, REFRESH_PNG))  # путь к изображению
        refresh_img = ImageTk.PhotoImage(refresh_img)
        self.refresh_button.config(image=refresh_img, compound="top")
        self.refresh_button.image = refresh_img  # сохраняем ссылку на изображение

        # for col, col_txt in self.tree_columns.items():
        #     self.tree.column(col, minwidth=col_txt[1], width=col_txt[2], anchor=tk.CENTER)
        #     self.tree.heading(col, text=col_txt[0])
        # #
        # # self.tree.pack(side=tk.LEFT)
        # self.tree = ttk.Treeview(self.root, columns=('short_name', 'full_name'), show="headings")
        # # self.tree = ttk.Treeview(self.root, columns=('id', 'short_name', 'full_name'), show="headings")
        # # self.tree.heading('id', text='ID')
        # self.tree.heading('short_name', text='Short Name')
        # self.tree.heading('full_name', text='Full Name')
        # # self.tree.column('id', width=50)
        # self.tree.column('short_name', width=180)
        # self.tree.column('full_name', width=220)
        # self.tree.grid(row=5, columnspan=5)
        # scroll = tk.Scrollbar(self.root, command=self.tree.yview)
        # scroll.pack(side=tk.LEFT, fill=tk.Y)
        # self.tree.configure(yscrollcommand=scroll.set)
        #
        # self.tree.bind("<Double-1>", self.OnDoubleClick)
        data = [
            (1, "John", "Doe"),
            (2, "Jane", "Smith"),
            # Добавьте данные из вашего словаря здесь
        ]

        for entry in data:
            self.tree.insert("", tk.END, values=entry)

        tk.Button(self.root, text="Назад к Справочникам", bg='DarkSlateGray', fg='white',
                  command=lambda: self.return_to_start_page(), width=25, height=1).grid(row=10, column=0, columnspan=2,
                                                                                        sticky='e')
        self.root.pack(expand=True, fill="both")
    def add_data(self):
        # Логика добавления данных в таблицу benefit
        pass

    def edit_data(self):
        # Логика редактирования данных в таблицу benefit
        pass

    def delete_data(self):
        # Логика удаления данных из таблицы benefit
        pass

    def search_data(self):
        # Логика удаления данных из таблицы benefit
        pass

    def refresh_data(self):
        # Логика удаления данных из таблицы benefit
        pass
