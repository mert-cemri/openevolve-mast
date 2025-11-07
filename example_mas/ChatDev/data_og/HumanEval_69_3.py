'''
This module contains the implementation of the search function which finds the greatest integer in a list
that has a frequency greater than or equal to its value.
'''
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    from collections import Counter
    # Count the frequency of each integer in the list
    frequency = Counter(lst)
    # Initialize the result as -1
    result = -1
    # Iterate over the frequency dictionary
    for num, freq in frequency.items():
        # Check if the frequency is greater than or equal to the integer value
        if freq >= num:
            # Update the result with the greatest integer satisfying the condition
            result = max(result, num)
    return result