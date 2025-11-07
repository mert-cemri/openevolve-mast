'''
This module contains the implementation of the prime_fib function,
which returns the n-th Fibonacci number that is also a prime number.
'''
def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
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
def fibonacci_generator():
    """
    Generator to yield Fibonacci numbers indefinitely.
    :yield: Next Fibonacci number.
    """
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
def prime_fib(n: int) -> int:
    """
    Return the n-th Fibonacci number that is also prime.
    :param n: The position of the desired prime Fibonacci number.
    :return: The n-th prime Fibonacci number.
    """
    count = 0
    for fib in fibonacci_generator():
        if is_prime(fib):
            count += 1
            if count == n:
                return fib