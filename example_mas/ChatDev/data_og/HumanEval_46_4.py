'''
This module contains the implementation of the fib4 function, which computes the n-th element of the Fib4 number sequence.
'''
def fib4(n: int) -> int:
    """Compute the n-th element of the Fib4 number sequence.
    The Fib4 sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    Args:
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
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2
    # Initialize the base cases
    fib4_values = [0, 0, 2, 0]
    # Compute the sequence iteratively
    for i in range(4, n + 1):
        next_value = fib4_values[-1] + fib4_values[-2] + fib4_values[-3] + fib4_values[-4]
        fib4_values.append(next_value)
    return fib4_values[n]