'''
This module contains a function to calculate the Mean Absolute Deviation (MAD) of a list of numbers.
'''
from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    Args:
    numbers (List[float]): A list of floating-point numbers.
    Returns:
    float: The mean absolute deviation of the numbers.
    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0
    mean_value = sum(numbers) / len(numbers)
    absolute_deviations = [abs(x - mean_value) for x in numbers]
    mad = sum(absolute_deviations) / len(numbers)
    return mad