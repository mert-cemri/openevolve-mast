'''
This module contains the function cycpattern_check which checks if any rotation of the second word is a substring of the first word.
'''
def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    # Get the length of the second word
    len_b = len(b)
    # Generate all rotations of b
    for i in range(len_b):
        # Rotate b by slicing
        rotated_b = b[i:] + b[:i]
        # Check if the rotated version is a substring of a
        if rotated_b in a:
            return True
    # If no rotation is a substring, return False
    return False