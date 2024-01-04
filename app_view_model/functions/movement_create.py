from tkinter import messagebox

from app_model.db.db_query import query_insert_into_table_return_id, DB_DICT, movement
from app_view_model.functions.functions import save_access, find_id, current_timestamp


def movement_create(db, statement_number, statement_date, date_of_joining_team, contract_number, contarct_date,
                    contract_begin_date, order_of_admission_number, order_of_admission_date,
                    child_id, referral_id, team_id, person_id):
    try:
        order_of_admission_number = order_of_admission_number or '0'
        order_of_admission_date = '01.01.2000' if order_of_admission_number == '0' else order_of_admission_date

        with db as cur:
            query_check_contract_number = """SELECT 1 FROM movement WHERE contract_number = ? AND is_visible = True"""
            exists = cur.execute(query_check_contract_number, (contract_number,)).fetchone()
            if exists or statement_number == '':
                messagebox.showinfo(title="Внимание!",
                                    message=f'Номер договора уже существует или не заполнен! Повторите ввод.')
                return
            query_add_movement = query_insert_into_table_return_id(movement, movement) % DB_DICT[movement]
            cur.execute(query_add_movement,
                        (statement_number, statement_date, date_of_joining_team, contract_number, contarct_date,
                         contract_begin_date, order_of_admission_number, order_of_admission_date, current_timestamp(),
                         child_id, referral_id, team_id, person_id))
        save_access()

    except Exception as err:
        print(f'Ошибка в def movement_create - >>> {err}')
        messagebox.showinfo(title="Внимание!", message=f'Данные для договора не записаны. Проверьте все ли внесено и '
                                                       f'попробуйте еще раз! Ошибка {err}')


if __name__ == '__main__':
    pass
