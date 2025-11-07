'''
This module contains a function to sort an array of integers based on the number of ones in their binary representation and then by their decimal value.
'''
def sort_array(arr):
    """
    Sort an array of integers based on the number of ones in their binary representation.
    For numbers with the same number of ones, sort by their decimal value.
    :param arr: List of integers to be sorted.
    :return: Sorted list of integers.
    """
    return sorted(arr, key=lambda x: (bin(abs(x)).count('1'), x))