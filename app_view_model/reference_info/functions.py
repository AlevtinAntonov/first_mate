# для извлечения вложенного словаря по заданному ключу из исходного словаря data_dict
def get_sub_dict(key, data_dict):
    if key in data_dict:
        sub_list = data_dict[key]
        result_dict = {f"column_{index}": value for index, value in enumerate(sub_list)}
        return result_dict
    else:
        return None