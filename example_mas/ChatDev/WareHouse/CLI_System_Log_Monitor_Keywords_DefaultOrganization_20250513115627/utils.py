'''
Utility functions for the log monitor application.
'''
def read_keywords(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []