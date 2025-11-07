'''
Utility functions for the Calendar tool.
Provides helper functions for converting month names to numbers.
'''
class CalendarUtils:
    @staticmethod
    def month_name_to_number(month_name):
        '''
        Converts a month name to its corresponding number.
        Raises ValueError if the month name is invalid.
        '''
        month_dict = {
            'january': 1, 'february': 2, 'march': 3, 'april': 4,
            'may': 5, 'june': 6, 'july': 7, 'august': 8,
            'september': 9, 'october': 10, 'november': 11, 'december': 12
        }
        month_name = month_name.lower()
        if month_name in month_dict:
            return month_dict[month_name]
        else:
            raise ValueError("Invalid month name")