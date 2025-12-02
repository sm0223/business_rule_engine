from datetime import datetime


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


def years_difference(date1:datetime, date2:datetime, date_format="%Y-%m-%d"):

    if date1 > date2:
        date1, date2 = date2, date1

    years = date2.year - date1.year

    # Adjust if the full year hasn't passed yet
    if (date2.month, date2.day) < (date1.month, date1.day):
        years -= 1

    return years
