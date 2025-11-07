'''
Handles reading the contents of files.
'''
import sys
class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = self._read_file()
    def _read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} does not exist.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while reading the file {self.file_path}: {e}")
            sys.exit(1)
    def get_content(self):
        return self.content