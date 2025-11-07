'''
This module contains the implementation of the function can_arrange which
returns the largest index of an element in the array that is not greater than
or equal to the element immediately preceding it. If no such element exists,
it returns -1.
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
    # Initialize the variable to store the largest index found
    largest_index = -1
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is less than the preceding element
        if arr[i] < arr[i - 1]:
            # Update the largest index
            largest_index = i
    # Return the largest index found, or -1 if no such index exists
    return largest_index