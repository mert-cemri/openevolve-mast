'''
This module contains the function to determine if the length of the intersection of two intervals is a prime number.
'''
def intersection(interval1, interval2):
    """
    You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".
    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    # Calculate the intersection
    start1, end1 = interval1
    start2, end2 = interval2
    # Find the start and end of the intersection
    start_intersection = max(start1, start2)
    end_intersection = min(end1, end2)
    # Calculate the length of the intersection
    if start_intersection <= end_intersection:
        length_of_intersection = end_intersection - start_intersection + 1
    else:
        return "NO"
    # Check if the length is a prime number
    if is_prime(length_of_intersection):
        return "YES"
    else:
        return "NO"
def is_prime(n):
    """
    Check if a number is a prime number.
    """
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