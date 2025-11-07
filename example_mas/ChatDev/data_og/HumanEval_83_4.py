'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n <= 0:
        return 0
    # Calculate the range of n-digit numbers
    start = 10**(n-1)
    end = 10**n - 1
    # Count numbers starting with 1
    start_with_1_count = 10**(n-1)
    # Count numbers ending with 1
    end_with_1_count = 10**(n-1)
    # Count numbers both starting and ending with 1
    both_start_and_end_with_1_count = 10**(n-2) if n > 1 else 1
    # Total count
    total_count = start_with_1_count + end_with_1_count - both_start_and_end_with_1_count
    return total_count