from app_model.domain.person import Person


class Child(Person):
    def __init__(self, person_id: int = None, team_id: int = None):
        super().__init__()
        self.person_id = person_id
        self.team_id = team_id

