import tkinter as tk
from tkinter import ttk

from app_model.variables import LARGE_FONT
from app_view.gui_input_window import Gui

from app_view_model.functions.update_data_app import UpdateDataApp
from app_view_model.functions.update_datas import query_tab_birth_certificate, query_child_doc_move_reg_adr, \
    query_read_birth_certificate, query_read_address_reg, query_read_parent_address_reg, \
    query_read_parent_document, query_tab_parent_document, query_read_movement, query_read_referral, \
    query_child_referral, query_read_compensation, query_child_compensation


class NewPersonalDatas(Gui):
    def __init__(self, width: str = '850', height: str = '600'):
        super().__init__(width, height)
        self.root.geometry(f"{width}x{height}")

    def create_widgets(self):
        self.child_name_var = tk.StringVar()
        # Frame для размещения заголовка окна
        title_frame = tk.Frame(self.root)
        title_frame.pack()

        # Заголовок окна
        title_label = tk.Label(title_frame, text="Личные дела воспитанников", font=LARGE_FONT)
        title_label.pack()

        # Создание вкладок
        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Verdana", 10), padding=[5, 5])
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill="both")

        self.tab_birth_certificate = ttk.Frame(tab_control)
        self.tab_address = ttk.Frame(tab_control)
        self.tab_parent_document = ttk.Frame(tab_control)
        self.tab_address_parent = ttk.Frame(tab_control)
        self.tab_referral = ttk.Frame(tab_control)
        self.tab_movement = ttk.Frame(tab_control)
        self.tab_compensation = ttk.Frame(tab_control)

        tab_control.add(self.tab_birth_certificate, text='Св-во о рождении')
        tab_control.add(self.tab_address, text='Адрес ребенка')
        tab_control.add(self.tab_parent_document, text='Паспорт родителя')
        tab_control.add(self.tab_address_parent, text='Адрес родителя')
        tab_control.add(self.tab_movement, text='Движение')
        tab_control.add(self.tab_compensation, text='Компенсация')
        tab_control.add(self.tab_referral, text='Направление')

        # вкладка tab_birth_certificate
        UpdateDataApp(self.tab_birth_certificate, 'birth_certificate', query_read_birth_certificate,
                      query_tab_birth_certificate, 'child')

        # вкладка tab_address
        UpdateDataApp(self.tab_address, 'addresses', query_read_address_reg, query_child_doc_move_reg_adr, 'child')

        # вкладка tab_address_parent
        UpdateDataApp(self.tab_parent_document, 'parent_document', query_read_parent_document,
                      query_tab_parent_document, 'parents')

        # вкладка tab_address_parent
        UpdateDataApp(self.tab_address_parent, 'addresses_parent', query_read_parent_address_reg,
                      query_child_doc_move_reg_adr, 'parents')

        # вкладка self.tab_movement
        UpdateDataApp(self.tab_movement, 'agreement', query_read_movement,
                      query_child_doc_move_reg_adr, 'movement')

        # вкладка self.tab_referral
        UpdateDataApp(self.tab_referral, 'child_referral', query_read_referral,
                      query_child_referral, 'referral')

        # вкладка self.tab_compensation
        UpdateDataApp(self.tab_compensation, 'child_compensation', query_read_compensation,
                      query_child_compensation, 'compensation_statement')

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()
        self.close_button = tk.Button(buttons_frame, text="Закрыть", bg='DarkSlateGray', fg='white',
                                      command=self.return_to_start_page)
        self.close_button.pack(padx=10, pady=10)
