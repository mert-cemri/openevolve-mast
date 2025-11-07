'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n == 1:
        # For single-digit numbers, only '1' is valid
        return 1
    # Count of numbers starting with 1
    start_with_1 = 10**(n-1)
    # Count of numbers ending with 1
    end_with_1 = (10**n - 1) // 10 - (10**(n-1) - 1) // 10
    # Count of numbers both starting and ending with 1
    both_start_and_end_with_1 = 10**(n-2)
    # Total count is sum of both counts minus the overlap
    total_count = start_with_1 + end_with_1 - both_start_and_end_with_1
    return total_count