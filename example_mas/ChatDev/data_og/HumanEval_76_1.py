'''
This module contains a function to check if a number is a simple power of another number.
'''
def is_simple_power(x, n):
    """Returns True if x is a simple power of n, otherwise False."""
    if x == 1:
        return True
    if n <= 1:
        return False
    power = 1
    while power < x:
        power *= n
        if power == x:
            return True
    return False
# Example usage:
# print(is_simple_power(1, 4))  # True
# print(is_simple_power(2, 2))  # True
# print(is_simple_power(8, 2))  # True
# print(is_simple_power(3, 2))  # False
# print(is_simple_power(3, 1))  # False
# print(is_simple_power(5, 3))  # False