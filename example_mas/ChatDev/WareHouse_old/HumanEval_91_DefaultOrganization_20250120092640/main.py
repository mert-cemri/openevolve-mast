'''
This module contains a function to count the number of sentences starting with "I".
'''
import re
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences using regex
    sentences = re.split(r'[.?!]', S)
    # Remove empty strings and trim whitespace
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    # Count sentences starting with "I"
    boredom_count = sum(1 for sentence in sentences if sentence.startswith('I'))
    return boredom_count