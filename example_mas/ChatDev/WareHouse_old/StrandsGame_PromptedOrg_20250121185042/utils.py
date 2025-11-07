'''
Utility functions for the Strands puzzle game.
'''
def load_strands_from_file(file_path):
    '''
    Loads strands or valid words from a given file to initialize the puzzle.
    :param file_path: Path to the file containing strands or valid words.
    :return: List of strands or valid words.
    '''
    try:
        with open(file_path, 'r') as file:
            items = file.read().splitlines()
        return items
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []