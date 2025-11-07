'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n == 1:
        # For single-digit numbers, only '1' satisfies the condition
        return 1
    # Calculate the number of n-digit numbers starting with '1'
    start_with_one_count = 10**(n-1)
    # Calculate the number of n-digit numbers ending with '1'
    end_with_one_count = 9 * 10**(n-1) // 10
    # Calculate the number of n-digit numbers that both start and end with '1'
    start_and_end_with_one_count = 10**(n-2)
    # Total count is the sum of numbers starting with '1' and ending with '1'
    # minus those that are counted twice (start and end with '1')
    total_count = start_with_one_count + end_with_one_count - start_and_end_with_one_count
    return total_count