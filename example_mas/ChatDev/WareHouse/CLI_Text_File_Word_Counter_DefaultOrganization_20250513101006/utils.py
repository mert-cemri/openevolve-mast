'''
Utility functions for the Word Count CLI tool.
'''
import re
def count_words_in_file(file_path):
    '''
    Count the number of words in the given file.
    Parameters:
    - file_path: str, path to the text file
    Returns:
    - int, total word count
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Use regex to find all sequences of alphanumeric characters
        words = re.findall(r'\b\w+\b', text)
        return len(words)