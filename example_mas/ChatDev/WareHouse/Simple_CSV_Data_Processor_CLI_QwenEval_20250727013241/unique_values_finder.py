'''
Module to find unique values in a specified column of a CSV file.
'''
class UniqueValuesFinder:
    def __init__(self, column_values):
        self.column_values = column_values
    def find_unique_values(self):
        return list(set(self.column_values))