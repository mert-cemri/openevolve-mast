'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 2  # Numbers 1 and 10
    # Count of numbers starting with 1
    start_with_1 = 10**(n-1)
    # Count of numbers ending with 1
    end_with_1 = 10**(n-1)
    # Count of numbers both starting and ending with 1
    start_and_end_with_1 = 10**(n-2)
    # Total count
    total_count = start_with_1 + end_with_1 - start_and_end_with_1
    return total_count