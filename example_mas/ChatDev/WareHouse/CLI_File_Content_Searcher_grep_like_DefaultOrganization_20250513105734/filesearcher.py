'''
Module to search for a pattern in text files within a directory.
'''
import os
class FileSearcher:
    def search_files(self, directory, pattern):
        '''
        Searches for the pattern in all text files within the specified directory and its subdirectories.
        Parameters:
            directory (str): The directory to search in.
            pattern (str): The pattern to search for.
        Returns:
            dict: A dictionary where keys are filenames and values are lists of matching lines.
        '''
        results = {}
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        matching_lines = []
                        for line in f:
                            if pattern in line:
                                matching_lines.append(line.strip())
                        if matching_lines:
                            results[file_path] = matching_lines
        return results