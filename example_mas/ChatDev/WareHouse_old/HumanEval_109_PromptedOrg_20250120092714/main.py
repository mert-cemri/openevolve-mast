'''
This module contains the implementation of the function `move_one_ball` which determines
if an array can be sorted in non-decreasing order by performing any number of right shift operations.
'''
def move_one_ball(arr):
    """Determine if the array can be sorted in non-decreasing order by right shifts.
    Args:
        arr (list): A list of unique integers.
    Returns:
        bool: True if the array can be sorted by right shifts, False otherwise.
    """
    # If the array is empty, return True
    if not arr:
        return True
    n = len(arr)
    # Count the number of break points
    break_count = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            break_count += 1
            if break_count > 1:
                return False
    return True