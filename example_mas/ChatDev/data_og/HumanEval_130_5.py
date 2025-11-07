'''
This module contains the implementation of the Tribonacci sequence generator.
The function `tri(n)` returns the first n + 1 numbers of the Tribonacci sequence.
'''
def tri(n):
    """Generate the first n + 1 numbers of the Tribonacci sequence.
    Args:
        n (int): A non-negative integer representing the number of terms to generate.
    Returns:
        list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Initialize the list with the first three elements of the sequence
    sequence = [1, 3, 2]  # tri(0) = 1, tri(1) = 3, tri(2) = 2
    # Generate the sequence up to n
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)  # tri(n) = 1 + n / 2, if n is even
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])  # tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3), if n is odd
    return sequence[:n + 1]
# Example usage:
# print(tri(3))  # Output: [1, 3, 2, 8]