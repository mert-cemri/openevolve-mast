'''
This module contains the implementation of the find_max function, which
returns the word with the maximum number of unique characters from a list
of strings. If multiple words have the same number of unique characters,
the function returns the one that comes first in lexicographical order.
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
    max_unique_chars = 0
    result_word = None
    for word in words:
        # Calculate the number of unique characters in the current word
        unique_chars = len(set(word))
        # Check if the current word has more unique characters than the previous maximum
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result_word = word
        # If the number of unique characters is the same, choose the lexicographically smaller word
        elif unique_chars == max_unique_chars:
            if result_word is None or word < result_word:
                result_word = word
    return result_word