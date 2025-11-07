'''
This module contains a function to convert a given integer to a specified base and return its string representation.
'''
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    Args:
    x (int): The number to be converted.
    base (int): The base to convert the number to.
    Returns:
    str: The string representation of the number in the specified base.
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x = x // base
    # Reverse the digits since the conversion process gives us the least significant digit first
    digits.reverse()
    return ''.join(digits)