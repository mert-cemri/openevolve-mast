'''
Handles the command-line interface interactions for the Calendar tool.
Parses arguments, validates inputs, and displays the calendar.
'''
import calendar
from calendar_utils import CalendarUtils
class CalendarCLI:
    def run(self, args):
        '''
        Main method to run the CLI tool.
        Parses arguments and displays the calendar.
        '''
        month, year = self.parse_arguments(args)
        self.display_calendar(month, year)
    def parse_arguments(self, args):
        '''
        Parses the command-line arguments to extract month and year.
        Validates the inputs and converts month names to numbers if necessary.
        '''
        if len(args) != 2:
            raise ValueError("Invalid number of arguments")
        month = args[0]
        year = int(args[1])
        if month.isdigit():
            month = int(month)
        else:
            month = CalendarUtils.month_name_to_number(month)
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        return month, year
    def display_calendar(self, month, year):
        '''
        Displays the calendar for the given month and year.
        '''
        cal = calendar.month(year, month)
        print(cal)