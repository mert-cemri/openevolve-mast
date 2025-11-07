'''
This module contains the implementation of the anti_shuffle function,
which takes a string and returns an ordered version of it. Each word
in the string is replaced by a new word where all the characters are
arranged in ascending order based on ASCII value, while maintaining
the order of words and spaces.
'''
import re
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.
    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Use regular expression to split the string into words and spaces
    parts = re.split(r'(\s+)', s)
    # Sort each word and keep spaces as they are
    sorted_parts = [''.join(sorted(part)) if not part.isspace() else part for part in parts]
    # Join the parts back together
    return ''.join(sorted_parts)