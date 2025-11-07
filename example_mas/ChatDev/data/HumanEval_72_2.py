'''
This module contains the function will_it_fly which determines if an object will fly based on its balance and weight.
'''
def will_it_fly(q, w):
    '''
    Determines if the object q will fly.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal to the maximum possible weight w.
    Parameters:
    q (list): A list of integers representing the object.
    w (int): An integer representing the maximum possible weight.
    Returns:
    bool: True if the object will fly, False otherwise.
    '''
    # Check if the list is palindromic
    is_balanced = q == q[::-1]
    # Calculate the sum of the list
    total_weight = sum(q)
    # Check if the sum is less than or equal to the maximum weight
    can_fly = total_weight <= w
    # The object will fly if it is balanced and can fly
    return is_balanced and can_fly