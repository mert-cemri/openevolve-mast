'''
This module contains the implementation of the Tribonacci sequence calculation.
The function `tri(n)` returns a list of the first n + 1 numbers of the Tribonacci sequence.
'''
def tri(n):
    # Initialize the list to store the Tribonacci sequence
    tribonacci_sequence = [1]  # Starting with tri(0) = 1 as per example output
    # Calculate the sequence up to n
    for i in range(1, n + 1):
        if i == 1:
            # Base case tri(1) = 3
            tribonacci_sequence.append(3)
        elif i % 2 == 0:
            # If i is even, use the formula 1 + i / 2
            tribonacci_sequence.append(1 + i // 2)
        else:
            # If i is odd, calculate using the previous values
            # tri(i) = tri(i - 1) + tri(i - 2) + tri(i - 3)
            tri_i = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
            tribonacci_sequence.append(tri_i)
    return tribonacci_sequence
# Example usage:
# print(tri(3))  # Output should be [1, 3, 2, 8]