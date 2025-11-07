'''
Module for converting JSON to CSV.
'''
import json
import csv
from collections import OrderedDict
def convert_json_to_csv(json_path, csv_path, fields=None, list_handling='concatenate'):
    data = load_json(json_path)
    if fields:
        data = [{field: item.get(field, None) for field in fields} for item in data]
    else:
        data = [flatten_json(item, list_handling) for item in data]
    save_csv(data, csv_path)
def flatten_json(y, list_handling='concatenate'):
    '''
    Flattens a nested JSON object into a flat dictionary.
    Handles nested dictionaries and lists by creating keys with hierarchical names.
    list_handling: Specifies how to handle lists ('concatenate' or 'index').
    '''
    out = {}
    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            if list_handling == 'concatenate':
                out[name[:-1]] = ', '.join(map(str, x))
            elif list_handling == 'index':
                for i, a in enumerate(x):
                    flatten(a, name + str(i) + '_')
        else:
            out[name[:-1]] = x
    flatten(y)
    return out
def load_json(file_path):
    '''
    Loads a JSON file and returns its content.
    '''
    with open(file_path, 'r') as file:
        return json.load(file, object_pairs_hook=OrderedDict)
def save_csv(data, file_path):
    '''
    Saves a list of dictionaries to a CSV file.
    '''
    if not data:
        raise ValueError("No data to save.")
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)