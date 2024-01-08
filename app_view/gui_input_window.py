import ctypes
import win32api
import tkinter as tk
from tkinter import messagebox, ttk
import keyboard
import pyperclip
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
        self.bind_keyboard_shortcuts()

    def create_widgets(self):
        pass

    def bind_keyboard_shortcuts(self):
        keyboard.add_hotkey('ctrl+c', self.copy_text)
        keyboard.add_hotkey('ctrl+v', self.paste_text)

    def copy_text(self):
        widget = self.root.focus_get()
        if isinstance(widget, ttk.Entry):
            selected_text = widget.selection_get()
            pyperclip.copy(selected_text)

    def paste_text(self):
        widget = self.root.focus_get()
        if isinstance(widget, ttk.Entry):
            widget.insert('insert', pyperclip.paste())

    def on_close(self):
        result = messagebox.askokcancel("Завершение работы", "Вы действительно хотите выйти?")
        if result:
            self.root.destroy()

    def display_info(self, *args):
        selected_name = self.referral_select.get()
        for key, value in self.data.items():
            if value[0] == selected_name:
                self.child_full_name_label.config(text=f"ФИО ребенка: {value[3]} {value[4]} {value[5]}")
                self.date_of_birth_label.config(text=f"Дата рождения: {value[6].strftime("%d.%m.%Y")}")
                self.team_plan_label.config(text=f"Группа по направлению: {value[2]}")
                self.referral_id = key
                self.child_id = value[7]
                self.refferal_team_id = value[2]

    def update_referral_options(self, event):
        typed_text = self.referral_select.get()

        if typed_text == "":
            filtered_values = [value[0] for value in
                               self.data.values()]  # Показать все варианты, если нет введенного текста
        else:
            filtered_values = [value[0] for value in self.data.values() if
                               typed_text.lower() in str(value).lower()]  # Фильтрация вариантов по введенному тексту

        self.referral_select["values"] = filtered_values


if __name__ == '__main__':
    pass
