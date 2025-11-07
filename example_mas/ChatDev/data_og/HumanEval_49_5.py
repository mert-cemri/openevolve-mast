'''
This module contains the implementation of the function `modp` which calculates 2^n modulo p.
'''
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
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
    # Using modular exponentiation to compute (2^n) % p
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply base with result
        if n % 2 == 1:
            result = (result * base) % p
        # n must be even now
        n = n // 2
        base = (base * base) % p
    return result