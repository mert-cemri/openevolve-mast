'''
This module contains the function will_it_fly which determines if a given list is palindromic and if the sum of its elements is within a specified weight limit.
'''
def will_it_fly(q, w):
    '''
    Determines if the object q will fly based on two conditions:
    1. The list q must be palindromic.
    2. The sum of the elements in q must be less than or equal to the maximum possible weight w.
    Parameters:
    q (list): A list of integers representing the object.
    w (int): An integer representing the maximum possible weight.
    Returns:
    bool: True if the object will fly, False otherwise.
    '''
    # Check if the list is palindromic
    is_palindrome = q == q[::-1]
    # Calculate the sum of the elements
    total_weight = sum(q)
    # Determine if the object will fly
    return is_palindrome and total_weight <= w