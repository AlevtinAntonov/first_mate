from tkinter import messagebox

from app_model.db.db_query import gender, DB_DICT, team, person, query_insert_into_table_return_id, child, building, \
    age, focus, mode, benefit, referral, query_insert_into
from app_view_model.functions.functions import capitalize_double_surname, find_id, check_if_exists, current_timestamp, \
    find_person, save_access


def referral_save(db, referral_number, referral_date, referral_begin_date, referral_comment, child_last_name: str,
                  child_first_name: str, child_patronymic: str, child_male, child_date_of_birth, mode_get, building_get,
                  team_get, age_get, focus_get, benefit_get):
    try:
        child_last_name = capitalize_double_surname(child_last_name)
        child_first_name = capitalize_double_surname(child_first_name)
        child_patronymic = capitalize_double_surname(child_patronymic)

        gender_id = find_id(db, gender, DB_DICT[gender][0], DB_DICT[gender][1], child_male)
        team_id = find_id(db, team, DB_DICT[team][0], DB_DICT[team][1], team_get)
        if not check_if_exists(db, person, child_last_name, child_first_name, child_patronymic,
                               child_date_of_birth):
            with db as cur:
                query = query_insert_into_table_return_id(person, person) % DB_DICT[person]
                cur.execute(query,
                            (child_last_name, child_first_name, child_patronymic, child_date_of_birth, gender_id,
                             current_timestamp()))
                person_id = cur.fetchone()[0]
                query_add_child = query_insert_into_table_return_id(child, child) % DB_DICT[child]
                cur.execute(query_add_child, (person_id, current_timestamp()))
                child_id = cur.fetchone()[0]

        person_id = check_if_exists(db, person, child_last_name, child_first_name, child_patronymic,
                                    child_date_of_birth)
        child_id = find_person(db, child, person_id)
        building_id = find_id(db, building, DB_DICT[building][0], DB_DICT[building][1], building_get)
        age_id = find_id(db, age, DB_DICT[age][0], DB_DICT[age][1], age_get)
        focus_id = find_id(db, focus, DB_DICT[focus][0], DB_DICT[focus][1], focus_get)
        mode_id = find_id(db, mode, DB_DICT[mode][0], DB_DICT[mode][1], mode_get)
        benefit_id = find_id(db, benefit, DB_DICT[benefit][0], DB_DICT[benefit][1], benefit_get)
        # referral_id = find_id(db, referral, DB_DICT[referral][0], DB_DICT[referral][1], referral_number)



        with db as cur:
            query_check_referral_number = """SELECT 1 FROM referral WHERE referral_number = ? AND is_visible = True"""
            exists = cur.execute(query_check_referral_number, (referral_number,)).fetchone()
            if exists:
                messagebox.showinfo(title="Внимание!",
                                    message=f'Номер направления уже существует! Повторите ввод.')
                return
            query = query_insert_into(referral) % DB_DICT[referral]
            cur.execute(query,
                        (referral_number, referral_date, referral_begin_date, referral_comment, child_id, mode_id,
                         building_id, team_id, age_id, focus_id, benefit_id))
        save_access()
    except Exception as err:
        print(f'Ошибка в def referral_save - >>> {err}')
        messagebox.showinfo(title="Внимание!", message=f'Данные не записаны. Проверьте все ли внесено и '
                                                       f'попробуйте еще раз! Ошибка {err}')
