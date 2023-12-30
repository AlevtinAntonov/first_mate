import tkinter as tk
from tkinter import messagebox, ttk

from app_model.domain.address import Address
from app_model.domain.referral import Referral
from app_model.variables import LARGE_FONT, MAIN_TITLE, MAIN_ICO, references_dict
from app_view.gui_input_window import Gui
from app_view.referral_labels import ReferralLabels, ReferralLabelsWin3
from app_view_model.functions.functions import position_center
from app_view_model.new_address import AddressWin
from app_view_model.new_child import NewChild
from app_view_model.new_parent import NewParent
from app_view_model.new_referral import NewReferral
from app_view_model.print_forms.print_application import PrintAplication
from app_view_model.reference_info.edit_reference import EditReference
from app_view_model.reference_info.functions import get_sub_dict
from app_view_model.reference_info.reference_citizenship import EditCitizenship
from app_view_model.reference_info.reference_organization import EditOrganization


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
    NewAddressWin()


def edit_citizenship():
    EditCitizenship()


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

        self.button_5 = tk.Button(self.root, text="Ввод справочников", command=self.open_references, width=30, height=1)
        self.button_5.pack(padx=5, pady=5)

        self.button_6 = tk.Button(self.root, text="Печать документов", command=self.open_print_forms, width=30,
                                  height=1)
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

    def open_references(self):
        self.root.destroy()  # Close the Start Page
        window_5 = ReferenceInfoEdit('360', '500')

    def open_print_forms(self):
        self.root.destroy()  # Close the Start Page
        window_5 = PrintForms('360', '500')

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


class EditReferenceWin(EditReference):
    def return_to_start_page(self):
        self.root.destroy()
        ReferenceInfoEdit()


class PrintApplicationWin(PrintAplication):
    def return_to_start_page(self):
        self.root.destroy()
        PrintForms()


class ReferenceInfoEdit(Gui):
    def __init__(self, width='360', height='500'):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        tk.Label(self.root, text="Ввод справочников", font=LARGE_FONT).pack(pady=10, padx=10)
        tk.Button(self.root, text="Сведения об организации", command=self.open_window_organization, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Гражданство", command=lambda: self.open_window("citizenship"), width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Льготные категории", command=lambda: self.open_window("benefit"),
                  width=30, height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Режим пребывания", command=lambda: self.open_window("mode"), width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Администрирование", command=self.open_window_admin, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Назад в Главное меню", bg='DarkSlateGray', fg='white',
                  command=self.return_to_main_page,
                  width=25,
                  height=1).pack()

    def open_window_organization(self):
        self.root.destroy()
        EditOrganization()

    def open_window(self, dict_key):
        self.root.destroy()
        EditReferenceWin('600', '400', get_sub_dict(dict_key, references_dict), dict_key)

    def open_window_admin(self):
        self.root.destroy()
        # EditAdmin()

    def return_to_main_page(self):
        self.root.destroy()
        start_page()


class PrintForms(Gui):
    def __init__(self, width='360', height='500'):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.root.geometry('x'.join((self.width, self.height)))

    def create_widgets(self):
        tk.Label(self.root, text="Печать документов", font=LARGE_FONT).pack(pady=10, padx=10)
        tk.Button(self.root, text="Пакет документов при приеме", command=self.open_window_all_docs, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Заявление на зачисление", command=self.open_window_application,
                  width=30, height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Договор об образовании", command=self.open_window_agreement, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Согласие на обработку данных", command=self.open_window_consent, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Заявление на компенсацию РП", command=self.open_window_compensation, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Расписка о приеме заявления на КРП", command=self.open_window_receipt, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Доп.соглашение к договору", command=self.open_window_add_agreement,
                  width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Экспорт данных в АИСУ ПараГраф", command=self.open_window_export, width=30,
                  height=1).pack(padx=5, pady=5)
        tk.Button(self.root, text="Назад в Главное меню", bg='DarkSlateGray', fg='white',
                  command=self.return_to_start_page,
                  width=25,
                  height=1).pack()

    def open_window_all_docs(self):
        self.root.destroy()
        # EditCitizenship()

    def open_window_application(self):
        self.root.destroy()
        PrintApplicationWin()

    def open_window_agreement(self):
        self.root.destroy()
        # EditMode()

    def open_window_consent(self):
        self.root.destroy()
        # EditAdmin()

    def open_window_compensation(self):
        self.root.destroy()
        # EditAdmin()

    def open_window_receipt(self):
        self.root.destroy()
        # EditAdmin()

    def open_window_add_agreement(self):
        self.root.destroy()
        # EditAdmin()

    def open_window_export(self):
        self.root.destroy()
        # EditAdmin()

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
    def __init__(self):
        super().__init__()
        self.address = Address()

    def return_to_start_page(self):
        self.root.destroy()
        ProjectAddNew()


class NewChildCertificateWin(NewChild):
    def return_to_start_page(self):
        self.root.destroy()
        ProjectAddNew()


class ReferenceInfoEditWin(ReferenceInfoEdit):
    def return_to_start_page(self):
        self.root.destroy()
        ReferenceInfoEdit()


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
