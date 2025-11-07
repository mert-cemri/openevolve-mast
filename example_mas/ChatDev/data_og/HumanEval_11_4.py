'''
This module contains a function to perform a binary XOR operation on two strings.
'''
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure the strings are of equal length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")
    # Perform XOR operation
    result = []
    for char_a, char_b in zip(a, b):
        # XOR operation: 1 if the bits are different, 0 if they are the same
        result.append('1' if char_a != char_b else '0')
    return ''.join(result)