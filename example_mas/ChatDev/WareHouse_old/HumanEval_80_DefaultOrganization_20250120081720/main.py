'''
This module contains the function is_happy which checks if a given string is "happy".
A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.
'''
def is_happy(s):
    """Check if the string is happy.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    Args:
        s (str): The input string to check.
    Returns:
        bool: True if the string is happy, False otherwise.
    """
    # Check if the length of the string is less than 3
    if len(s) < 3:
        return False
    # Iterate through the string and check every set of three consecutive characters
    for i in range(len(s) - 2):
        # Get the current set of three characters
        triplet = s[i:i+3]
        # Check if all characters in the triplet are distinct
        if len(set(triplet)) != 3:
            return False
    # If no non-distinct triplet is found, the string is happy
    return True