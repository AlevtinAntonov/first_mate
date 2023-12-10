import tkinter as tk


class ReferralLabels:
    def __init__(self, root):
        self.root = root
        self.label_referral_number = tk.Label(self.root, text="Referral Number")
        self.label_referral_number.grid(row=2, column=0, sticky="e")
        self.entry_referral_number = tk.Entry(self.root)
        self.entry_referral_number.grid(row=2, column=1)

        self.label_referral_date = tk.Label(self.root, text="Referral Date")
        self.label_referral_date.grid(row=3, column=0, sticky="e")
        self.entry_referral_date = tk.Entry(self.root)
        self.entry_referral_date.grid(row=3, column=1)

        self.label_referral_begin_date = tk.Label(self.root, text="Referral Begin Date")
        self.label_referral_begin_date.grid(row=4, column=0, sticky="e")
        self.entry_referral_begin_date = tk.Entry(self.root)
        self.entry_referral_begin_date.grid(row=4, column=1)


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
