'''
This module contains a function to find the largest prime factor of a given integer n.
'''
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime number
    factor = 2
    # Reduce n by dividing it by its smallest factor until it becomes 1
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n