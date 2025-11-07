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
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    # Initialize the base cases
    fib_values = [0, 0, 2, 0]
    # Compute the sequence iteratively
    for i in range(4, n + 1):
        next_value = fib_values[-1] + fib_values[-2] + fib_values[-3] + fib_values[-4]
        fib_values.append(next_value)
        fib_values.pop(0)  # Maintain only the last four values
    return fib_values[-1]