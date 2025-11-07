'''
This module contains a function to compute 2^n modulo p.
'''
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p using efficient modular exponentiation.
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1
    base = 2 % p  # Initial base is 2
    while n > 0:
        # If n is odd, multiply the base with result
        if n % 2 == 1:
            result = (result * base) % p
        # n must be even now
        n = n // 2
        base = (base * base) % p
    return result