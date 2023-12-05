from datetime import datetime


class Referral:
    def __init__(self, referral_id: int, referral_number: str, referral_date: datetime, referral_begin_date: datetime,
                 referral_comment: str, child_id: int, mode_id: int, building_id: int, team_id: int, age_id: int,
                 focus_id: int, benefit_id: int, is_visible: bool = True):
        self.referral_id = referral_id
        self.referral_number = referral_number
        self.referral_date = referral_date
        self.referral_begin_date = referral_begin_date
        self.referral_comment = referral_comment
        self.child_id = child_id
        self.mode_id = mode_id
        self.building_id = building_id
        self.team_id = team_id
        self.age_id = age_id
        self.focus_id = focus_id
        self.benefit_id = benefit_id
        self.is_visible = is_visible
