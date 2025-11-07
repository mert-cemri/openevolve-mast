'''
This module contains a function to remove duplicates from a list of integers,
keeping only elements that appear exactly once and maintaining their order.
'''
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Count occurrences of each number
    count = {}
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    # Collect numbers that occur exactly once
    result = [number for number in numbers if count[number] == 1]
    return result