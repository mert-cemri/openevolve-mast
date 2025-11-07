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
    # Iterate over the array from the second element to the end
    for i in range(len(arr) - 1, 0, -1):
        # Check if the current element is less than the previous element
        if arr[i] < arr[i - 1]:
            return i
    # If no such element is found, return -1
    return -1