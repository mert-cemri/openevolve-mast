'''
This file contains utility functions for the Word Count CLI tool.
Specifically, it includes the function to count words in a text file.
'''
import re
def count_words_in_file(file_path):
    '''
    Counts the words in the specified text file.
    Handles basic punctuation and counts sequences of alphanumeric characters as words.
    :param file_path: Path to the text file.
    :return: Total word count.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Use regex to find all sequences of alphanumeric characters
        words = re.findall(r'\b\w+\b', text)
        return len(words)