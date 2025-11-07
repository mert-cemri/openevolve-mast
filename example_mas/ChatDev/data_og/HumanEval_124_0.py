'''
This module contains a function to validate date strings based on specific rules.
'''
def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    if not date:
        return False
    # Check if the date format is mm-dd-yyyy
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    # Check month range
    if month < 1 or month > 12:
        return False
    # Check day range based on month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return False
    elif month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    return True
# Example usage:
# print(valid_date('03-11-2000'))  # True
# print(valid_date('15-01-2012'))  # False
# print(valid_date('04-0-2040'))   # False
# print(valid_date('06-04-2020'))  # True
# print(valid_date('06/04/2020'))  # False