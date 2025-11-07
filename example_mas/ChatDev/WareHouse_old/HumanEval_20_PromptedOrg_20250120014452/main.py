'''
From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).
'''
from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")
    # Sort the list to make it easier to find the closest elements
    numbers.sort()
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair