'''
This module contains a function to find all prime numbers less than a given non-negative integer.
'''
def is_prime(num):
    """
    Determine if a number is prime.
    :param num: Integer to check for primality.
    :return: True if num is prime, False otherwise.
    """
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
    """
    Implement a function that takes a non-negative integer and returns an array of prime numbers less than n.
    :param n: Non-negative integer.
    :return: List of prime numbers less than n.
    """
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes