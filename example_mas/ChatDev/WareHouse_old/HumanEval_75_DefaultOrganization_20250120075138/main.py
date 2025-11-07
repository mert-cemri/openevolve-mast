'''
This module contains a function to determine if a given number is the product of exactly three distinct prime numbers.
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
    """Returns true if the given number is the multiplication of 3 distinct prime numbers and false otherwise."""
    if a < 2:
        return False
    prime_factors = []
    for i in range(2, a):
        while is_prime(i) and a % i == 0:
            prime_factors.append(i)
            a //= i
        if len(prime_factors) > 3:
            return False
    return len(prime_factors) == 3 and len(set(prime_factors)) == 3
# Example usage:
# print(is_multiply_prime(30))  # Should return True
# print(is_multiply_prime(60))  # Should return False