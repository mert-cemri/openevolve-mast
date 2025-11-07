'''
FileHandler class for handling file operations.
'''
import re
class FileHandler:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()
    @staticmethod
    def parse_file(data, delimiter):
        if delimiter == ' ':
            return [re.split(r'\s+', line.strip()) for line in data]
        else:
            return [line.strip().split(delimiter) for line in data]