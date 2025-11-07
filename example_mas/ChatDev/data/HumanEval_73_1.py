'''
Given an array arr of integers, find the minimum number of elements that
need to be changed to make the array palindromic. A palindromic array is an array that
is read the same backwards and forwards. In one change, you can change one element to any other element.
Assumptions:
- The input is a list of integers.
- The function does not handle non-integer inputs or empty lists.
For example:
smallest_change([1,2,3,5,4,7,9,6]) == 4
smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
smallest_change([1, 2, 3, 2, 1]) == 0
'''
def smallest_change(arr):
    if not arr:
        return 0  # No changes needed for an empty array
    left = 0
    right = len(arr) - 1
    changes = 0
    # Compare elements from the start and end of the array moving towards the center
    while left < right:
        if arr[left] != arr[right]:
            # Increment changes if elements are not equal
            changes += 1
        left += 1
        right -= 1
    return changes