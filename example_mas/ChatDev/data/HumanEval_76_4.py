'''
This module contains a function to determine if a number x is a simple power of n.
'''
def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if there exists an integer k such that n**k = x.
    :param x: The number to check.
    :param n: The base number.
    :return: True if x is a simple power of n, False otherwise.
    """
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