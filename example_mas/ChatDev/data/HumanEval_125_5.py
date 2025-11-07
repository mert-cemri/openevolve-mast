'''
This module contains the implementation of the split_words function.
'''
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace. If no whitespaces exist in the text,
    split on commas ','. If no commas exist, return the number of lowercase letters with odd order in the
    alphabet, where ord('a') = 0, ord('b') = 1, ..., ord('z') = 25.
    Examples:
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") ➞ 3
    '''
    # Check if there are whitespaces in the text
    if ' ' in txt:
        return txt.split()
    # Check if there are commas in the text
    elif ',' in txt:
        return txt.split(',')
    else:
        # Calculate the number of lowercase letters with odd order in the alphabet
        odd_count = 0
        for char in txt:
            if char.islower():
                # Calculate the order of the character
                order = ord(char) - ord('a')
                if order % 2 == 1:
                    odd_count += 1
        return odd_count