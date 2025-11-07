'''
CSV parser to read and parse CSV files.
'''
import csv
class CSVParser:
    def parse_csv(self, file_path):
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data