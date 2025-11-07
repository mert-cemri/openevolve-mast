'''
Module for converting JSON files to CSV format.
'''
import json
import csv
from collections import abc
def flatten_json(y, fields_to_flatten=None, list_handling='index'):
    '''
    Flattens a JSON object. Only specified fields are flattened if provided.
    Handles lists based on the specified list_handling method.
    '''
    if fields_to_flatten is None:
        fields_to_flatten = []
    out = {}
    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                if name + a in fields_to_flatten or not fields_to_flatten:
                    flatten(x[a], name + a + '_')
                else:
                    out[name + a] = x[a]
        elif isinstance(x, list):
            if list_handling == 'index':
                for i, a in enumerate(x):
                    flatten(a, name + str(i) + '_')
            elif list_handling == 'concat':
                out[name[:-1]] = ', '.join(map(str, x))
        else:
            out[name[:-1]] = x
    flatten(y)
    return out
def convert_json_to_csv(json_file_path, csv_file_path, fields_to_flatten=None, list_handling='index'):
    '''
    Converts a JSON file to a CSV file, flattening specified fields if provided.
    '''
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    if isinstance(data, list):
        data = [flatten_json(item, fields_to_flatten, list_handling) for item in data]
    else:
        data = [flatten_json(data, fields_to_flatten, list_handling)]
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)