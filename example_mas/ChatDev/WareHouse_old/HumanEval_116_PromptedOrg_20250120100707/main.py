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
    # Separate non-negative and negative numbers
    non_negative = [x for x in arr if x >= 0]
    negative = [x for x in arr if x < 0]
    # Sort non-negative numbers based on the number of ones in binary representation
    # and then by their decimal value
    non_negative_sorted = sorted(non_negative, key=lambda x: (bin(x).count('1'), x))
    # Sort negative numbers in ascending order
    negative_sorted = sorted(negative)
    # Combine the sorted negative and non-negative numbers
    return negative_sorted + non_negative_sorted