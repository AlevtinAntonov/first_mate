import configparser


def db_config():
    # читаем путь к базе данных из файла base.ini
    config = configparser.ConfigParser()
    config.read('base.ini')
    db_path = config['DATABASE']['path']

    # записываем путь к базе в файл variables.py
    with open('app_model/db_path.py', 'w') as file:
        file.write(f"DB_PATH = '{db_path}'")

    print("Константа DB_PATH записана в файл db_path.py!")
