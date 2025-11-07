'''
This module contains a function `find_max` that finds the word with the maximum number of unique characters from a list of words.
If multiple words have the same number of unique characters, it returns the one which comes first in lexicographical order.
'''
def find_max(words):
    # Initialize variables to track the word with the maximum unique characters
    max_unique_count = 0
    result_word = None
    for word in words:
        # Calculate the number of unique characters in the current word
        unique_chars = set(word)
        unique_count = len(unique_chars)
        # Check if the current word has more unique characters than the previous maximum
        # or if it has the same number of unique characters but comes first lexicographically
        if unique_count > max_unique_count or (unique_count == max_unique_count and (result_word is None or word < result_word)):
            max_unique_count = unique_count
            result_word = word
    return result_word
# Example usage:
# print(find_max(["name", "of", "string"]))  # Output: "string"
# print(find_max(["name", "enam", "game"]))  # Output: "enam"
# print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"