'''
Reads the input file based on the delimiter.
'''
import csv
def read_file(file_path, delimiter):
    with open(file_path, 'r', newline='') as file:
        if delimiter == ',':
            reader = csv.reader(file)
        else:
            reader = csv.reader(file, delimiter=delimiter)
        return list(reader)