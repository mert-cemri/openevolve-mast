'''
Handles the reading and writing of snippets to local files.
'''
import json
class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
    def load_snippets(self):
        '''
        Loads snippets from a local JSON file. Returns an empty list if the file does not exist.
        '''
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.file_path} not found. Creating a new file.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {self.file_path}. Returning an empty list.")
            return []
    def save_snippets(self, snippets):
        '''
        Saves snippets to a local JSON file.
        '''
        try:
            with open(self.file_path, 'w') as file:
                json.dump(snippets, file, indent=4)
        except IOError as e:
            print(f"Error writing to file {self.file_path}: {e}")