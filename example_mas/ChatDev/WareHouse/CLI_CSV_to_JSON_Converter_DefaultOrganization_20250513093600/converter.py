'''
Module containing the CSVtoJSONConverter class for converting CSV files to JSON format.
'''
import csv
import json
class CSVtoJSONConverter:
    def convert(self, csv_path, json_path):
        '''
        Read a CSV file and write its contents to a JSON file.
        '''
        with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        with open(json_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)