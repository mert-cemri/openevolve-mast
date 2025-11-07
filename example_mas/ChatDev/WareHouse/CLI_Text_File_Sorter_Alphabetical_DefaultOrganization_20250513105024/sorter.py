'''
This module contains functions for sorting lines in a text file and handling file operations.
'''
def read_file(file_path):
    '''Reads lines from a text file.'''
    with open(file_path, 'r') as file:
        return file.readlines()
def write_file(file_path, lines):
    '''Writes lines to a text file.'''
    with open(file_path, 'w') as file:
        file.writelines(lines)
def sort_lines(input_file, output_file, reverse=False):
    '''Sorts the lines of a file and writes the result to another file.'''
    with open(input_file, 'r') as file:
        lines = file.readlines()
    # Sort lines using Python's built-in sorted function
    sorted_lines = sorted(lines, reverse=reverse)
    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)