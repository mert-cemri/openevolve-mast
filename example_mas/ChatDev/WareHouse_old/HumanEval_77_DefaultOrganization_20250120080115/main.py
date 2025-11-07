'''
This module contains a function to check if a given integer is a perfect cube of another integer.
'''
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Calculate the cube root range
    if a < 0:
        # For negative numbers, check negative roots
        n = int(round(abs(a) ** (1/3)))
        return n**3 == abs(a) or (-n)**3 == a
    else:
        # For non-negative numbers, check positive roots
        n = int(round(a ** (1/3)))
        return n**3 == a