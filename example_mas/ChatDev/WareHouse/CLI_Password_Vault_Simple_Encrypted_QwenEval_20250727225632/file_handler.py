'''
This module contains the FileHandler class, which handles reading from and writing to the local file.
'''
class FileHandler:
    def __init__(self, filename='vault.dat'):
        self.filename = filename
    def read_file(self):
        try:
            with open(self.filename, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file {self.filename} does not exist.")
            return None
        except IOError as e:
            print(f"Error reading file {self.filename}: {e}")
            return None
    def write_file(self, data):
        try:
            with open(self.filename, 'wb') as file:
                file.write(data)
        except IOError as e:
            print(f"Error writing to file {self.filename}: {e}")