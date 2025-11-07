'''
Module to load exchange rates from a configuration file.
'''
import json
def load_rates(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)