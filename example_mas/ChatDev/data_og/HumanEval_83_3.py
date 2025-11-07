'''
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
'''
def starts_one_ends(n):
    if n == 1:
        # For single-digit numbers, only '1' is valid
        return 1
    # Count numbers starting with '1'
    start_with_one = 10**(n-1)
    # Count numbers ending with '1' (excluding those starting with '1')
    end_with_one = 9 * 10**(n-1) - 10**(n-2)
    # Adjust for overlap (numbers that start and end with '1')
    overlap = 10**(n-2)
    return start_with_one + end_with_one - overlap
# Example usage
if __name__ == "__main__":
    print(starts_one_ends(2))  # Output should be 18