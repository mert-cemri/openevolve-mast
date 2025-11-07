'''
This file contains the implementation of the strlen function, which returns the length of a given string.
'''
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)