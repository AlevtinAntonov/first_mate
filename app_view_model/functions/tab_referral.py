from app_model.variables import label_referral_list
from app_view_model.functions.functions import create_labels_in_grid


def show_referral(tab):
    create_labels_in_grid(tab, label_referral_list)