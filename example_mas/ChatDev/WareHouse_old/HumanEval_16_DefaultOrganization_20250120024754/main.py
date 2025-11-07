'''
This module contains a function to count distinct characters in a string, ignoring case.
'''
def count_distinct_characters(string: str) -> int:
    """ 
    Given a string, find out how many distinct characters (regardless of case) it consists of.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    lowercase_string = string.lower()
    # Use a set to find distinct characters
    distinct_characters = set(lowercase_string)
    # Return the number of distinct characters
    return len(distinct_characters)