'''
This module contains the implementation of the max_fill function which calculates
the number of times buckets need to be lowered to empty the wells in a grid.
'''
def max_fill(grid, capacity):
    """
    Calculate the number of times buckets need to be lowered to empty the wells.
    Parameters:
    grid (list of list of int): A rectangular grid where each 1 represents a unit of water.
    capacity (int): The capacity of the bucket.
    Returns:
    int: The number of times the bucket needs to be lowered.
    """
    import math
    # Count the total number of water units in the grid
    total_water_units = sum(sum(row) for row in grid)
    # Calculate the number of times the bucket needs to be lowered
    bucket_lowerings = math.ceil(total_water_units / capacity)
    return bucket_lowerings