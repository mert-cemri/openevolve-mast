'''
This module contains the implementation of the make_a_pile function.
'''
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if the current number of stones is odd.
        - the next even number if the current number of stones is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    pile = [n]
    current_stones = n
    for _ in range(1, n):
        current_stones += 2
        pile.append(current_stones)
    return pile