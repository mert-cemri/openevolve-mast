'''
This module contains a function to find the largest divisor of a given number n that is smaller than n.
'''
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisor found, return 1 (which divides any number)