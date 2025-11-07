'''
Main application file for the calendar CLI tool.
'''
import calendar
def get_month_number(month):
    '''
    Convert month name to month number if necessary.
    '''
    try:
        month = int(month)
        if 1 <= month <= 12:
            return month
        else:
            raise ValueError("Month must be between 1 and 12.")
    except ValueError:
        month = month.capitalize()
        months = list(calendar.month_name)
        if month in months:
            return months.index(month)
        else:
            raise ValueError("Invalid month name.")
def show_calendar(month_input, year_input):
    '''
    Display the calendar for the given month and year.
    '''
    try:
        month = get_month_number(month_input)
        year = int(year_input)
        cal = calendar.month(year, month)
        print(cal)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    month_input = input("Enter month (name or number): ")
    year_input = input("Enter year: ")
    show_calendar(month_input, year_input)