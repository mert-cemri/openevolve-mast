'''
Sort an array of integers based on the number of ones in their binary representation.
For numbers with the same number of ones, sort them by their decimal value.
:param arr: List of integers to be sorted.
:return: A new list of sorted integers.
Examples:
>>> sort_array([1, 5, 2, 3, 4])
[1, 2, 3, 4, 5]
>>> sort_array([-2, -3, -4, -5, -6])
[-6, -5, -4, -3, -2]
>>> sort_array([1, 0, 2, 3, 4])
[0, 1, 2, 3, 4]
'''
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(abs(x)).count('1'), x))