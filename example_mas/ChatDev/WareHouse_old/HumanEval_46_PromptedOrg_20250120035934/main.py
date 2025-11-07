'''
This module contains the implementation of the fib4 function, which computes the n-th element of the Fib4 sequence.
'''
def fib4(n: int) -> int:
    """Compute the n-th element of the Fib4 sequence.
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Parameters:
    n (int): The index of the sequence to compute.
    Returns:
    int: The n-th element of the Fib4 sequence.
    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    # Initialize the base cases
    fib4_sequence = [0, 0, 2, 0]
    # Compute the sequence iteratively up to n
    for i in range(4, n + 1):
        next_value = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        fib4_sequence.append(next_value)
    return fib4_sequence[n]
# Example usage
if __name__ == "__main__":
    import doctest
    doctest.testmod()