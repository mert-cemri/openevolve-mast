'''
This module contains the implementation of the max_fill function which calculates
the number of times buckets need to be lowered to empty all the wells in a grid.
'''
def max_fill(grid, capacity):
    """
    Calculate the number of times buckets need to be lowered to empty all the wells in a grid.
    Parameters:
    grid (list of list of int): A 2D list representing the grid of wells.
    capacity (int): The capacity of each bucket.
    Returns:
    int: The number of times buckets need to be lowered.
    """
    import math
    # Count the total number of water units (1s) in the grid
    total_water_units = sum(sum(row) for row in grid)
    # Calculate the number of times the bucket needs to be lowered
    bucket_lowerings = math.ceil(total_water_units / capacity)
    return bucket_lowerings