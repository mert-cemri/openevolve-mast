'''
Given an array of non-negative integers, return a copy of the given array after sorting.
You will sort the given array in ascending order if the sum of the first index value and last index value is odd,
or sort it in descending order if the sum is even.
Note:
* Don't change the given array.
Examples:
* sort_array([]) => []
* sort_array([5]) => [5]
* sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
* sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
'''
def sort_array(array):
    if len(array) == 0 or len(array) == 1:
        return array.copy()
    sum_first_last = array[0] + array[-1]
    if sum_first_last % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)