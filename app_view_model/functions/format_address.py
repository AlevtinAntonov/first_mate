dict_address = {
    'д.': None,
    'корп.': None,
    'лит.': None,
    'стр.': None,
    'кв.': None,
}


# Add values from 5 last elements of list to empty dictionary without last element(later added)
def assign_values(dictionary, lst):
    keys = list(dictionary.keys())
    values = lst[-6:-1]
    for i in range(5):
        dictionary[keys[i]] = values[i] if values[i] != '' and values[i] is not None else None
    return dictionary


# Remove empties from beginig of string
def remove_until_first_alnum(s):
    for i, c in enumerate(s):
        if c.isalnum():
            return s[i:].lstrip()
    return s


# Convert dictionary to string
def dict_to_string(dictionary):
    result = ""
    for key, value in dictionary.items():
        if value != '' and value is not None:
            result += f"{key} {value}, "
    return result.rstrip(", ")


# Format address from DataBase to string without empty data
def format_address(list_input):
    dict_input = dict_address
    formatted_list = ''
    if list_input[0] != "" and list_input[0] is not None:
        formatted_list = list_input[0]
    if list_input[1] != "" and list_input[1] is not None:
        formatted_list += f', {list_input[1]}'
        if list_input[2] != "" and list_input[2] is not None:
            formatted_list += f' {list_input[2]}'
    if list_input[3] != "" and list_input[3] is not None:
        formatted_list += f', {list_input[3]} р-н'
    if list_input[4] != "" and list_input[4] is not None:
        formatted_list += f', {list_input[4]} {list_input[5]}'
    if list_input[6] != "" and list_input[6] is not None:
        formatted_list += f', {list_input[6]} {list_input[7]}'
    if list_input[8] != "" and list_input[8] is not None:
        formatted_list += f', {list_input[8]} {list_input[9]}, '
    formatted_list += dict_to_string(assign_values(dict_input, list_input))
    formatted_list = remove_until_first_alnum(formatted_list)
    return formatted_list


if __name__ == '__main__':

    address_list = (
        '197375', 'Санкт-Петербург', None, '', 'Санкт-Петербург', 'г.', '', None, 'Вербная', 'ул.', '20/3', '', 'А', '',
        '300')
    # print(dict_to_string(assign_values(dict_address, address_list)))
    print(format_address(address_list))


