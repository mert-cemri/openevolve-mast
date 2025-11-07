'''
This module contains the implementation of the circular_shift function which circularly shifts the digits of an integer.
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
    digits = str(x)
    num_digits = len(digits)
    # Calculate effective shift
    effective_shift = shift % num_digits
    # If shift is greater than or equal to number of digits, return reversed digits
    if shift >= num_digits:
        return digits[::-1]
    # Perform circular shift
    if effective_shift > 0:
        shifted_digits = digits[-effective_shift:] + digits[:-effective_shift]
    else:
        shifted_digits = digits
    return shifted_digits