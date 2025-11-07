'''
This module contains a function to split a string into words based on commas or spaces.
'''
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Replace commas with spaces
    s = s.replace(',', ' ')
    # Split the string by spaces and filter out any empty strings
    words = s.split()
    return words