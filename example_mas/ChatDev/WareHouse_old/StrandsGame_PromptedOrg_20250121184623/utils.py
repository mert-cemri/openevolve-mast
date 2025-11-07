'''
This module provides utility functions for the Strands puzzle application.
'''
def load_strands_from_file(filename):
    '''
    Load strands from a file to initialize the puzzle.
    :param filename: Name of the file containing strands.
    :return: List of strands.
    '''
    try:
        with open(filename, 'r') as file:
            strands = [line.strip() for line in file.readlines()]
        return strands
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure the file exists in the correct directory.")
        return []