'''
Handles reading from and writing to the configuration file.
'''
import json
import os
class ConfigFile:
    def __init__(self, file_path):
        self.file_path = file_path
    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
    def exists(self):
        return os.path.exists(self.file_path)