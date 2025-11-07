'''
Given a string of words, return a list of words split on whitespace, if no whitespaces exist in the text you
should split on commas ',' if no commas exist you should return the number of lower-case letters with odd order in the
alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
Examples:
split_words("Hello world!") ➞ ["Hello", "world!"]
split_words("Hello,world!") ➞ ["Hello", "world!"]
split_words("abcdef") == 3 
'''
def split_words(txt):
    # Check if there are any whitespace characters
    if ' ' in txt:
        return txt.split()
    # Check if there are any commas
    elif ',' in txt:
        return txt.split(',')
    else:
        # Count lowercase letters with odd order in the alphabet
        odd_order_count = sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 1)
        return odd_order_count
# Example usage
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))        # ➞ 3