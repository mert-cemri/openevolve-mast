'''
This module contains a function to calculate the sum of odd elements at even positions in a list.
'''
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    Args:
    lst (list): A non-empty list of integers.
    Returns:
    int: The sum of all odd elements at even positions in the list.
    Examples:
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    total_sum = 0
    for index in range(0, len(lst), 2):  # Iterate over even indices
        if lst[index] % 2 != 0:  # Check if the element is odd
            total_sum += lst[index]
    return total_sum