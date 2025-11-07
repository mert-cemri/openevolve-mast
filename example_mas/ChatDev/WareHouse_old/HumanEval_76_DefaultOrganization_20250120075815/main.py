'''
This module contains the function is_simple_power which checks if a number x is a simple power of n.
'''
def is_simple_power(x, n):
    """Returns true if x is a simple power of n, false otherwise."""
    if n <= 1:
        return x == 1  # Only 1 is a power of 1
    power = 1
    while power < x:
        power *= n
    return power == x
# Example usage:
# print(is_simple_power(1, 4))  # True
# print(is_simple_power(2, 2))  # True
# print(is_simple_power(8, 2))  # True
# print(is_simple_power(3, 2))  # False
# print(is_simple_power(3, 1))  # False
# print(is_simple_power(5, 3))  # False