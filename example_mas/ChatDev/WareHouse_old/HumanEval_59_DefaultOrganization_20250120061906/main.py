'''
Return the largest prime factor of n. Assume n > 1 and is not a prime.
'''
def largest_prime_factor(n: int):
    # Start with the smallest prime number
    factor = 2
    # Divide n by factor until it is no longer divisible
    while n % factor == 0:
        n //= factor
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2
    # If n becomes a prime number greater than 2
    if n > 2:
        return n
    # Otherwise, return the last factor found
    return factor