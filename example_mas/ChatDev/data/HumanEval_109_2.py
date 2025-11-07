'''
This module contains the implementation of the function `move_one_ball` which determines
if an array can be sorted in non-decreasing order by performing right shift operations.
'''
def move_one_ball(arr):
    """
    We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 
    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.
    Note: The given list is guaranteed to have unique elements.
    For Example:
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
    """
    if not arr:
        return True
    n = len(arr)
    count_breaks = 0
    break_index = -1
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count_breaks += 1
            break_index = i
    if count_breaks == 0:
        return True
    elif count_breaks == 1:
        # Check if the array can be split into two parts that form a sorted array
        return arr[break_index] <= arr[(break_index + 2) % n]
    else:
        return False