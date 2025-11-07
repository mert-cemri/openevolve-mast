'''
Module containing the word count logic.
This module reads the file, processes the text to remove punctuation, and counts the words.
'''
import re
def count_words(file_path, encoding='utf-8'):
    '''
    Counts the number of words in a given text file.
    Args:
        file_path (str): The path to the text file.
        encoding (str): The encoding of the text file.
    Returns:
        int: The total word count.
    '''
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    # Remove punctuation using regex and split the text into words
    words = re.findall(r'\b\w+\b', text)
    return len(words)