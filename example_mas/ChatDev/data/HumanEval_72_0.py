'''
This file contains the implementation of the will_it_fly function.
The function checks if an object will fly based on two conditions:
1. The object is balanced (the list is palindromic).
2. The sum of its elements is less than or equal to the maximum possible weight.
'''
def will_it_fly(q, w):
    '''
    Determines if the object q will fly.
    Parameters:
    q (list): A list of integers representing the object.
    w (int): An integer representing the maximum possible weight.
    Returns:
    bool: True if the object will fly, False otherwise.
    '''
    # Check if the list is palindromic
    is_balanced = q == q[::-1]
    # Calculate the sum of the list elements
    total_weight = sum(q)
    # Check if the object will fly
    return is_balanced and total_weight <= w