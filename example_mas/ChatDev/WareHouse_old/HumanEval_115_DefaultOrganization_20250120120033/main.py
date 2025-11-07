'''
This module contains the function max_fill which calculates the number of times
buckets need to be lowered to empty the wells represented by a grid.
'''
def max_fill(grid, capacity):
    """
    Calculate the number of times buckets need to be lowered to empty the wells.
    Parameters:
    grid (list of list of int): A 2D list representing the grid of wells.
    capacity (int): The capacity of each bucket.
    Returns:
    int: The number of times buckets need to be lowered.
    """
    total_water_units = 0
    # Count the total number of water units (1s) in the grid
    for row in grid:
        total_water_units += sum(row)
    # Calculate the number of times the bucket needs to be lowered
    # Each lowering can remove 'capacity' units of water
    times_lowered = (total_water_units + capacity - 1) // capacity  # Ceiling division
    return times_lowered