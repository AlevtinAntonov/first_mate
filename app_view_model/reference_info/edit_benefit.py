import tkinter as tk
from tkinter import ttk, BOTH
from PIL import Image, ImageTk

from app_model.variables import LARGE_FONT, ICO_DIRECTORY, ADD_PNG, EDIT_PNG, DELETE_PNG, SEARCH_PNG, REFRESH_PNG
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import buttons_add_new, path_to_file


class EditBenefit(Gui):
    # def __init__(self, width: str = '400', height: str = '400', project_title: str = None, tbl_name: str = None,
    #              field_id: str = None, sort_col: str = None, label_1: str = None, label_2: str = None, field_1=None,
    #              field_2=None, tree_columns: dict = None):
    #     super().__init__(width, height)
    #     self.root.geometry('x'.join((self.width, self.height)))
    #     if tree_columns is None:
    #         tree_columns = {'col_0': ['XXX', 0, 0], 'col_1': ['XXXXX', 250, 250],
    #                         'col_2': ['XXXX', 250, 250]}
    #     self.tree_columns = tree_columns
    #     self.tbl_name = tbl_name
    #     self.field_id = field_id
    #     self.field_1 = field_1
    #     self.field_2 = field_2
    #     self.sort_col = sort_col
    #     self.project_title = project_title
    #     self.label_1 = label_1
    #     self.label_2 = label_2
    #     self.add_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, ADD_PNG))
    #     self.update_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, EDIT_PNG))
    #     self.delete_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, DELETE_PNG))
    #     self.search_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, SEARCH_PNG))
    #     self.refresh_img = tk.PhotoImage(file=path_to_file(ICO_DIRECTORY, REFRESH_PNG))
    #     col_names = tuple(self.tree_columns)
    #     self.tree = ttk.Treeview(self.root, columns=col_names, height=15, show='headings')
    #
    #     tk.Label(self.root, text=project_title, font=LARGE_FONT).pack(pady=5, padx=5)

    # def create_widgets(self):
    #     frame = ttk.Frame(self.root)
    #     frame.pack(fill=BOTH, expand=1)
    #
    #     tk.Label(frame, text="Льготная категория", font=LARGE_FONT).pack()
    #
    #     tk.Button(frame, text="Назад в меню приема", bg='DarkSlateGray', fg='white',
    #               command=lambda: self.return_to_start_page(), width=25, height=1).pack()
    def create_widgets(self):
        # super().create_widgets()

        self.tree = ttk.Treeview(self.root, columns=('short_name', 'full_name'), show="headings")
        # self.tree = ttk.Treeview(self.root, columns=('id', 'short_name', 'full_name'), show="headings")
        # self.tree.heading('id', text='ID')
        self.tree.heading('short_name', text='Short Name')
        self.tree.heading('full_name', text='Full Name')
        # self.tree.column('id', width=50)
        self.tree.column('short_name', width=150)
        self.tree.column('full_name', width=250)
        self.tree.grid(row=5, columnspan=2)

        self.add_button = tk.Button(self.root, text="Add", command=self.add_data)
        self.add_button.grid(row=2, column=0)

        self.edit_button = tk.Button(self.root, text="Edit", command=self.edit_data)
        self.edit_button.grid(row=2, column=1)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_data)
        self.delete_button.grid(row=3, columnspan=2)

        # Добавление изображений к кнопкам
        save_img = Image.open("save_image.png")  # замените "save_image.png" на путь к вашему изображению
        save_img = save_img.resize((20, 20))  # измените размер изображения по вашему усмотрению
        save_img = ImageTk.PhotoImage(save_img)

        self.save_button.config(image=save_img, compound="left")
        self.save_button.image = save_img  # сохраняем ссылку на изображение, чтобы не было ошибок

        cancel_img = Image.open("cancel_image.png")  # замените "cancel_image.png" на путь к вашему изображению
        cancel_img = cancel_img.resize((20, 20))  # измените размер изображения по вашему усмотрению
        cancel_img = ImageTk.PhotoImage(cancel_img)

        self.cancel_button.config(image=cancel_img, compound="left")
        self.cancel_button.image = cancel_img  # сохраняем ссылку на изображение, чтобы не было ошибок

        add_img = Image.open("add_image.png")  # замените "add_image.png" на путь к вашему изображению
        add_img = add_img.resize((20, 20))  # измените размер изображения по вашему усмотрению
        add_img = ImageTk.PhotoImage(add_img)

        self.add_button.config(image=add_img, compound="left")
        self.add_button.image = add_img  # сохраняем ссылку на изображение, чтобы не было ошибок

        edit_img = Image.open("edit_image.png")  # замените "edit_image.png" на путь к вашему изображению
        edit_img = edit_img.resize((20, 20))  # измените размер изображения по вашему усмотрению
        edit_img = ImageTk.PhotoImage(edit_img)

        self.edit_button.config(image=edit_img, compound="left")
        self.edit_button.image = edit_img  # сохраняем ссылку на изображение, чтобы не было ошибок

        delete_img = Image.open("delete_image.png")  # замените "delete_image.png" на путь к вашему изображению
        delete_img = delete_img.resize((20, 20))  # измените размер изображения по вашему усмотрению
        delete_img = ImageTk.PhotoImage(delete_img)

        self.delete_button.config(image=delete_img, compound="left")
        self.delete_button.image = delete_img  # сохраняем ссылку на изображение, чтобы не было ошибок

        # Rest of the code remains the same

        # Adding images to buttons
        save_img_path = "save_image.png"  # Replace with the actual path to your image
        save_img = Image.open(save_img_path)
        save_img = save_img.resize((20, 20))
        save_img = ImageTk.PhotoImage(save_img)

        self.save_button.config(image=save_img, compound="left")
        self.save_button.image = save_img

        # Repeat the same process for other buttons

        cancel_img_path = "cancel_image.png"  # Replace with the actual path to your image
        cancel_img = Image.open(cancel_img_path)
        # Resize and add to the button as done above

        add_img_path = "add_image.png"  # Replace with the actual path to your image
        add_img = Image.open(add_img_path)
        # Resize and add to the button as done above

        edit_img_path = "edit_image.png"  # Replace with the actual path to your image
        edit_img = Image.open(edit_img_path)
        # Resize and add to the button as done above

        delete_img_path = "delete_image.png"  # Replace with the actual path to your image
        delete_img = Image.open(delete_img_path)
        # Resize and add to the button as done above

def add_data(self):
        # Логика добавления данных в таблицу benefit
        pass

    def edit_data(self):
        # Логика редактирования данных в таблицу benefit
        pass

    def delete_data(self):
        # Логика удаления данных из таблицы benefit
        pass
