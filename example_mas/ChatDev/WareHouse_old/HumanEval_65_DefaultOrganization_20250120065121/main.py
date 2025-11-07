'''
This module contains the function circular_shift which performs a circular shift on the digits of an integer.
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
    # Convert the integer to a string to manipulate its digits
    digits = str(x)
    num_digits = len(digits)
    # Calculate the effective shift
    effective_shift = shift % num_digits
    # If shift is greater than the number of digits, return the digits reversed
    if shift > num_digits:
        return digits[::-1]
    # If the effective shift is zero, return the original digits
    if effective_shift == 0:
        return digits
    # Perform the circular shift
    shifted_digits = digits[-effective_shift:] + digits[:-effective_shift]
    return shifted_digits