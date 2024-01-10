from app_model.variables import label_parent_list
from app_view_model.functions.functions import create_labels_in_grid


def show_family_labels(tab):
    create_labels_in_grid(tab, label_parent_list)