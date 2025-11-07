'''
This module contains a function to validate a given date string based on specific rules.
'''
def valid_date(date):
    import re
    # Check if the date string is empty
    if not date:
        return False
    # Check the format using regular expression
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    # Extract month, day, and year
    month, day, year = map(int, date.split('-'))
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
        if day < 1:
            return False
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    # If all checks pass, return True
    return True