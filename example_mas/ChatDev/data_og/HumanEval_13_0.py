'''
This file contains the implementation of the greatest_common_divisor function, which calculates the greatest common divisor of two integers using the Euclidean algorithm.
'''
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a