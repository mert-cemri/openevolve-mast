'''
This module contains a function to determine if a string is "happy".
A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.
'''
def is_happy(s):
    """Check if the string is happy.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is happy, False otherwise.
    """
    # Check if the string length is less than 3
    if len(s) < 3:
        return False
    # Iterate through the string with a sliding window of size 3
    for i in range(len(s) - 2):
        # Get the current window of 3 characters
        window = s[i:i+3]
        # Check if all characters in the window are distinct
        if len(set(window)) != 3:
            return False
    # If all windows have distinct characters, return True
    return True