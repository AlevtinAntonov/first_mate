from app_model.variables import label_child_list
from app_view_model.functions.functions import create_labels_in_grid


def show_child_labels(tab):
    create_labels_in_grid(tab, label_child_list)