'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        # For single-digit numbers, only '1' is valid
        return 1
    # Calculate numbers starting with 1
    start_with_1_count = 10**(n-1) - 10**(n-2)
    # Calculate numbers ending with 1
    end_with_1_count = 9 * 10**(n-2)
    # Calculate overlap (numbers that both start and end with 1)
    overlap_count = 10**(n-2)
    # Total count is the sum of both, minus the overlap
    total_count = start_with_1_count + end_with_1_count - overlap_count
    return total_count