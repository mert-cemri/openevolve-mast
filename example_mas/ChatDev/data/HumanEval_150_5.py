'''
This module contains a function `x_or_y` which returns the value of `x` if `n` is a prime number and returns the value of `y` otherwise.
'''
def is_prime(n):
    """Check if a number is prime."""
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
def x_or_y(n, x, y):
    """Return x if n is a prime number, otherwise return y."""
    return x if is_prime(n) else y