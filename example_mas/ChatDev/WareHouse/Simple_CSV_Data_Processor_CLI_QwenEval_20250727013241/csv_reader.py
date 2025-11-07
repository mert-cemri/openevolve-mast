'''
Module to handle reading and parsing CSV files.
'''
import csv
import sys
class CSVReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
    def read_csv(self):
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            sys.exit(1)
        except csv.Error as e:
            print(f"Error reading CSV file '{self.filename}': {e}")
            sys.exit(1)
    def get_column_values(self, column_name):
        if not self.data:
            print("Error: No data available. Please read the CSV file first.")
            sys.exit(1)
        if column_name not in self.data[0]:
            print(f"Error: Column '{column_name}' not found in the CSV file.")
            sys.exit(1)
        return [row[column_name] for row in self.data]