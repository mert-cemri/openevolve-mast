'''
This module contains a function to remove vowels from a given string.
'''
def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)