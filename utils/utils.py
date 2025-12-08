import os
from datetime import datetime

import dill


def str_years_difference(date1_str: str, date2_str: str, date_format="%Y-%m-%d"):
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    if date1 > date2:
        date1, date2 = date2, date1

    years = date2.year - date1.year

    # Adjust if the full year hasn't passed yet
    if (date2.month, date2.day) < (date1.month, date1.day):
        years -= 1

    return years


def years_difference(date1, date2):
    """
    Calculates the difference in full years between two dates.
    Handles both datetime.date and datetime.datetime objects.
    """
    # Convert datetime.datetime to datetime.date if necessary
    if isinstance(date1, datetime):
        date1 = date1.date()
    if isinstance(date2, datetime):
        date2 = date2.date()

    if date1 > date2:
        date1, date2 = date2, date1

    years = date2.year - date1.year

    # Adjust if the full year hasn't passed yet
    if (date2.month, date2.day) < (date1.month, date1.day):
        years -= 1

    return years

def get_dmn_from_pkl(file_path):
    print(os.getcwd())
    try:
        with open(file_path, 'rb') as f:
            dmn_object = dill.load(f)
        print(f"Successfully loaded DMN object from: {file_path}")
        return dmn_object
    except Exception as ex:
        print(f"Error loading pickle file {file_path}: {ex}")
        raise ex