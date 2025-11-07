'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n == 1:
        return 1  # Only the number 1 is valid for 1-digit numbers
    # Calculate the number of n-digit numbers starting with 1
    start_with_1 = 10**(n-1)
    # Calculate the number of n-digit numbers ending with 1
    end_with_1 = 10**(n-1)
    # Calculate the overlap where numbers both start and end with 1
    start_and_end_with_1 = 10**(n-2) if n > 2 else 1
    # Total count is the sum of start_with_1 and end_with_1 minus the overlap
    return start_with_1 + end_with_1 - start_and_end_with_1