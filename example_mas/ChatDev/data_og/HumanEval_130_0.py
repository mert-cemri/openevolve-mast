'''
This module contains the implementation of the Tribonacci sequence generator.
'''
def tri(n):
    """
    Generates the first n + 1 numbers of the Tribonacci sequence.
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
        return []
    # Base cases
    sequence = [1]  # Assuming tri(0) = 1 for sequence start
    if n >= 1:
        sequence.append(3)  # tri(1) = 3
    if n >= 2:
        sequence.append(2)  # tri(2) = 1 + (2 / 2) = 2
    # Generate the sequence
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
    return sequence
# Example usage
# print(tri(3))  # Output should be [1, 3, 2, 8]