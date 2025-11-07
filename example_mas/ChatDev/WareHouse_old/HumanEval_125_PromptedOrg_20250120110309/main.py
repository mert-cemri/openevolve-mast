'''
This file contains the implementation of the split_words function which processes a string
based on the presence of whitespaces, commas, or calculates a specific count of lowercase letters.
'''
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace. If no whitespaces exist in the text,
    split on commas ','. If no commas exist, return the number of lower-case letters with odd order in the
    alphabet, where ord('a') = 0, ord('b') = 1, ... ord('z') = 25.
    Examples:
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
            # Calculate the order of the character
            order = ord(char) - ord('a')
            if order % 2 == 1:  # Check if the order is odd
                odd_count += 1
    return odd_count