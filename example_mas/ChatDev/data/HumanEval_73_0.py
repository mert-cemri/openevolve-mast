'''
This module contains a function to determine the minimum number of changes required
to make an array palindromic.
'''
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.
    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    left = 0
    right = len(arr) - 1
    changes = 0
    # Iterate over the array from both ends towards the center
    while left < right:
        # If elements at the current positions are not equal, increment the change counter
        if arr[left] != arr[right]:
            changes += 1
        # Move towards the center
        left += 1
        right -= 1
    return changes