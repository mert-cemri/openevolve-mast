'''
This module contains the implementation of the choose_num function, which
returns the largest even integer within a given inclusive range [x, y].
If no even number exists within the range, it returns -1.
'''
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.
    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Ensure x is less than or equal to y
    if x > y:
        x, y = y, x
    # Iterate from y to x to find the largest even number
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    # If no even number is found, return -1
    return -1