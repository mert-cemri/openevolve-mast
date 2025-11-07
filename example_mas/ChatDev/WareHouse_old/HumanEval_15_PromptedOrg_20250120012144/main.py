'''
This module contains the implementation of the string_sequence function, which returns a string of space-delimited numbers starting from 0 up to a given number n inclusive.
'''
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(i) for i in range(n + 1))