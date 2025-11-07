'''
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
'''
def generate_integers(a, b):
    # Ensure a is less than or equal to b for consistent range handling
    start, end = min(a, b), max(a, b)
    # Generate even numbers in the range [start, end]
    return [x for x in range(start, end + 1) if x % 2 == 0]