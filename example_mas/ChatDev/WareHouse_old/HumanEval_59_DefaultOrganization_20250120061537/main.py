'''
This module contains the implementation of the function to find the largest prime factor of a given number.
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
    # Divide n by 2 until it is no longer divisible
    while n % factor == 0:
        n //= factor
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2
    # If n is still greater than 1, then it is a prime number
    if n > 1:
        return n
    else:
        return factor - 2