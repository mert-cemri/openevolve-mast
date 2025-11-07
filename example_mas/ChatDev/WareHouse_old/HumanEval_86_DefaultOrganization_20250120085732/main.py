'''
This module contains the implementation of the anti_shuffle function
which takes a string and returns an ordered version of it.
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
    # Split the string into words and spaces
    words = s.split(' ')
    # Sort each word individually
    sorted_words = [''.join(sorted(word)) for word in words]
    # Join the sorted words with spaces to reconstruct the original sentence structure
    return ' '.join(sorted_words)
# Example usage
if __name__ == "__main__":
    print(anti_shuffle('Hi'))  # Output: 'Hi'
    print(anti_shuffle('hello'))  # Output: 'ehllo'
    print(anti_shuffle('Hello World!!!'))  # Output: 'Hello !!!Wdlor'