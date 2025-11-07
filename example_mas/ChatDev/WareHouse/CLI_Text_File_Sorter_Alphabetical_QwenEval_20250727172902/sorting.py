'''
Module containing functions for sorting lines in a text file.
'''
def sort_lines(lines, order="asc"):
    '''
    Sorts lines alphabetically or reverse-alphabetically based on the order parameter.
    '''
    if order == "asc":
        return sorted(lines)
    elif order == "desc":
        return sorted(lines, reverse=True)
    else:
        raise ValueError("Invalid sort order. Use 'asc' or 'desc'.")
def read_file(file_path):
    '''
    Reads lines from a text file.
    '''
    with open(file_path, 'r') as file:
        return file.readlines()
def write_file(file_path, lines):
    '''
    Writes lines to a text file.
    '''
    with open(file_path, 'w') as file:
        file.writelines(lines)