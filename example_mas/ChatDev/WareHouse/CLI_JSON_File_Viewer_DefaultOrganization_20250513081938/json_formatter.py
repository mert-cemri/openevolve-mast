'''
json_formatter.py
Reads a JSON file and returns its contents in a formatted, human-readable string.
'''
import json
def format_json_file(file_path):
    '''
    Parameters:
    file_path (str): The path to the JSON file.
    Returns:
    str: The formatted JSON string.
    '''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return json.dumps(data, indent=4)
    except FileNotFoundError:
        raise Exception(f"The file at {file_path} was not found.")
    except json.JSONDecodeError:
        raise Exception("The file is not a valid JSON.")