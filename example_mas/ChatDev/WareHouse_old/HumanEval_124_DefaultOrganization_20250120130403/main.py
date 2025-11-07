'''
This module contains a function to validate a date string based on specific rules.
'''
def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    if not date:
        return False
    # Split the date string into components
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
    # Validate day based on month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return False
    elif month in {4, 6, 9, 11}:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        # Check for leap year
        is_leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        if day < 1 or (day > 29 if is_leap_year else day > 28):
            return False
    # If all checks pass, the date is valid
    return True
# Example usage
if __name__ == "__main__":
    print(valid_date('03-11-2000'))  # True
    print(valid_date('15-01-2012'))  # False
    print(valid_date('04-0-2040'))   # False
    print(valid_date('06-04-2020'))  # True
    print(valid_date('06/04/2020'))  # False