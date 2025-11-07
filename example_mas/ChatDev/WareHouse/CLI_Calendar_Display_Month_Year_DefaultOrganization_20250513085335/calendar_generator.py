'''
Calendar generator module for creating a calendar for a given month and year.
'''
import calendar
class CalendarGenerator:
    def generate_calendar(self, month, year):
        '''
        Generate a calendar for the given month and year.
        '''
        cal = calendar.TextCalendar(calendar.SUNDAY)
        return cal.formatmonth(year, month)