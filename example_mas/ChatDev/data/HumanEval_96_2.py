'''
This module contains functions to find prime numbers less than a given number.
Functions:
- is_prime(num): Returns True if num is a prime number, False otherwise.
- count_up_to(n): Returns a list of prime numbers less than n.
'''
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def count_up_to(n):
    """Return a list of prime numbers less than n."""
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes