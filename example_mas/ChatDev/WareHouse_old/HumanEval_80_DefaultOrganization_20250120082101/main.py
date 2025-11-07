'''
This module contains the function is_happy which checks if a given string is "happy".
A string is considered "happy" if its length is at least 3 and every 3 consecutive letters are distinct.
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
    # Iterate over the string with a sliding window of size 3
    for i in range(len(s) - 2):
        # Get the current window of 3 characters
        window = s[i:i+3]
        # Check if all characters in the window are distinct
        if len(set(window)) != 3:
            return False
    # If all windows are distinct, return True
    return True