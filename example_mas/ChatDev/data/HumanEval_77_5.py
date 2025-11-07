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
def iscube(a):
    '''
    Check if the given integer a is a perfect cube.
    '''
    if a < 0:
        # For negative numbers, take the cube root of the absolute value and check
        root = round(abs(a) ** (1/3))
        return root ** 3 == abs(a)
    else:
        # For non-negative numbers, calculate the cube root and check
        root = round(a ** (1/3))
        return root ** 3 == a