'''
This module contains the implementation of the Tribonacci sequence generator function.
'''
def tri(n):
    """
    Generates the first n + 1 numbers of the Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3), if n is odd (corrected formula).
    Parameters:
    n (int): A non-negative integer indicating the number of terms to generate.
    Returns:
    list: A list containing the first n + 1 numbers of the Tribonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Initialize the sequence with the base case
    sequence = [1]  # tri(0) = 1
    if n >= 1:
        sequence.append(3)  # tri(1) = 3
    # Generate the sequence up to n
    for i in range(2, n + 1):
        if i % 2 == 0:
            value = 1 + i // 2
        else:
            # For odd i, use the corrected recursive formula
            if i >= 3:
                value = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
            else:
                # Handle the case where i < 3
                value = sequence[i - 1] + sequence[i - 2]
        sequence.append(value)
    return sequence