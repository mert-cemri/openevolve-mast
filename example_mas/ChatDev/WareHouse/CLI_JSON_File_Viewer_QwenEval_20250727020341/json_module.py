'''
Module to handle JSON file reading and formatting.
'''
import json
import sys  # Added import statement for sys
def read_json(file_path):
    '''
    Reads a JSON file and returns the data as a dictionary.
    Handles exceptions and prints an error message if the file cannot be loaded.
    '''
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to load file: {e}", file=sys.stderr)
        sys.exit(1)
def format_json(json_data):
    '''
    Formats the JSON data into a human-readable, indented string.
    '''
    return json.dumps(json_data, indent=4)