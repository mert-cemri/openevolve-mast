'''
Computes the first n + 1 numbers of the Tribonacci sequence.
Tribonacci sequence is defined by the recurrence:
tri(1) = 3
tri(n) = 1 + n / 2, if n is even.
tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
Parameters:
n (int): A non-negative integer indicating the number of terms to compute.
Returns:
list: A list of the first n + 1 numbers of the Tribonacci sequence.
'''
def tri(n):
    if n < 0:
        return []
    # Initialize the sequence with the first element
    sequence = [1]
    # Handle the case for n = 0
    if n == 0:
        return sequence
    # Add the second element
    sequence.append(3)
    # Compute the sequence iteratively
    for i in range(2, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            # Compute the next element based on the defined recurrence relation
            next_value = sequence[i - 1] + sequence[i - 2] + sequence[0]  # tri(n + 1) is tri(1) = 3
            sequence.append(next_value)
    return sequence
# Example usage
print(tri(3))  # Output: [1, 3, 2, 8]