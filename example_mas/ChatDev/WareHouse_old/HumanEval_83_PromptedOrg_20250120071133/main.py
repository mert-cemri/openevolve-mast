'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n == 1:
        # For 1-digit numbers, they are 1 to 9, so only 1 starts or ends with 1
        return 1
    # Count numbers starting with 1 (e.g., 100 to 199 for n=3)
    start_with_1 = 10**(n-1)
    # Count numbers ending with 1 (e.g., 101, 111, ..., 991 for n=3)
    end_with_1 = 10**(n-1)
    # Count numbers starting and ending with 1 (e.g., 101, 111, ..., 191 for n=3)
    start_and_end_with_1 = 10**(n-2)
    # Total count is sum of both minus the overlap
    total_count = start_with_1 + end_with_1 - start_and_end_with_1
    return total_count