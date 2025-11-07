'''
Module for calculating directory size and converting it to a human-readable format.
'''
import os
import math
def calculate_directory_size(directory):
    '''
    Recursively calculates the total size of a directory and its subdirectories.
    Parameters:
    directory (str): The path to the directory.
    Returns:
    int: Total size in bytes.
    '''
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if not os.path.islink(filepath):
                total_size += os.path.getsize(filepath)
    return total_size
def convert_size(size_bytes):
    '''
    Converts a size in bytes to a human-readable format (KB, MB, GB, etc.).
    Parameters:
    size_bytes (int): Size in bytes.
    Returns:
    str: Human-readable size.
    '''
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"