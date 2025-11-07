'''
This function takes two positive numbers x and y and returns the biggest even integer number that is in the range [x, y] inclusive. If there's no such number, then the function should return -1.
For example:
choose_num(12, 15) = 14
choose_num(13, 12) = -1
'''
def choose_num(x, y):
    # Determine the range boundaries
    start = min(x, y)
    end = max(x, y)
    # Iterate from the end to the start to find the largest even number
    for num in range(end, start - 1, -1):
        if num % 2 == 0:
            return num
    # If no even number is found, return -1
    return -1