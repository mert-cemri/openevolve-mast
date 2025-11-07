'''
The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
This function efficiently computes the n-th element of the fibfib number sequence.
'''
def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # Initialize the base cases
    a, b, c = 0, 0, 1
    # Compute the sequence iteratively
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c
# Example usage
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24