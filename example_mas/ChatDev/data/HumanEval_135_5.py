'''
Create a function which returns the largest index of an element which
is not greater than or equal to the element immediately preceding it. If
no such element exists then return -1. The given array will not contain
duplicate values.
Examples:
can_arrange([1,2,4,3,5]) = 3
can_arrange([1,2,3]) = -1
'''
def can_arrange(arr):
    # Initialize the result index to -1
    result_index = -1
    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is less than the previous element
        if arr[i] < arr[i - 1]:
            # Update the result index
            result_index = i
    # Return the result index
    return result_index