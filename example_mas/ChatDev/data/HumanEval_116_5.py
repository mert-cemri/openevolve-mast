'''
In this Kata, you have to sort an array of non-negative integers according to
number of ones in their binary representation in ascending order.
For similar number of ones, sort based on decimal value.
It must be implemented like this:
>>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
>>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
>>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
'''
def sort_array(arr):
    # Sort the array based on the number of 1's in the binary representation for non-negative integers
    # For negative integers, sort by their absolute values
    return sorted(arr, key=lambda x: (bin(x).count('1'), x) if x >= 0 else (0, x))
# Test cases
print(sort_array([1, 5, 2, 3, 4]))  # Expected: [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # Expected: [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # Expected: [0, 1, 2, 3, 4]