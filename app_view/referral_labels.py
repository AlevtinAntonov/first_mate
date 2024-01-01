import tkinter as tk

from app_model.variables import LARGE_FONT, CONF_D_W, CONF


class OrganizationLabels:
    def __init__(self, root):
        self.root = root
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=3)
        tk.Label(self.root, text="Реквизиты организации", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W,
                                                                                columnspan=3, sticky="nsew")
        self.label_full_name = tk.Label(self.root, text="Полное название организации")
        self.label_full_name.grid(row=2, column=1, cnf=CONF)
        self.label_short_name = tk.Label(self.root, text="Краткое название организации")
        self.label_short_name.grid(row=4, column=1, cnf=CONF)
        self.label_legal_address = tk.Label(self.root, text="Юридический адрес")
        self.label_legal_address.grid(row=6, column=1, cnf=CONF)
        self.label_post_address = tk.Label(self.root, text="Почтовый адрес")
        self.label_post_address.grid(row=8, column=1, cnf=CONF)
        self.label_phone = tk.Label(self.root, text="Телефон")
        self.label_phone.grid(row=10, column=1, cnf=CONF)
        self.label_email = tk.Label(self.root, text="Электронная почта")
        self.label_email.grid(row=12, column=1, cnf=CONF)
        tk.Label(self.root, text="Реквизиты организации", font=LARGE_FONT).grid(row=14, column=1, cnf=CONF_D_W,
                                                                                columnspan=2, sticky="nsew")
        self.label_okpo = tk.Label(self.root, text="ОКПО")
        self.label_okpo.grid(row=16, column=1, cnf=CONF)
        self.label_ogrn = tk.Label(self.root, text="ОГРН")
        self.label_ogrn.grid(row=18, column=1, cnf=CONF)
        self.label_okogu = tk.Label(self.root, text="ОКОГУ")
        self.label_okogu.grid(row=20, column=1, cnf=CONF)
        self.label_inn = tk.Label(self.root, text="ИНН")
        self.label_inn.grid(row=22, column=1, cnf=CONF)
        self.label_kpp = tk.Label(self.root, text="КПП")
        self.label_kpp.grid(row=24, column=1, cnf=CONF)
        tk.Label(self.root, text="Руководитель организации", font=LARGE_FONT).grid(row=26, column=1, cnf=CONF_D_W,
                                                                                   columnspan=2, sticky="nsew")
        self.label_position_name = tk.Label(self.root, text="Должность руководителя")
        self.label_position_name.grid(row=28, column=1, cnf=CONF)
        self.label_boss_last_name = tk.Label(self.root, text="Фамилия руководителя")
        self.label_boss_last_name.grid(row=30, column=1, cnf=CONF)
        self.label_boss_first_name = tk.Label(self.root, text="Имя руководителя")
        self.label_boss_first_name.grid(row=32, column=1, cnf=CONF)
        self.label_boss_patronymic = tk.Label(self.root, text="Отчество руководителя")
        self.label_boss_patronymic.grid(row=34, column=1, cnf=CONF)
        tk.Label(self.root, text="Банковские реквизиты", font=LARGE_FONT).grid(row=36, column=1, cnf=CONF_D_W,
                                                                               columnspan=2, sticky="nsew")
        self.label_beneficiary = tk.Label(self.root, text="Получатель")
        self.label_beneficiary.grid(row=38, column=1, cnf=CONF)
        self.label_bank_name = tk.Label(self.root, text="Название банка")
        self.label_bank_name.grid(row=40, column=1, cnf=CONF)
        self.label_bic = tk.Label(self.root, text="БИК")
        self.label_bic.grid(row=42, column=1, cnf=CONF)
        self.label_cor_account = tk.Label(self.root, text="Корреспондентский счет")
        self.label_cor_account.grid(row=44, column=1, cnf=CONF)
        self.label_account = tk.Label(self.root, text="Расчетный счет")
        self.label_account.grid(row=46, column=1, cnf=CONF)


class ReferralLabelsWin3:
    def __init__(self, root):
        self.root = root
        self.label_referral_number = tk.Label(self.root, text="333Referral Number")
        self.label_referral_number.grid(row=2, column=0, sticky="e")
        self.entry_referral_number = tk.Entry(self.root)
        self.entry_referral_number.grid(row=2, column=1)

        self.label_referral_date = tk.Label(self.root, text="333Referral Date")
        self.label_referral_date.grid(row=3, column=0, sticky="e")
        self.entry_referral_date = tk.Entry(self.root)
        self.entry_referral_date.grid(row=3, column=1)

        self.label_referral_begin_date = tk.Label(self.root, text="333Referral Begin Date")
        self.label_referral_begin_date.grid(row=4, column=0, sticky="e")
        self.entry_referral_begin_date = tk.Entry(self.root)
        self.entry_referral_begin_date.grid(row=4, column=1)


if __name__ == '__main__':
    pass
