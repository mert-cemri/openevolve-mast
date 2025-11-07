'''
This module contains a function to split a string into words based on spaces or commas.
'''
def words_string(s):
    """
    Splits a string into words separated by spaces or commas and returns them as a list.
    Parameters:
    s (str): The input string containing words separated by spaces or commas.
    Returns:
    list: A list of words extracted from the input string.
    Examples:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Replace commas with spaces and then split by spaces
    return s.replace(',', ' ').split()