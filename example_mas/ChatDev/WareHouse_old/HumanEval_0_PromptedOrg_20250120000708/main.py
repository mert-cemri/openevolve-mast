'''
This module contains a function to determine if any two numbers in a list are closer to each other than a specified threshold.
'''
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ 
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The threshold distance to check against.
    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    Examples:
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Sort the numbers to ensure we only need to check adjacent pairs
    numbers.sort()
    # Iterate through the sorted list and check adjacent pairs
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True
    return False