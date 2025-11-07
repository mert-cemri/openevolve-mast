'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n == 1:
        # For single-digit numbers, only '1' is valid
        return 1
    # Calculate numbers starting with 1
    start_with_1 = 10**(n-1)
    # Calculate numbers ending with 1
    end_with_1 = 10**(n-1)
    # Calculate numbers starting and ending with 1
    start_and_end_with_1 = 10**(n-2)
    # Total count is sum of both minus the overlap
    return start_with_1 + end_with_1 - start_and_end_with_1