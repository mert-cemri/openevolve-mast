'''
This module contains the implementation of the Tribonacci sequence function `tri`.
The function calculates the first n + 1 numbers of the Tribonacci sequence based on
the given recurrence relations.
'''
def tri(n):
    # Initialize the list to store Tribonacci numbers
    tribonacci_sequence = [0] * (n + 1)
    # Base cases
    if n >= 0:
        tribonacci_sequence[0] = 1
    if n >= 1:
        tribonacci_sequence[1] = 3
    # Calculate the sequence iteratively
    for i in range(2, n + 1):
        if i % 2 == 0:
            tribonacci_sequence[i] = 1 + i // 2
        else:
            # Ensure tri(n + 1) is calculated correctly
            if i + 1 <= n:
                tribonacci_sequence[i + 1] = 1 + (i + 1) // 2
            tribonacci_sequence[i] = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i + 1]
    # Return the sequence up to n + 1
    return tribonacci_sequence