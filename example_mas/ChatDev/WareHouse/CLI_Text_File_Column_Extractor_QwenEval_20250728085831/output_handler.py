'''
Outputs the extracted data to the console or a file.
'''
import csv
import sys
def output_data(extracted_data, output_path, delimiter):
    if output_path:
        with open(output_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerows(extracted_data)
    else:
        writer = csv.writer(sys.stdout, delimiter=delimiter)
        writer.writerows(extracted_data)