'''
This module contains a function to find the largest prime factor of a given number.
'''
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime factor
    factor = 2
    # Divide n by 2 until it is odd
    while n % factor == 0:
        n //= factor
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2
    # If n is still greater than 2, then n itself is a prime number
    if n > 2:
        return n
    else:
        return factor
# Example usage
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2