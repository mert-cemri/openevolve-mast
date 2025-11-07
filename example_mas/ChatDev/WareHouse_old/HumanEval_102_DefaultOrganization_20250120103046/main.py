'''
This function takes two positive numbers x and y and returns the
biggest even integer number that is in the range [x, y] inclusive. If 
there's no such number, then the function should return -1.
For example:
choose_num(12, 15) = 14
choose_num(13, 12) = -1
'''
def choose_num(x, y):
    # Ensure x is less than or equal to y for a valid range
    if x > y:
        return -1
    # Iterate from the largest possible number in the range down to the smallest
    for num in range(y, x - 1, -1):
        if num % 2 == 0:  # Check if the number is even
            return num
    # If no even number is found, return -1
    return -1