'''
From a supplied list of numbers (of length at least two), select and return two that are the closest to each other and return them in order (smaller number, larger number).
'''
from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers to make it easier to find the closest pair
    sorted_numbers = sorted(numbers)
    # Initialize the smallest difference as a large number
    smallest_diff = float('inf')
    closest_pair = (0.0, 0.0)
    # Iterate through the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between consecutive numbers
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        # Update the closest pair if a smaller difference is found
        if diff < smallest_diff:
            smallest_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair