'''
This module contains the function hex_key which counts the number of prime hexadecimal digits in a given string.
'''
def hex_key(num):
    """Counts the number of prime hexadecimal digits in the input string.
    Prime hexadecimal digits are: 2, 3, 5, 7, B (11), D (13).
    Args:
        num (str): A string representing a hexadecimal number.
    Returns:
        int: The count of prime hexadecimal digits in the input string.
    """
    # Set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    # Count the number of prime digits in the input string
    count = sum(1 for digit in num if digit in prime_hex_digits)
    return count
# Example usage:
# print(hex_key("AB"))  # Output: 1
# print(hex_key("1077E"))  # Output: 2
# print(hex_key("ABED1A33"))  # Output: 4
# print(hex_key("123456789ABCDEF0"))  # Output: 6
# print(hex_key("2020"))  # Output: 2