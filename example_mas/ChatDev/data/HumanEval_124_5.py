'''
This module contains the implementation of the valid_date function which validates a given date string
and returns True if the date is valid according to specified rules, otherwise False.
'''
def valid_date(date):
    if not date:
        return False
    # Check format
    parts = date.split('-')
    if len(parts) != 3:
        return False
    # Check if all parts are digits
    if not all(part.isdigit() for part in parts):
        return False
    month, day, year = map(int, parts)
    # Validate month
    if month < 1 or month > 12:
        return False
    # Validate day based on month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return False
    elif month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    return True