'''
Handles loading the exchange rates from a configuration file.
'''
import json
import os
def load_exchange_rates():
    config_file = 'exchange_rates.json'
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    try:
        with open(config_file, 'r') as file:
            exchange_rates = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Configuration file is not a valid JSON.")
    return exchange_rates