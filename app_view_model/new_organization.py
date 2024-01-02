import tkinter as tk
from tkinter import ttk

from app_model.db.db_connect import db
from app_model.db.db_query import query_insert_into, organization, DB_DICT, get_total_table_records
from app_model.variables import CONF_GRID_WIDTH
from app_view.gui_input_window import Gui
from app_view.referral_labels import OrganizationLabels
from app_view_model.functions.functions import next_entries, save_access, clear_text


class NewOrganization(Gui):
    def __init__(self, width: str = '500', height: str = '700'):
        super().__init__(width, height)
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))
        self.labels = OrganizationLabels(self.root)
        # self.populate_with_last_organization_data()  # Call the method to populate with the last organization data
        self.current_record_index = 0  # Store the index of the current record
        self.total_records = get_total_table_records(db, organization)  # Count the total number of records
        self.populate_with_organization_data(self.current_record_index)  # Populate with the current organization data
        self.initialize_shortcuts()

    def create_widgets(self):
        self.entry_full_name = ttk.Entry(self.root)
        self.entry_full_name.grid(row=2, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_short_name = ttk.Entry(self.root)
        self.entry_short_name.grid(row=4, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_legal_address = ttk.Entry(self.root)
        self.entry_legal_address.grid(row=6, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_post_address = ttk.Entry(self.root)
        self.entry_post_address.grid(row=8, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_phone = ttk.Entry(self.root)
        self.entry_phone.grid(row=10, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.grid(row=12, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_okpo = ttk.Entry(self.root)
        self.entry_okpo.grid(row=16, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_ogrn = ttk.Entry(self.root)
        self.entry_ogrn.grid(row=18, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_okogu = ttk.Entry(self.root)
        self.entry_okogu.grid(row=20, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_inn = ttk.Entry(self.root)
        self.entry_inn.grid(row=22, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_kpp = ttk.Entry(self.root)
        self.entry_kpp.grid(row=24, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_position_name = ttk.Entry(self.root)
        self.entry_position_name.grid(row=28, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_boss_last_name = ttk.Entry(self.root)
        self.entry_boss_last_name.grid(row=30, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_boss_first_name = ttk.Entry(self.root)
        self.entry_boss_first_name.grid(row=32, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_boss_patronymic = ttk.Entry(self.root)
        self.entry_boss_patronymic.grid(row=34, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_beneficiary = ttk.Entry(self.root)
        self.entry_beneficiary.grid(row=38, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_bank_name = ttk.Entry(self.root)
        self.entry_bank_name.grid(row=40, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_bic = ttk.Entry(self.root)
        self.entry_bic.grid(row=42, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_cor_account = ttk.Entry(self.root)
        self.entry_cor_account.grid(row=44, column=2, cnf=CONF_GRID_WIDTH)
        self.entry_account = ttk.Entry(self.root)
        self.entry_account.grid(row=46, column=2, cnf=CONF_GRID_WIDTH)

        self.save_button = tk.Button(self.root, text="Сохранить", bg='red', fg='white',
                                     command=self.save_and_return_with_access)
        self.save_button.grid(row=60, column=1)

        self.cancel_button = tk.Button(self.root, text="Закрыть", bg='DarkSlateGray', fg='white',
                                       command=self.return_to_start_page)
        self.cancel_button.grid(row=60, column=2)

        self.next_button = tk.Button(self.root, text=" >>> ", command=self.next_record)
        self.next_button.grid(row=1, column=2)

        self.previous_button = tk.Button(self.root, text=" <<< ", command=self.previous_record)
        self.previous_button.grid(row=1, column=1)

        next_entries(self.root)

    def save_and_return(self):
        with db as cur:  # Start a context manager to handle the database connection
            query_insert = query_insert_into(organization) % DB_DICT[organization]
            # Insert the data into the 'ORGANIZATION' table using the entries
            cur.execute(query_insert, (self.entry_full_name.get(),
                                       self.entry_short_name.get(),
                                       self.entry_legal_address.get(),
                                       self.entry_post_address.get(),
                                       self.entry_phone.get(),
                                       self.entry_email.get(),
                                       self.entry_okpo.get(),
                                       self.entry_ogrn.get(),
                                       self.entry_okogu.get(),
                                       self.entry_inn.get(),
                                       self.entry_kpp.get(),
                                       self.entry_position_name.get(),
                                       self.entry_boss_last_name.get(),
                                       self.entry_boss_first_name.get(),
                                       self.entry_boss_patronymic.get(),
                                       self.entry_beneficiary.get(),
                                       self.entry_bank_name.get(),
                                       self.entry_bic.get(),
                                       self.entry_cor_account.get(),
                                       self.entry_account.get()
                                       ))

    def save_and_return_with_access(self):
        self.save_and_return()
        save_access()

    def next_record(self):
        if self.current_record_index < self.total_records - 1:
            clear_text(self.root)
            self.current_record_index += 1
            self.populate_with_organization_data(self.current_record_index)

    def previous_record(self):
        if self.current_record_index > 0:
            clear_text(self.root)
            self.current_record_index -= 1
            self.populate_with_organization_data(self.current_record_index)

    def populate_entry_with_data(self, data):
        if data:
            self.entry_full_name.insert(0, data[1])
            self.entry_short_name.insert(0, data[2])
            self.entry_legal_address.insert(0, data[3])
            self.entry_post_address.insert(0, data[4])
            self.entry_phone.insert(0, data[5])
            self.entry_email.insert(0, data[6])
            self.entry_okpo.insert(0, data[7])
            self.entry_ogrn.insert(0, data[8])
            self.entry_okogu.insert(0, data[9])
            self.entry_inn.insert(0, data[10])
            self.entry_kpp.insert(0, data[11])
            self.entry_position_name.insert(0, data[12])
            self.entry_boss_last_name.insert(0, data[13])
            self.entry_boss_first_name.insert(0, data[14])
            self.entry_boss_patronymic.insert(0, data[15])
            self.entry_beneficiary.insert(0, data[16])
            self.entry_bank_name.insert(0, data[17])
            self.entry_bic.insert(0, data[18])
            self.entry_cor_account.insert(0, data[19])
            self.entry_account.insert(0, data[20])

    def populate_with_last_organization_data(self):
        query = "SELECT FIRST 1 * FROM organization ORDER BY organization_id DESC"
        with db as cur:
            cur.execute(query)
            last_organization = cur.fetchone()
        self.populate_entry_with_data(last_organization)

    def populate_with_organization_data(self, index):
        query = f"SELECT FIRST 1 SKIP {index} * FROM organization ORDER BY organization_id"
        with db as cur:
            cur.execute(query)
            organization_data = cur.fetchone()
        self.populate_entry_with_data(organization_data)
