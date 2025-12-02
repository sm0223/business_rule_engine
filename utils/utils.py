from datetime import datetime

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
