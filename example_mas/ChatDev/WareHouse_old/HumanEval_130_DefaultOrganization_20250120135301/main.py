'''
This module contains the implementation of the Tribonacci sequence function `tri(n)`.
The function computes the first n + 1 numbers of the Tribonacci sequence based on the
given recurrence relations.
'''
def tri(n):
    """
    Computes the first n + 1 numbers of the Tribonacci sequence.
    Parameters:
    n (int): A non-negative integer representing the number of terms to compute.
    Returns:
    list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Initialize the sequence with known values
    sequence = [1]  # tri(0) = 1
    if n == 0:
        return sequence
    sequence.append(3)  # tri(1) = 3
    if n == 1:
        return sequence
    sequence.append(2)  # tri(2) = 2
    # Compute the sequence up to n
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
    return sequence
# Example usage:
# print(tri(3))  # Output: [1, 3, 2, 8]