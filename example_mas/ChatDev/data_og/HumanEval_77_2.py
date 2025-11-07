'''
This module contains a function to determine if a given integer is a perfect cube.
'''
def iscube(a):
    '''
    Determine if the integer a is a perfect cube of some integer.
    Parameters:
    a (int): The integer to check.
    Returns:
    bool: True if a is a perfect cube, False otherwise.
    '''
    if a == 0:
        return True
    abs_a = abs(a)
    for i in range(int(abs_a**(1/3)) + 2):
        if i**3 == abs_a:
            return True
    return False
# Example usage:
# print(iscube(1))  # True
# print(iscube(2))  # False
# print(iscube(-1)) # True
# print(iscube(64)) # True
# print(iscube(0))  # True
# print(iscube(180))# False