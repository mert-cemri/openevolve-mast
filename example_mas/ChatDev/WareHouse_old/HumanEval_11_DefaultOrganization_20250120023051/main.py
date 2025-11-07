'''
This module contains a function to perform binary XOR on two strings consisting of 1s and 0s.
'''
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")
    # Perform XOR operation
    result = []
    for char_a, char_b in zip(a, b):
        # XOR operation: if both bits are the same, result is '0', else '1'
        result.append('1' if char_a != char_b else '0')
    return ''.join(result)