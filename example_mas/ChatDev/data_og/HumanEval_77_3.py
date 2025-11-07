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
    # Calculate the cube root of the absolute value of a
    n = round(abs(a) ** (1/3))
    # Check if n^3 equals the absolute value of a
    return n**3 == abs(a)