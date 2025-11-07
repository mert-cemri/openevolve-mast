'''
This module contains a function to calculate the number of collisions
between two sets of cars moving in opposite directions on an infinite road.
'''
def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.
    This function outputs the number of such collisions.
    Parameters:
    n (int): The number of cars in each set.
    Returns:
    int: The number of collisions.
    """
    # Each car from the left-to-right set will collide with exactly one car from the right-to-left set.
    return n