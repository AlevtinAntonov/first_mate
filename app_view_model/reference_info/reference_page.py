import tkinter as tk
from PIL import Image, ImageTk

from app_model.variables import ICO_DIRECTORY, ADD_PNG, EDIT_PNG, DELETE_PNG, SEARCH_PNG, REFRESH_PNG
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import path_to_file


class ReferencePage(Gui):
    def __init__(self, width: str, height: str, data_dict: dict = None):
        super().__init__(width, height)
        self.data_dict = data_dict
        self.create_widgets()

    def create_widgets(self):
        self.show_buttons()

    def show_buttons(self):
        button_frame = tk.Frame(self.root, borderwidth=4, relief="groove")  # Создание фрейма с рамкой
        button_frame.grid(row=2, column=0, columnspan=5,
                          pady=10, padx=10)  # Добавление фрейма с кнопками в родительский контейнер

        self.add_button = tk.Button(button_frame, text="Добавить", command=self.add_data, width=80)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(button_frame, text="Редактировать", command=self.edit_data, width=80)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Удалить", command=self.delete_data, width=80)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_button = tk.Button(button_frame, text="Поиск", command=self.search_data, width=80)
        self.search_button.grid(row=0, column=3, padx=5)

        self.refresh_button = tk.Button(button_frame, text="Обновить", command=self.refresh_data, width=80)
        self.refresh_button.grid(row=0, column=4, padx=5)

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

        tk.Button(self.root, text="Назад к Справочникам", bg='DarkSlateGray', fg='white',
                  command=lambda: self.return_to_start_page(), width=25, height=1).grid(row=10, column=1, columnspan=3,
                                                                                        sticky='we', pady=10)

    def add_data(self):
        # Логика добавления данных в таблицу
        pass

    def edit_data(self):
        # Логика редактирования данных в таблицу
        pass

    def delete_data(self):
        # Логика удаления данных из таблицы
        pass

    def search_data(self):
        # Логика поиска данных в таблице
        pass

    def refresh_data(self):
        # Логика обновления данных в таблице
        pass
