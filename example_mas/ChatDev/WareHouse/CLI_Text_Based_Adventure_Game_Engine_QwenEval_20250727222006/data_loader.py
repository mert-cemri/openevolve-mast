'''
DataLoader class that loads game data from JSON or YAML files.
This class reads the game data from a file and returns it as a Python dictionary.
'''
import json
import yaml
class DataLoader:
    @staticmethod
    def load_game_data(filename):
        with open(filename, 'r') as file:
            if filename.endswith('.json'):
                return json.load(file)
            elif filename.endswith('.yaml') or filename.endswith('.yml'):
                return yaml.safe_load(file)
            else:
                raise ValueError("Unsupported file format. Please use JSON or YAML.")