'''
This module contains the implementation of the search function which finds the greatest integer in a list
that has a frequency greater than or equal to the integer itself.
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
    # Count the frequency of each number in the list
    frequency = Counter(lst)
    # Initialize the result as -1 (in case no valid number is found)
    result = -1
    # Iterate over the frequency dictionary
    for number, count in frequency.items():
        # Check if the number satisfies the condition
        if count >= number:
            # Update the result with the maximum valid number found
            result = max(result, number)
    return result