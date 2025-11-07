'''
This module contains a function to validate a given date string based on specific rules.
'''
def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12.
       The number of days is not less than 1 or higher than 30 days for months 4,6,9,11.
       The number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy
    Args:
        date (str): The date string to validate.
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    if not date:
        return False
    # Check if the date is in the correct format
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month_str, day_str, year_str = parts
    # Validate month
    if not month_str.isdigit() or not (1 <= int(month_str) <= 12):
        return False
    # Validate day
    if not day_str.isdigit():
        return False
    month = int(month_str)
    day = int(day_str)
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if not (1 <= day <= 31):
            return False
    elif month in {4, 6, 9, 11}:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if not (1 <= day <= 29):
            return False
    # Validate year
    if not year_str.isdigit():
        return False
    return True