'''
This module contains the function is_simple_power which checks if a number x is a simple power of n.
'''
def is_simple_power(x, n):
    """Check if x is a simple power of n."""
    if x < 1 or n < 1:
        return False
    if x == 1:
        return True
    while x % n == 0:
        x //= n
    return x == 1