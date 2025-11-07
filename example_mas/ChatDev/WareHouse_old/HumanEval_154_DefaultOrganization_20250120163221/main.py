'''
This module contains the function cycpattern_check which checks if any rotation of the second word is a substring of the first word.
'''
def cycpattern_check(a, b):
    # Generate all rotations of the second word
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        # Check if the rotated version is a substring of the first word
        if rotated_b in a:
            return True
    return False