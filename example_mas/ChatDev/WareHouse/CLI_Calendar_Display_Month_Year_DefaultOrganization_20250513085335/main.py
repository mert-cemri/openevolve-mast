'''
Main application file for the calendar CLI tool.
'''
import argparse
from calendar_generator import CalendarGenerator
import calendar
def main():
    '''
    Parse command-line arguments and display the calendar for the given month and year.
    '''
    parser = argparse.ArgumentParser(description='Display a calendar for a given month and year.')
    parser.add_argument('month', type=str, help='Month as a number (1-12) or name (e.g., January)')
    parser.add_argument('year', type=int, help='Year as a four-digit number')
    args = parser.parse_args()
    month_input = args.month
    year = args.year
    # Check if the month is numeric or a name
    if month_input.isdigit():
        month = int(month_input)
        if month < 1 or month > 12:
            print("Error: Please enter a valid month (1-12).")
            return
    else:
        try:
            month = list(calendar.month_name).index(month_input.capitalize())
            if month == 0:
                raise ValueError
        except ValueError:
            print("Error: Please enter a valid month name.")
            return
    calendar_generator = CalendarGenerator()
    calendar_output = calendar_generator.generate_calendar(month, year)
    print(calendar_output)
if __name__ == "__main__":
    main()