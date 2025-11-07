'''
This module contains the implementation of the Tribonacci sequence generator function.
'''
def tri(n):
    """
    Calculate the first n + 1 numbers of the Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    Args:
    n (int): A non-negative integer representing the number of terms to generate.
    Returns:
    list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Base cases
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    # Initialize the sequence with the first two known values
    sequence = [1, 3]
    # Calculate the sequence up to n
    for i in range(2, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
    return sequence
# Example usage:
# print(tri(3))  # Output: [1, 3, 2, 8]