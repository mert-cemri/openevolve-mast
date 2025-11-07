'''
This module contains the function split_words which processes a string
to split it based on whitespace, commas, or count lowercase letters with odd order in the alphabet.
'''
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exist in the text you
    should split on commas ',' if no commas exist you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Check for whitespace
    if ' ' in txt:
        return txt.split()
    # Check for commas
    if ',' in txt:
        return txt.split(',')
    # Count lowercase letters with odd order in the alphabet
    odd_count = 0
    for char in txt:
        if char.islower():
            order = ord(char) - ord('a')
            if order % 2 == 1:
                odd_count += 1
    return odd_count