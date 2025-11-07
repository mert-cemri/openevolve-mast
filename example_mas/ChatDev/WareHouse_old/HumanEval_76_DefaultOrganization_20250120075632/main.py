'''
This module contains the function is_simple_power which checks if a number x is a simple power of n.
'''
def is_simple_power(x, n):
    """Returns True if x is a simple power of n, otherwise False."""
    if x == 1:
        return True  # 1 is n**0 for any n
    if n <= 1:
        return False  # n must be greater than 1 to have powers greater than 1
    power = 1
    while power < x:
        power *= n
    return power == x