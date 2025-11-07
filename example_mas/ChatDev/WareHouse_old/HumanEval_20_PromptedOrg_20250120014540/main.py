'''
From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).
'''
from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list to ensure closest elements are adjacent
    sorted_numbers = sorted(numbers)
    # Initialize variables to store the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between adjacent numbers
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        # Update the closest pair if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair