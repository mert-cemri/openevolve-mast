'''
This file contains the implementation of the flip_case function, which flips the case of each character in a given string.
'''
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()