from app_model.domain.person import Person


class Parents(Person):
    def __init__(self, person_id: int = None, status_id: int = None):
        super().__init__()
        self.person_id = person_id
        self.status_id = status_id
