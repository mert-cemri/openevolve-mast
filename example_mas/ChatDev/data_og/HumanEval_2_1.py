'''
This module contains the implementation of the truncate_number function,
which returns the decimal part of a given positive floating-point number.
'''
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part