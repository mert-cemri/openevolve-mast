'''
This module contains the implementation of the hex_key function, which counts the number of prime hexadecimal digits in a given string.
'''
def hex_key(num):
    """Counts the number of prime hexadecimal digits in the input string.
    Args:
        num (str): A string representing a hexadecimal number.
    Returns:
        int: The count of prime hexadecimal digits in the input string.
    """
    # Set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    # Count the number of prime digits in the input string
    prime_count = sum(1 for char in num if char in prime_hex_digits)
    return prime_count