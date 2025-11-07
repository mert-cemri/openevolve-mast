'''
This module contains the function is_happy which checks if a string is "happy".
A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.
'''
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # Check if the string length is less than 3
    if len(s) < 3:
        return False
    # Iterate through the string and check every set of 3 consecutive characters
    for i in range(len(s) - 2):
        # Extract three consecutive characters
        a, b, c = s[i], s[i+1], s[i+2]
        # Check if all three characters are distinct
        if a == b or b == c or a == c:
            return False
    # If all sets of three consecutive characters are distinct, return True
    return True