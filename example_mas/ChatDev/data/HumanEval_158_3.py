'''
This module contains a function to find the word with the maximum number of unique characters
from a list of strings. If multiple words have the same number of unique characters, the function
returns the one that comes first in lexicographical order.
'''
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_unique_count = -1
    result_word = ""
    for word in words:
        unique_chars = set(word)
        unique_count = len(unique_chars)
        if unique_count > max_unique_count or (unique_count == max_unique_count and word < result_word):
            max_unique_count = unique_count
            result_word = word
    return result_word