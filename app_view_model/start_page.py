import tkinter as tk
from tkinter import messagebox, ttk

from app_model.domain.referral import Referral
from app_model.variables import LARGE_FONT, MAIN_TITLE, MAIN_ICO
from app_view.gui_input_window import Gui
from app_view.referral_labels import ReferralLabels, ReferralLabelsWin3
from app_view_model.functions.functions import position_center
from app_view_model.new_address import AddressWin
from app_view_model.new_child import NewChild
from app_view_model.new_parent import NewParent
from app_view_model.new_referral import NewReferral


def start_page():
    root = tk.Tk()
    StartPage(root)
    root.mainloop()


def new_referral():
    NewReferralWin()


def new_parent():
    NewParentWin()


def child_birth_certificate():
    NewChildCertificateWin()


def new_address():
    NewChildCertificateWin()


class StartPage:
    def __init__(self, root):
        self.root = root
        self.root.title(MAIN_TITLE)
        self.root.iconbitmap(MAIN_ICO)
        self.width = '360'
        self.height = '500'
        self.root.minsize(self.width, self.height)
        self.root.geometry('x'.join((self.width, self.height)))
        position_center(root, self.width, self.height)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        tk.Label(self.root, text="ГЛАВНОЕ МЕНЮ").pack(pady=10, padx=10)

        self.button_3 = tk.Button(self.root, text="Приём нового воспитанника", command=self.add_new_child, width=30,
                                  height=1)
        self.button_3.pack(padx=5, pady=5)

        self.button_4 = tk.Button(self.root, text="Личные Дела Воспитанников", command=self.open_window_4, width=30,
                                  height=1)
        self.button_4.pack(padx=5, pady=5)

        self.button_5 = tk.Button(self.root, text="Ввод справочников", command=self.open_window_5, width=30, height=1)
        self.button_5.pack(padx=5, pady=5)

        self.button_6 = tk.Button(self.root, text="Резервная кнопка", command=self.open_window_6, width=30, height=1)
        self.button_6.pack(padx=5, pady=5)

        tk.Button(self.root, text="Выход", bg='DarkSlateGray', fg='white', command=lambda: self.root.destroy(),
                  width=20,
                  height=1).pack(padx=5, pady=15)

    def add_new_child(self):
        self.root.destroy()  # Close the Start Page
        gui = ProjectAddNew()

    def open_window_4(self):
        self.root.destroy()  # Close the Start Page
        window_4 = Gui_4('600', '600')

    def open_window_5(self):
        self.root.destroy()  # Close the Start Page
        window_5 = Gui_4('250', '250')

    def open_window_6(self):
        self.root.destroy()  # Close the Start Page
        window_6 = Gui_4('700', '700')

    def on_close(self):
        result = messagebox.askokcancel("Завершение работы", "Вы действительно хотите выйти?")
        if result:
            self.root.destroy()


class ProjectAddNew(Gui):
    def __init__(self, width='360', height='500'):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        tk.Label(self.root, text="Прием нового воспитанника", font=LARGE_FONT).pack(pady=10, padx=10)
        tk.Button(self.root, text="Направление", command=self.open_window_referral, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Паспорт родителя/представителя", command=self.open_window_parent,
                  width=30, height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Свидетельство о рождении", command=self.open_birth_certificate, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Ввод адреса", command=self.open_window_address, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Компенсация родит.платы", command=self.open_window, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Сведения о семье", command=self.open_window, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Назад в Главное меню", bg='DarkSlateGray', fg='white',
                  command=self.return_to_start_page,
                  width=25,
                  height=1).pack()

    def open_window_referral(self):
        self.root.destroy()
        new_referral()

    def open_window_parent(self):
        self.root.destroy()
        NewParentWin()

    def open_window_address(self):
        self.root.destroy()
        NewAddressWin()

    def open_birth_certificate(self):
        self.root.destroy()
        child_birth_certificate()

    def open_window(self):
        self.root.destroy()
        new_referral()

    def return_to_start_page(self):
        self.root.destroy()
        start_page()


class NewReferralWin(NewReferral):
    def return_to_start_page(self):
        self.root.destroy()
        ProjectAddNew()


class NewParentWin(NewParent):
    def return_to_start_page(self):
        self.root.destroy()
        ProjectAddNew()


class NewAddressWin(AddressWin):
    def return_to_start_page(self):
        self.root.destroy()
        ProjectAddNew()


class NewChildCertificateWin(NewChild):
    def return_to_start_page(self):
        self.root.destroy()
        ProjectAddNew()


class Gui_4(Gui):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.root.geometry('x'.join((self.width, self.height)))
        self.labels = ReferralLabelsWin3(self.root)

    def return_to_start_page(self):
        self.root.destroy()
        start_page()


if __name__ == '__main__':
    pass
