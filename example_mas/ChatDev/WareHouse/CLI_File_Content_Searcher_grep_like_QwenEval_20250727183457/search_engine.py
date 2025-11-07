'''
Search engine module that handles searching for patterns in text files.
This module provides a function `search_files` that searches for a given pattern in all text files within a specified directory and its subdirectories.
'''
import os
import re
def search_files(directory, pattern):
    '''
    Search for a given pattern in all text files within a specified directory and its subdirectories.
    Args:
        directory (str): The directory to search in.
        pattern (str): The string/pattern to search for.
    Returns:
        dict: A dictionary where keys are file paths and values are lists of matching lines.
    '''
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if is_text_file(file):
                file_path = os.path.join(root, file)
                matching_lines = []
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if re.search(pattern, line):
                                matching_lines.append(line)
                except Exception as e:
                    print(f"Error reading file '{file_path}': {e}")
                if matching_lines:
                    results[file_path] = matching_lines
    return results
def is_text_file(filename):
    '''
    Check if a file is a text file based on its extension.
    Args:
        filename (str): The name of the file to check.
    Returns:
        bool: True if the file is a text file, False otherwise.
    '''
    text_extensions = ['.txt', '.py', '.html', '.css', '.js', '.json', '.xml', '.md']
    return any(filename.endswith(ext) for ext in text_extensions)