'''
This module contains a function to calculate the area of a triangle given the base and height.
'''
def triangle_area(a, h):
    """Given length of a side (base) and height, return area for a triangle.
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    Returns:
    float: The area of the triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h