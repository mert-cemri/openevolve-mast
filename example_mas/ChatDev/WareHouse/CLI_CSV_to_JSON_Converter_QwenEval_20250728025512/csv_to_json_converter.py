'''
Module containing the logic to convert a CSV file to a JSON file.
'''
import csv
import json
def convert_csv_to_json(input_csv_path, output_json_path):
    '''
    Reads a CSV file and writes the data to a JSON file.
    Each row in the CSV becomes a JSON object.
    '''
    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    with open(output_json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Conversion successful: {input_csv_path} -> {output_json_path}")