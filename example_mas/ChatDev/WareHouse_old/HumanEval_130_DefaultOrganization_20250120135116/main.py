'''
This module contains the implementation of the Tribonacci sequence generator.
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
    # Initialize the sequence with the first term
    sequence = [1]
    # Calculate the sequence up to n
    for i in range(1, n + 1):
        if i == 1:
            sequence.append(3)
        elif i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            # Calculate the next term based on the previous terms
            next_value = sequence[i - 1] + sequence[i - 2] + (1 + (i + 1) // 2 if (i + 1) % 2 == 0 else 3)
            sequence.append(next_value)
    return sequence
# Example usage:
# print(tri(3))  # Output: [1, 3, 2, 8]