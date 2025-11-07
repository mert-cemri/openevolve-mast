'''
This file contains the implementation of the function iscube, which checks if a given integer is a perfect cube of another integer.
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
    # Calculate the cube root of the absolute value of a
    cube_root = round(abs(a) ** (1/3))
    # Check if cubing the cube_root gives the original number a
    return cube_root ** 3 == abs(a)