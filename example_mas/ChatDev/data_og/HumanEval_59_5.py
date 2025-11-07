'''
This module contains a function to find the largest prime factor of a given integer.
'''
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime number
    largest_factor = 1
    # Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
    # If n becomes a prime number greater than 2
    if n > 2:
        largest_factor = n
    return largest_factor