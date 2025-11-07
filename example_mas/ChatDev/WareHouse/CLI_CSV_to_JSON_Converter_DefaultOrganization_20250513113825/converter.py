'''
Utility functions for converting CSV files to JSON format.
'''
import csv
import json
def convert_csv_to_json(input_path, output_path):
    '''
    Convert a CSV file to a JSON file.
    :param input_path: Path to the input CSV file.
    :param output_path: Path to the output JSON file.
    '''
    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        with open(output_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
    except IOError as e:
        print(f"IO error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")