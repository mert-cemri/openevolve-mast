'''
This module contains the function will_it_fly which determines if an object will fly based on its balance and weight.
'''
def will_it_fly(q, w):
    '''
    Determines if the object q will fly. The object will fly if it is a palindromic list and the sum of its elements is less than or equal to the maximum possible weight w.
    Parameters:
    q (list): A list of integers representing the object.
    w (int): The maximum possible weight.
    Returns:
    bool: True if the object will fly, False otherwise.
    '''
    # Check if the list is a palindrome
    is_palindrome = q == q[::-1]
    # Calculate the sum of the elements
    total_weight = sum(q)
    # Determine if the object will fly
    return is_palindrome and total_weight <= w