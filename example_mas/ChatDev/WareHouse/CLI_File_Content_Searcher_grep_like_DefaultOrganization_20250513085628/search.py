'''
Contains the search function that looks for a given pattern in text files within a directory and its subdirectories.
'''
import os
def search_in_files(directory, pattern):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if pattern in line:
                            results.append((file_path, line.strip()))
    return results