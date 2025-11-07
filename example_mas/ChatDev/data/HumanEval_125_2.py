'''
Given a string of words, return a list of words split on whitespace. If no whitespaces exist in the text, split on commas ','. If no commas exist, return the number of lowercase letters with an odd order in the alphabet, where ord('a') = 0, ord('b') = 1, ..., ord('z') = 25.
Examples:
split_words("Hello world!") ➞ ["Hello", "world!"]
split_words("Hello,world!") ➞ ["Hello", "world!"]
split_words("abcdef") == 3
'''
def split_words(txt):
    # Check if there is any whitespace in the text
    if ' ' in txt:
        return txt.split()
    # Check if there is any comma in the text
    elif ',' in txt:
        return txt.split(',')
    else:
        # Calculate the number of lowercase letters with odd order in the alphabet
        odd_count = sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 1)
        return odd_count
# Example usage
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))        # ➞ 3