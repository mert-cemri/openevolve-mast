'''
Handles the file renaming logic.
'''
import os
import glob
class FileRenamer:
    def __init__(self, directory):
        if not os.path.exists(directory) or not os.path.isdir(directory):
            raise ValueError(f"The specified directory '{directory}' does not exist or is not a directory.")
        self.directory = directory
        self.files = glob.glob(os.path.join(directory, '*'))
    def add_prefix(self, prefix):
        for file in self.files:
            new_name = os.path.join(self.directory, prefix + os.path.basename(file))
            os.rename(file, new_name)
    def replace_substring(self, old, new):
        for file in self.files:
            new_name = file.replace(old, new)
            os.rename(file, new_name)
    def add_sequential_numbers(self, start=1):
        for i, file in enumerate(self.files, start):
            base, ext = os.path.splitext(os.path.basename(file))
            new_name = os.path.join(self.directory, f"{base}_{i}{ext}")
            os.rename(file, new_name)