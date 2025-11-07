'''
This module contains a function to check if the length of a given string is a prime number.
'''
def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_length(string):
    """Return True if the length of the string is a prime number, False otherwise."""
    length = len(string)
    return is_prime(length)