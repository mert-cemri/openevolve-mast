'''
This module contains the function will_it_fly which determines if an object will fly based on its balance and weight.
'''
def will_it_fly(q, w):
    '''
    Determines if the object q will fly.
    Parameters:
    q (list): A list of integers representing the object.
    w (int): The maximum possible weight the object can have to fly.
    Returns:
    bool: True if the object will fly, False otherwise.
    '''
    # Check if the list q is a palindrome
    is_palindrome = q == q[::-1]
    # Calculate the sum of elements in q
    total_weight = sum(q)
    # Check if the object will fly
    return is_palindrome and total_weight <= w