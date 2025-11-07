'''
This module contains the implementation of the modp function, which calculates 2^n modulo p.
'''
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p using exponentiation by squaring.
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
    base = 2
    while n > 0:
        if n % 2 == 1:  # If n is odd, multiply the base with result
            result = (result * base) % p
        base = (base * base) % p  # Square the base
        n //= 2  # Divide n by 2
    return result