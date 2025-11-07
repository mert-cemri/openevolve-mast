'''
This function checks if an array can be sorted in non-decreasing order by performing right shift operations.
'''
def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    break_point = -1
    # Find the point where the order breaks
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break_point = i
            break
    # If no break point is found, the array is already sorted
    if break_point == -1:
        return True
    # Check if rotating from the break point sorts the array
    for i in range(break_point + 1, n - 1):
        if arr[i] > arr[i + 1]:
            return False
    # Check if the last element is less than or equal to the first element
    if arr[-1] > arr[0]:
        return False
    return True
# Example usage:
# print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
# print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False