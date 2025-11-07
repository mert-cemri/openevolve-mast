'''
This module contains the function `move_one_ball` which determines if an array can be sorted in non-decreasing order by performing right shift operations.
'''
def move_one_ball(arr):
    """Determine if the array can be sorted in non-decreasing order by right shifts.
    Args:
        arr (list): A list of unique integers.
    Returns:
        bool: True if the array can be sorted by right shifts, False otherwise.
    """
    if not arr:
        return True
    n = len(arr)
    count_breaks = 0
    break_point = -1
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count_breaks += 1
            break_point = i
    # If there is more than one break point, it cannot be sorted by rotation
    if count_breaks > 1:
        return False
    # If there is no break point, the array is already sorted
    if count_breaks == 0:
        return True
    # Check if the array can be sorted by rotating from the break point
    return arr[break_point + 1:] + arr[:break_point + 1] == sorted(arr)