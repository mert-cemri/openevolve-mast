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
    # Initialize variables to track the word with the maximum unique characters
    max_unique_count = 0
    max_word = None
    for word in words:
        # Calculate the number of unique characters in the word
        unique_chars = set(word)
        unique_count = len(unique_chars)
        # Check if this word has more unique characters or is lexicographically smaller in case of a tie
        if unique_count > max_unique_count or (unique_count == max_unique_count and (max_word is None or word < max_word)):
            max_unique_count = unique_count
            max_word = word
    return max_word
# Example usage
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb" ,"cc"]))   # Output: "aaaaaaa"