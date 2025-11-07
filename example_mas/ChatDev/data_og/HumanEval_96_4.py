'''
This module implements the function `count_up_to` which returns a list of prime numbers less than a given non-negative integer `n`.
'''
def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_up_to(n):
    """Return a list of prime numbers less than n."""
    return [num for num in range(2, n) if is_prime(num)]
# Example usage:
# print(count_up_to(5))  # Output: [2, 3]
# print(count_up_to(11)) # Output: [2, 3, 5, 7]
# print(count_up_to(0))  # Output: []
# print(count_up_to(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
# print(count_up_to(1))  # Output: []
# print(count_up_to(18)) # Output: [2, 3, 5, 7, 11, 13, 17]