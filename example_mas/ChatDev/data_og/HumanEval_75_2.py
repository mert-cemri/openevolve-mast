'''
This module contains a function to check if a number is the product of exactly three prime numbers.
'''
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers and False otherwise."""
    primes = [i for i in range(2, a) if is_prime(i)]
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False
# Example usage
# print(is_multiply_prime(30))  # Should return True
# print(is_multiply_prime(60))  # Should return False