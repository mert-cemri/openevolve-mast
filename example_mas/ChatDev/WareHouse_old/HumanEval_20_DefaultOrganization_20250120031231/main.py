'''
This module contains a function to find the two closest numbers in a list.
Function:
    find_closest_elements(numbers: List[float]) -> Tuple[float, float]
'''
from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    Args:
    numbers (List[float]): A list of floating-point numbers.
    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in ascending order.
    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the numbers to make it easier to find the closest pair
    numbers.sort()
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    closest_pair = (0.0, 0.0)
    # Iterate through the sorted list and find the smallest difference
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair