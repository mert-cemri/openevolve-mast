'''
This module contains the implementation of the prime_fib function which returns the n-th Fibonacci number that is also prime.
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
def fibonacci_generator():
    """Generator to yield Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
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
    count = 0
    for fib_num in fibonacci_generator():
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num