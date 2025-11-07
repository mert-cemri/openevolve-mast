'''
This module contains a function to validate date strings based on specific rules.
'''
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12.
       The number of days is not less than 1 or higher than 30 days for months 4,6,9,11.
       The number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy
    :param date: A string representing the date.
    :return: True if the date is valid, False otherwise.
    """
    if not date:
        return False
    # Check if the date is in the correct format
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
    # Check month range
    if month < 1 or month > 12:
        return False
    # Check day range based on the month
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