'''
This module contains the implementation of the function `tri(n)` which calculates
the first n + 1 numbers of a custom Tribonacci sequence based on specified rules.
'''
def tri(n):
    """Calculate the first n + 1 numbers of the custom Tribonacci sequence.
    The sequence is defined as follows:
    - tri(1) = 3
    - tri(n) = 1 + n / 2, if n is even
    - tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3), if n is odd
    Args:
        n (int): A non-negative integer representing the number of terms to calculate.
    Returns:
        list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Initialize the sequence with the base case
    sequence = [1]  # tri(0) = 1
    for i in range(1, n + 1):
        if i == 1:
            sequence.append(3)  # tri(1) = 3
        elif i % 2 == 0:
            sequence.append(1 + i // 2)  # tri(n) = 1 + n / 2, if n is even
        else:
            # For odd indices, calculate based on previous terms
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
    return sequence
# Example usage:
# print(tri(3))  # Output should be [1, 3, 2, 8]