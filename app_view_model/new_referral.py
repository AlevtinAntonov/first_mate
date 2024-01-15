import tkinter as tk
from tkinter import ttk, BOTH

from app_model.db.db_connect import db
from app_model.db.db_query import building, DB_DICT, age, focus, benefit, team, gender, mode
from app_model.domain.child import Child
from app_model.domain.referral import Referral
from app_model.variables import LARGE_FONT, label_referral_list, DEFAULT_REFERRAL_NUMBER, CURRENT_YEAR, CONF_D_W, \
    CURRENT_MONTH, CURRENT_DAY, DEFAULT_BORN_YEAR, DEFAULT_BORN_MONTH, DEFAULT_BORN_DAY, DEFAULT_YEAR, DEFAULT_MONTH, \
    DEFAULT_DAY, CONF
from app_view.gui_input_window import Gui
from app_view_model.functions.functions import create_labels_in_grid, select_date, \
    select_from_db, next_entries, buttons_add_new, on_validate_input
from app_view_model.functions.referral_create import referral_save


class NewReferral(Gui):
    def __init__(self, referral: Referral = None, width: str = '650', height: str = '400', child: Child = None,
                 comment: str = None):
        super().__init__(width, height)
        self.child = child
        self.referral = referral
        self.height = height
        self.width = width
        self.root.geometry('x'.join((self.width, self.height)))
        self.comment = comment

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill=BOTH, expand=1)
        vcmd = self.root.register(on_validate_input)

        tk.Label(frame, text="Ввод направления", font=LARGE_FONT).grid(row=0, column=1, cnf=CONF_D_W, columnspan=4,
                                                                       sticky="nsew")
        create_labels_in_grid(frame, label_referral_list)
        referral_number = ttk.Entry(frame)
        referral_number.insert(0, DEFAULT_REFERRAL_NUMBER)
        referral_number.grid(row=2, column=1, cnf=CONF_D_W)
        referral_date = select_date(frame, CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, 2, 3, CONF_D_W)
        last_name = ttk.Entry(frame, validate='key', validatecommand=(vcmd, "%S"))
        last_name.grid(row=4, column=1, cnf=CONF_D_W)
        first_name = ttk.Entry(frame, validate='key', validatecommand=(vcmd, "%S"))
        first_name.grid(row=4, column=3, cnf=CONF_D_W)
        patronymic = ttk.Entry(frame, validate='key', validatecommand=(vcmd, "%S"))
        patronymic.grid(row=6, column=1, cnf=CONF_D_W)
        gender_id = select_from_db(frame, db, gender, DB_DICT[gender][0], DB_DICT[gender][1], 8, 1, CONF_D_W, width=15)
        date_of_birth = select_date(frame, DEFAULT_BORN_YEAR, DEFAULT_BORN_MONTH, DEFAULT_BORN_DAY, 8, 3,
                                    CONF_D_W)
        building_id = select_from_db(frame, db, building, DB_DICT[building][0], DB_DICT[building][1], 10, 1, CONF_D_W,
                                     2)
        age_id = select_from_db(frame, db, age, DB_DICT[age][0], DB_DICT[age][1], 12, 1, CONF_D_W, 2)
        focus_id = select_from_db(frame, db, focus, DB_DICT[focus][0], DB_DICT[focus][1], 14, 1, CONF_D_W, 2)
        mode_id = select_from_db(frame, db, mode, DB_DICT[mode][0], DB_DICT[mode][1], 16, 1, CONF_D_W, 2)
        referral_begin_date = select_date(frame, DEFAULT_YEAR, DEFAULT_MONTH, DEFAULT_DAY, 18, 1, CONF_D_W)
        benefit_id = select_from_db(frame, db, benefit, DB_DICT[benefit][0], DB_DICT[benefit][1], 20, 1, CONF_D_W, 2)
        team_id = select_from_db(frame, db, team, DB_DICT[team][0], DB_DICT[team][1], 22, 1, CONF_D_W, 2)
        comment = ttk.Entry(frame, width=50)
        comment.grid(row=24, column=1, cnf=CONF_D_W, columnspan=3)

        buttons_add_new(self, frame, 30)
        btn_ok = tk.Button(frame, text='Сохранить', bg='red', fg='white')
        btn_ok.grid(row=30, column=3, cnf=CONF)
        btn_ok.bind('<Button-1>',
                    lambda event: (referral_save(db, referral_number.get(),
                                                 referral_date.get(),
                                                 referral_begin_date.get(),
                                                 comment.get(),
                                                 last_name.get(),
                                                 first_name.get(),
                                                 patronymic.get(),
                                                 gender_id.get(),
                                                 date_of_birth.get(),
                                                 mode_id.get(),
                                                 building_id.get(),
                                                 team_id.get(),
                                                 age_id.get(),
                                                 focus_id.get(),
                                                 benefit_id.get()
                                                 )))

        next_entries(frame)


if __name__ == '__main__':
    pass
