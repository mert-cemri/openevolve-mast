'''
This module contains the implementation of the get_odd_collatz function, which generates
the Collatz sequence for a given positive integer n and returns a sorted list of odd numbers
in that sequence.
'''
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in the Collatz sequence.
    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.
    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.
    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    odd_numbers = []
    while n != 1:
        if n % 2 == 1:
            odd_numbers.append(n)
        n = 3 * n + 1 if n % 2 == 1 else n // 2
    odd_numbers.append(1)  # The sequence always ends with 1, which is odd
    return sorted(odd_numbers)