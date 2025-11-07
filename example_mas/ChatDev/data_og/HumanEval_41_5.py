'''
This module contains the function to calculate the number of collisions
between two sets of cars moving in opposite directions on an infinite line.
'''
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of cars moving in opposite directions.
    Parameters:
    n (int): The number of cars in each set.
    Returns:
    int: The number of collisions.
    """
    # Each car from the left-to-right set will collide with one car from the right-to-left set.
    # Therefore, the number of collisions is equal to the number of cars in one set, which is n.
    return n