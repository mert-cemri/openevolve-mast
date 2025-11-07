'''
Functions for file handling: reading and writing files.
'''
def read_file(file_path):
    '''
    Read lines from a text file.
    '''
    with open(file_path, 'r') as file:
        return file.readlines()
def write_file(file_path, lines):
    '''
    Write lines to a text file.
    '''
    with open(file_path, 'w') as file:
        file.writelines(lines)