'''
Contains the FileRenamer class which handles the logic for renaming files.
'''
import os
class FileRenamer:
    def add_prefix(self, directory, prefix):
        for filename in os.listdir(directory):
            new_name = prefix + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    def replace_substring(self, directory, old_substring, new_substring):
        for filename in os.listdir(directory):
            new_name = filename.replace(old_substring, new_substring)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    def add_sequential_numbers(self, directory, start_number):
        files = os.listdir(directory)
        for i, filename in enumerate(files, start=start_number):
            name, ext = os.path.splitext(filename)
            new_name = f"{name}_{i}{ext}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))