'''
This module contains a function to determine if a given integer is a perfect cube of another integer.
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
    if a == 0:
        return True
    abs_a = abs(a)
    cube_root = round(abs_a ** (1/3))
    return cube_root ** 3 == abs_a
# Example usage:
# print(iscube(1))  # True
# print(iscube(2))  # False
# print(iscube(-1)) # True
# print(iscube(64)) # True
# print(iscube(0))  # True
# print(iscube(180))# False