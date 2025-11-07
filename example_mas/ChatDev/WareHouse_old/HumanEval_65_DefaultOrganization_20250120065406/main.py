'''
This module contains the implementation of the circular_shift function,
which performs a circular shift on the digits of an integer.
'''
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    Args:
    x (int): The integer whose digits are to be shifted.
    shift (int): The number of positions to shift the digits.
    Returns:
    str: The result of the circular shift as a string.
    Examples:
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    # Convert the integer to a string to manipulate digits
    x_str = str(x)
    num_digits = len(x_str)
    # If shift is greater than the number of digits, return reversed digits
    if shift >= num_digits:
        return x_str[::-1]
    # Perform the circular shift
    shift = shift % num_digits  # To handle shifts greater than the number of digits
    shifted_str = x_str[-shift:] + x_str[:-shift]
    return shifted_str