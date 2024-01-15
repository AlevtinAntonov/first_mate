from app_view_model.reference_info.reference_page import ReferencePage


class EditCitizenship(ReferencePage):
    def __init__(self, width: str = '450', height: str = '450'):
        super().__init__(width, height)
        self.tree_columns = {'col_0': ['ИД №', 0, 0],
                             'col_1': ['Краткое наименование', 150, 150],
                             'col_2': ['Полное наименование', 350, 350]}

        self.project_title = 'Гражданство'
        self.tbl_name = 'citizenship'
        self.field_2 = 'citizenship_full_name'
        self.field_1 = 'citizenship_short_name'
        self.field_id = 'citizenship_id'
        self.sort_col = 'citizenship_id'
        self.label_1 = "Краткое название"
        self.label_2 = 'Полное название'

        def create_widgets(self):
            super().create_widgets()