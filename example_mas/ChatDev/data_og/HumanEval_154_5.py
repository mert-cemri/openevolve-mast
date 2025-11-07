'''
This function checks if any rotation of the second word is a substring of the first word.
'''
def cycpattern_check(a, b):
    # Generate all rotations of b
    for i in range(len(b)):
        # Rotate b by slicing
        rotated_b = b[i:] + b[:i]
        # Check if the rotated version is a substring of a
        if rotated_b in a:
            return True
    return False