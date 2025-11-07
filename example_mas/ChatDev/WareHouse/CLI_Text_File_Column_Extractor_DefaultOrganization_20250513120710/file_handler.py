'''
File handler for reading and parsing CSV or space-delimited text files.
'''
import csv
class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
    def read_file(self):
        with open(self.filepath, 'r') as file:
            return file.readlines()
    def parse_file(self, columns):
        data = self.read_file()
        if self.filepath.endswith('.csv'):
            delimiter = ','
            reader = csv.reader(data, delimiter=delimiter)
        else:
            # Handle space-delimited files
            reader = (line.split() for line in data)
        # Determine if columns are numbers or headers
        first_row = next(reader)
        if all(col.isdigit() for col in columns.split(',')):
            column_indices = [int(col) for col in columns.split(',')]
        else:
            column_indices = [first_row.index(col) for col in columns.split(',')]
        extracted_data = []
        for row in reader:
            extracted_row = [row[i] for i in column_indices]
            extracted_data.append(','.join(extracted_row))
        return extracted_data