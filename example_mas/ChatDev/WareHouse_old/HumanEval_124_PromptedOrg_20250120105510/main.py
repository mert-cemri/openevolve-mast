'''
This module contains a function `valid_date` that validates a given date string
based on specific rules and returns True if the date is valid, otherwise False.
'''
def is_leap_year(year):
    """Returns True if the given year is a leap year, otherwise False."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
def valid_date(date):
    """Validates a given date string and returns True if the date is valid otherwise False."""
    if not date:
        return False
    # Check if the date is in the format mm-dd-yyyy
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month_str, day_str, year_str = parts
    # Check if all parts are digits
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    # Validate month
    if month < 1 or month > 12:
        return False
    # Validate day based on the month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return False
    elif month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if is_leap_year(year):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    return True