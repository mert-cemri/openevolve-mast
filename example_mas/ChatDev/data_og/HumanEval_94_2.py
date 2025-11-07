'''
This module contains a function to find the largest prime number in a list and return the sum of its digits.
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
def sum_of_digits(n):
    """Return the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))
def skjkasdkd(lst):
    """Find the largest prime number in the list and return the sum of its digits."""
    largest_prime = None
    for number in lst:
        if is_prime(number):
            if largest_prime is None or number > largest_prime:
                largest_prime = number
    if largest_prime is not None:
        return sum_of_digits(largest_prime)
    return 0
# Example usage:
# print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))  # Output: 10