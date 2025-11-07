'''
Module to handle the conversion of JSON to CSV.
Includes functions to flatten nested JSON and perform the conversion.
'''
import json
import csv
def flatten_json(y, name='', sep='_', out=None):
    '''
    Flattens a nested JSON object into a flat dictionary.
    Handles nested lists and dictionaries with the same keys by appending a unique identifier.
    '''
    if out is None:
        out = {}
    if isinstance(y, dict):
        for a in y:
            flatten_json(y[a], name + a + sep, sep=sep, out=out)
    elif isinstance(y, list):
        for i, a in enumerate(y):
            flatten_json(a, name + str(i) + sep, sep=sep, out=out)
    else:
        out[name[:-len(sep)]] = y
    return out
def convert_json_to_csv(input_path, output_path, fields=None):
    '''
    Converts a JSON file to a CSV file.
    Handles nested JSON by flattening it.
    Allows user to specify fields to include in the CSV.
    '''
    with open(input_path, 'r') as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        raise ValueError("JSON data must be a list or a dictionary")
    if not data:
        raise ValueError("JSON data is empty")
    flat_data = [flatten_json(item) for item in data]
    if fields:
        headers = fields
        filtered_data = [{field: item.get(field, '') for field in fields} for item in flat_data]
    else:
        headers = flat_data[0].keys() if flat_data else []
        filtered_data = flat_data
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(filtered_data)