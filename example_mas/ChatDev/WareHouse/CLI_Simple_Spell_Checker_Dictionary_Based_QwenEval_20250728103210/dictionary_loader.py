'''
DictionaryLoader class to load a dictionary from a file.
'''
import sys
class DictionaryLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    def load_dictionary(self):
        try:
            with open(self.file_path, 'r') as file:
                # Read lines and strip whitespace
                dictionary = [line.strip().lower() for line in file]
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            sys.exit(1)
        except IOError:
            print(f"Error: An error occurred while reading the file {self.file_path}.")
            sys.exit(1)
        return dictionary