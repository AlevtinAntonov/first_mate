import tkinter as tk
from tkinter import messagebox

from app_model.variables import MAIN_TITLE, MAIN_ICO
from app_view_model.functions.functions import position_center
from app_view_model.interfaces.input_window import InputWindow


class Gui(InputWindow):
    def __init__(self, width: str, height: str):
        super().__init__()
        self.height = height
        self.width = width
        self.labels = None
        self.root.title(MAIN_TITLE)
        self.root.iconbitmap(MAIN_ICO)
        self.root.geometry('x'.join((self.width, self.height)))
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        position_center(self.root, self.width, self.height)
        self.create_widgets()

    def create_widgets(self):
        self.save_button = tk.Button(self.root, text="Save",
                                     command=lambda: print(self.labels.entry_referral_number.get()))
        self.save_button.grid(row=9, column=0)

        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.return_to_start_page)
        self.cancel_button.grid(row=9, column=1)

    def on_close(self):
        result = messagebox.askokcancel("Завершение работы", "Вы действительно хотите выйти?")
        if result:
            self.root.destroy()


if __name__ == '__main__':
    pass
