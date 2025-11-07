'''
This module contains a function `valid_date` which validates a given date string.
The date is valid if all of the following rules are satisfied:
1. The date string is not empty.
2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12.
   And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11.
   And, the number of days is not less than 1 or higher than 29 for the month 2.
3. The months should not be less than 1 or higher than 12.
4. The date should be in the format: mm-dd-yyyy
'''
def valid_date(date):
    """Validates a given date string."""
    if not date:
        return False
    # Check format
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
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
# Example usage
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False