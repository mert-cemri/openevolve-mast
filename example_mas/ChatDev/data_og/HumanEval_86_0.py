'''
This module contains the implementation of the anti_shuffle function,
which takes a string and returns an ordered version of it. Each word's
characters are sorted in ascending order based on ASCII values, while
maintaining the original order of words and spaces.
'''
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.
    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the input string by spaces to separate words and spaces
    words = s.split(' ')
    # Sort the characters in each word
    sorted_words = [''.join(sorted(word)) for word in words]
    # Join the sorted words back together with spaces
    return ' '.join(sorted_words)
# Example usage:
# print(anti_shuffle('Hi'))  # Output: 'Hi'
# print(anti_shuffle('hello'))  # Output: 'ehllo'
# print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'