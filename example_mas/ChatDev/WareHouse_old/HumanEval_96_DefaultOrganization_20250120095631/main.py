'''
This module contains a function to find all prime numbers less than a given non-negative integer n.
'''
def is_prime(num):
    """Check if a number is a prime number."""
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
    """Implement a function that takes a non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    """
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes