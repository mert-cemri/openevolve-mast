'''
This module contains the implementation of the Tribonacci sequence generator function.
'''
def tri(n):
    """
    Computes the first n + 1 numbers of the Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    Args:
    n (int): A non-negative integer representing the number of terms to compute.
    Returns:
    list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Initialize the sequence with the base case
    sequence = [1]  # Start with tri(0) = 1
    # Compute the sequence up to n
    for i in range(1, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            # Calculate tri(i) using the correct recurrence relation
            if i >= 3:
                sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
            else:
                sequence.append(3)  # tri(1) = 3
    return sequence
# Example usage
# print(tri(3))  # Output should be [1, 3, 2, 8]