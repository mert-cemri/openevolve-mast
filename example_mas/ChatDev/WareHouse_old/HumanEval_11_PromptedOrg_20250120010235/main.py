'''
This module contains a function to perform binary XOR operation on two binary strings.
'''
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty result string
    result = ''
    # Iterate over the characters of the input strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation and append the result to the result string
        result += '1' if char_a != char_b else '0'
    return result