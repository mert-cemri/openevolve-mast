'''
This module contains the function can_arrange which determines the largest index
of an element in a list that is not greater than or equal to the element immediately
preceding it. If no such element exists, it returns -1.
'''
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.
    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Iterate over the array from the second element to the end
    for i in range(1, len(arr)):
        # Check if the current element is less than the previous element
        if arr[i] < arr[i - 1]:
            # Return the index of the current element
            return i
    # If no such element is found, return -1
    return -1