'''
This module contains the implementation of the find_max function which finds the word with the maximum number of unique characters from a list of strings.
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
    # Initialize variables to track the word with the maximum unique characters
    max_unique_count = 0
    result_word = None
    for word in words:
        # Calculate the number of unique characters in the word
        unique_count = len(set(word))
        # Compare with the current maximum and update if necessary
        if unique_count > max_unique_count or (unique_count == max_unique_count and (result_word is None or word < result_word)):
            max_unique_count = unique_count
            result_word = word
    return result_word