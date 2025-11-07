'''
This module contains the function count_upper which counts the number of uppercase vowels
in even indices of a given string.
'''
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Define the set of uppercase vowels
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}
    # Initialize a counter for uppercase vowels at even indices
    count = 0
    # Iterate over the string with index
    for i in range(0, len(s), 2):  # Only consider even indices
        if s[i] in uppercase_vowels:
            count += 1
    return count