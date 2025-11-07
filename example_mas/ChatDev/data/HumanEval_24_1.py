'''
This module contains a function to find the largest divisor of a given number that is smaller than the number itself.
'''
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i