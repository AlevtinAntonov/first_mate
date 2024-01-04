def display_referral_data(db):
    dict_combo = {}
    # Подключение к базе данных
    with db as cur:
        query_select_ref_number = """
        SELECT referral.referral_id, referral.referral_number, child.person_id, team.team_name, person.last_name, person.first_name, 
               person.patronymic, person.date_of_birth, referral.child_id, referral.team_id  
        FROM referral 
        INNER JOIN child ON referral.child_id = child.child_id 
        INNER JOIN team ON referral.team_id = team.team_id 
        INNER JOIN person ON child.person_id = person.person_id
        WHERE referral.is_visible = True
        ORDER BY referral.referral_date DESC
        """
        # Получение данных из базы
        cur.execute(query_select_ref_number)
        rows = cur.fetchall()

        # Передача данных в словарь
        if rows:
            [dict_combo.update({row[0]: (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])}) for row in rows]
        else:
            print("Номер направления не найден")
    return dict_combo
