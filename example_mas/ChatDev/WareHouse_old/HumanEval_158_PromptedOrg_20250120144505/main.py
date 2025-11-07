'''
Write a function that accepts a list of strings.
The list contains different words. Return the word with maximum number
of unique characters. If multiple strings have maximum number of unique
characters, return the one which comes first in lexicographical order.
find_max(["name", "of", "string"]) == "string"
find_max(["name", "enam", "game"]) == "enam"
find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
'''
def find_max(words):
    # Initialize variables to keep track of the word with the maximum unique characters
    max_unique_count = 0
    max_word = ""
    for word in words:
        # Calculate the number of unique characters in the current word
        unique_count = len(set(word))
        # Check if the current word has more unique characters or is lexicographically smaller
        if unique_count > max_unique_count or (unique_count == max_unique_count and word < max_word):
            max_unique_count = unique_count
            max_word = word
    return max_word