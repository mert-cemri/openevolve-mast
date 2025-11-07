'''
Handles the reading of CSV files and extracting unique values from a specified column.
'''
import csv
class CSVProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
    def get_unique_values(self, column_name):
        unique_values = set()
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if column_name in row:
                    unique_values.add(row[column_name])
        return unique_values