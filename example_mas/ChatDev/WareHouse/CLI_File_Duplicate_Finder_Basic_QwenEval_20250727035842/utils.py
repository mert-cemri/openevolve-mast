'''
Module containing utility functions.
'''
import os
def get_file_size(file_path):
    '''Get the size of a file in bytes.'''
    return os.path.getsize(file_path)
def format_size(size):
    '''Format file size in a human-readable format.'''
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"