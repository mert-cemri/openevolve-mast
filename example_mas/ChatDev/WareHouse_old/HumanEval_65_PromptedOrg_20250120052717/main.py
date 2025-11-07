'''
This module contains the implementation of the circular_shift function, which performs a circular shift on the digits of an integer.
'''
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to manipulate digits
    x_str = str(x)
    num_digits = len(x_str)
    # If shift is greater than or equal to the number of digits, return the reversed string
    if shift >= num_digits:
        return x_str[::-1]
    # Calculate the effective shift
    effective_shift = shift % num_digits
    # Perform the circular shift using slicing
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    return shifted_str