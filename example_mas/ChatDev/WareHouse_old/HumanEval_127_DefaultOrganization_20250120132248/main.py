'''
This module contains a function to determine if the length of the intersection of two intervals is a prime number.
'''
def intersection(interval1, interval2):
    """
    Determine if the length of the intersection of two intervals is a prime number.
    :param interval1: Tuple[int, int] - The first interval (start, end).
    :param interval2: Tuple[int, int] - The second interval (start, end).
    :return: str - "YES" if the length of the intersection is a prime number, otherwise "NO".
    """
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
    # Calculate the intersection
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    # Calculate the length of the intersection
    if intersection_start <= intersection_end:
        intersection_length = intersection_end - intersection_start + 1
    else:
        intersection_length = 0
    # Determine if the length is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"