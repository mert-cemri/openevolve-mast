'''
This module contains a function to check if a number is the product of exactly three prime numbers.
'''
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # List of prime numbers less than 100
    primes = [2, 3, 5, 7]
    # Iterate over all combinations of three primes
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False