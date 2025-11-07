'''
This module contains a function to split a string into words based on spaces or commas.
'''
def words_string(s):
    """
    Splits a string into words separated by commas or spaces and returns a list of words.
    Args:
    s (str): A string of words separated by commas or spaces.
    Returns:
    list: A list of words.
    Examples:
    >>> words_string("Hi, my name is John")
    ['Hi', 'my', 'name', 'is', 'John']
    >>> words_string("One, two, three, four, five, six")
    ['One', 'two', 'three', 'four', 'five', 'six']
    """
    # Replace commas with spaces and then split by spaces
    return s.replace(',', ' ').split()