# извлечение вложенного словаря по заданному ключу из исходного словаря data_dict
def get_sub_dict(key, data_dict):
    if key in data_dict:
        sub_list = data_dict[key][1]
        result_dict = {f"column_{index}": value for index, value in enumerate(sub_list)}
        return result_dict
    else:
        return None


# название столбцов из таблицы
def get_column_names(cur, table_name):
    cur.execute("SELECT * FROM %s;" % table_name)
    column_names = [f[0] for f in cur.description]
    return column_names


def get_edit_record(self, db, table_name):
    with db as cur:
        column_names = get_column_names(cur, table_name)
        cur.execute(" SELECT * FROM %s WHERE (%s=?) " % (table_name, column_names[0]),
                    (self.tree.set(self.tree.selection()[0], '#1'),))
        row = cur.fetchone()
        if table_name == 'age':
            return row[0], row[1], row[2], row[3], row[4], row[5]
        elif table_name == 'users':
            return row[0], row[1], row[2], row[3], row[4], row[5], row[6]
        return row[0], row[1], row[2]
