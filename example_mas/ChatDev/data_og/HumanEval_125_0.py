'''
Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
Examples
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
        odd_count = 0
        for char in txt:
            if char.islower():
                order = ord(char) - ord('a')
                if order % 2 == 1:  # Check if the order is odd
                    odd_count += 1
        return odd_count
# Example usage
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))        # ➞ 3