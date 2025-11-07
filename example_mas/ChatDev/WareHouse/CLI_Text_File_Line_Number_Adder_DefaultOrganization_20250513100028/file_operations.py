'''
Module for file operations: reading a file, adding line numbers, and writing to a file.
'''
def read_file(file_path):
    '''Reads the content of the specified file.'''
    with open(file_path, 'r') as file:
        return file.readlines()
def add_line_numbers(content):
    '''Adds line numbers to the content of the file.'''
    return ''.join(f"{i+1}: {line}" for i, line in enumerate(content))
def write_to_file(content, output_path):
    '''Writes the modified content to a new file.'''
    with open(output_path, 'w') as file:
        file.write(content)