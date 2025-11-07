'''
This module contains the function `prime_fib` which returns the n-th number that is both a Fibonacci number and a prime number.
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
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    fib1, fib2 = 1, 1
    count = 0
    while True:
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
        if is_prime(fib):
            count += 1
            if count == n:
                return fib