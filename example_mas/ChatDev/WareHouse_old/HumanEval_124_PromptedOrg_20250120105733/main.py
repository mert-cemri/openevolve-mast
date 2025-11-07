'''
This function validates a given date string and returns True if the date is valid according to the specified rules, otherwise False.
'''
def valid_date(date):
    # Check if the date string is empty
    if not date:
        return False
    # Check if the date string is in the correct format
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False
    # Split the date string into components
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False
    # Check if the month is valid
    if month < 1 or month > 12:
        return False
    # Days in each month
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    # Adjust for leap year
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29
    # Check if the day is valid for the given month
    if day < 1 or day > days_in_month.get(month, 0):
        return False
    return True