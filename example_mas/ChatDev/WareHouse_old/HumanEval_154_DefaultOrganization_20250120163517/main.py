'''
This module contains the function cycpattern_check which checks if any rotation of the second word is a substring of the first word.
'''
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # Concatenate b with itself
    double_b = b + b
    # Check if any rotation of b is a substring of a
    for i in range(len(b)):
        # Generate the rotation by slicing double_b
        rotation = double_b[i:i+len(b)]
        if rotation in a:
            return True
    return False