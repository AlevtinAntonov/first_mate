from app_model.variables import label_compensation
from app_view_model.functions.functions import create_labels_in_grid


def show_compensation_labels(tab):
    create_labels_in_grid(tab, label_compensation)