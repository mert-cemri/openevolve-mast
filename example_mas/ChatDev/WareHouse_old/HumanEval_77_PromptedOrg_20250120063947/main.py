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
    # Handle the case where a is 0
    if a == 0:
        return True
    # Calculate the cube root of the absolute value of a
    abs_a = abs(a)
    cube_root = round(abs_a ** (1/3))
    # Check if the cube of the cube root equals the absolute value of a
    return cube_root ** 3 == abs_a