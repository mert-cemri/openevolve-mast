'''
We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N]. The
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
Explanation: By performing 2 right shift operations, non-decreasing order can
             be achieved for the given array.
move_one_ball([3, 5, 4, 1, 2])==>False
Explanation: It is not possible to get non-decreasing order for the given
             array by performing any number of right shift operations.
'''
def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    break_point = -1
    # Find the point where the array is not sorted
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            if break_point != -1:
                return False
            break_point = i
    # If the array is already sorted
    if break_point == -1:
        return True
    # Check if the array can be sorted by shifting from the break point
    for i in range(break_point, n):
        if i < n - 1 and arr[i] > arr[i + 1]:
            return False
    # Check if the last element is less than or equal to the first element of the sorted part
    if arr[n - 1] > arr[0]:
        return False
    return True