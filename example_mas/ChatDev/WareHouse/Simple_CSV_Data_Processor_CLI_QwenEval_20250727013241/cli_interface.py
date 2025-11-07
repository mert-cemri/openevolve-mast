'''
Module to handle the command-line interface for the CSV Unique Values Finder.
'''
import sys
from csv_reader import CSVReader
from unique_values_finder import UniqueValuesFinder
class CLIInterface:
    def run(self):
        if len(sys.argv) < 3:
            print("Usage: python main.py <filename> <column_name>")
            sys.exit(1)
        filename = sys.argv[1]
        column_name = sys.argv[2]
        csv_reader = CSVReader(filename)
        csv_reader.read_csv()
        column_values = csv_reader.get_column_values(column_name)
        unique_values_finder = UniqueValuesFinder(column_values)
        unique_values = unique_values_finder.find_unique_values()
        print(f"Unique values in column '{column_name}':")
        for value in unique_values:
            print(value)