'''
This module contains the implementation of the intersection function
which determines if the length of the intersection of two intervals is a prime number.
'''
def is_prime(n):
    """Check if a number is a prime number."""
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
def intersection(interval1, interval2):
    """Determine if the length of the intersection of two intervals is a prime number."""
    start1, end1 = interval1
    start2, end2 = interval2
    # Calculate the intersection
    start_intersection = max(start1, start2)
    end_intersection = min(end1, end2)
    # Check if there is an intersection
    if start_intersection <= end_intersection:
        length_of_intersection = end_intersection - start_intersection + 1
        # Check if the length is a prime number
        if is_prime(length_of_intersection):
            return "YES"
    return "NO"