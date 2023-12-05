import tkinter as tk
from tkinter import messagebox, ttk

from app_model.db.db_connect import db
from app_model.db.db_query import query_login
from app_model.variables import MAIN_TITLE, MAIN_ICO, ORGANIZATION_SHORT_NAME, LARGE_FONT, START_IMAGE
from app_view_model.functions.functions import position_center
from app_view_model.start_page import StartPage


class LoginPage:
    def __init__(self, root, width: str = '360', height: str = '500'):
        # Создаем главное окно входа в программу
        self.root = root
        self.root.title(MAIN_TITLE)
        self.root.iconbitmap(default=MAIN_ICO)
        self.root.minsize(360, 500)
        self.root.geometry('x'.join((width, height)))
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        position_center(root, width, height)

        # Создаем холст (Canvas) и добавляем его на форму
        self.canvas = tk.Canvas(root, width=340, height=340)
        self.canvas.pack()

        # Загружаем изображение
        self.photo = tk.PhotoImage(file=START_IMAGE)

        # Отображаем изображение на холсте
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Создаем рамку с заголовком
        self.frame = tk.LabelFrame(root, text=ORGANIZATION_SHORT_NAME, font=LARGE_FONT, width=600, height=200)
        self.frame.pack(expand=True, fill='both', padx=10, pady=5)

        self.label_username = tk.Label(self.frame, text="Имя пользователя ")
        self.label_username.place(x=60, y=30)
        self.entry_username = ttk.Entry(self.frame)
        self.entry_username.place(x=200, y=30)

        self.label_password = tk.Label(self.frame, text="Пароль ")
        self.label_password.place(x=120, y=60)
        self.entry_password = ttk.Entry(self.frame, show="*")
        self.entry_password.place(x=200, y=60)

        self.login_button = ttk.Button(self.frame, text="Вход", command=self.check_credentials)
        self.login_button.place(x=70, y=90)
        self.exit_button = ttk.Button(self.frame, text="Отмена", command=self.root.destroy, width=15)
        self.exit_button.place(x=200, y=90)

    def check_credentials(self):
        # Проверка логина и пароля в базе данных

        with db as cur:
            user = cur.execute(query_login, (self.entry_username.get(), self.entry_password.get())).fetchall()
        if user:
            self.root.destroy()  # Close the login window
            self.open_start_page()
        else:
            messagebox.showerror("Ошибка", "Такой логин и пароль не существует")

    def open_start_page(self):
        start()

    def on_close(self):
        result = messagebox.askokcancel("Завершение работы", "Вы действительно хотите выйти?")
        if result:
            self.root.destroy()


def start():
    root = tk.Tk()
    StartPage(root)
    root.mainloop()
