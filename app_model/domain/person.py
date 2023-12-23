from datetime import date


class Person:
    def __init__(self, last_name: str = None, first_name: str = None, patronymic: str = None,
                 date_of_birth: date = None, date_of_add: date = None, date_of_modify: date = None,
                 date_of_del: date = None, gender_id: int = None, citizenship_id: int = None, document_id: int = None,
                 sniils: str = None, is_visible: bool = True):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.date_of_birth = date_of_birth
        self.date_of_add = date_of_add
        self.date_of_modify = date_of_modify
        self.date_of_del = date_of_del
        self.gender_id = gender_id
        self.citizenship_id = citizenship_id
        self.document_id = document_id
        self.sniils = sniils
        self.is_visible = is_visible
