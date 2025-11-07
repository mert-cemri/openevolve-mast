'''
This file contains the implementation of the fibfib function, which computes the n-th element of the FibFib number sequence.
'''
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Initialize the first three elements of the sequence
    a, b, c = 0, 0, 1
    # Compute the sequence iteratively
    for i in range(3, n + 1):
        next_value = a + b + c
        a, b, c = b, c, next_value
    return c