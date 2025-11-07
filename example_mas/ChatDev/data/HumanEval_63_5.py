'''
This module contains the implementation of the FibFib number sequence function.
'''
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
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
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Initialize the base values
    fibfib_values = [0, 0, 1]
    # Compute the sequence up to n
    for i in range(3, n + 1):
        next_value = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3]
        fibfib_values.append(next_value)
    return fibfib_values[n]