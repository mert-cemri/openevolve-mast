'''
From a supplied list of numbers (of length at least two) select and return two that are the closest to each
other and return them in order (smaller number, larger number).
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)
'''
from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers to ensure the closest pair is found in order
    numbers.sort()
    # Initialize variables to store the closest pair and the smallest difference
    closest_pair = (numbers[0], numbers[1])
    smallest_diff = abs(numbers[1] - numbers[0])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        current_diff = abs(numbers[i + 1] - numbers[i])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair