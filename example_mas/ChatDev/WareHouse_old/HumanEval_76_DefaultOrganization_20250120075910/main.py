'''
This module contains a function to determine if a number x is a simple power of n.
'''
def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n, and false otherwise."""
    if x == 1:
        return True
    if n == 1:
        return x == 1
    power = 1
    while power < x:
        power *= n
        if power == x:
            return True
    return False