'''
This module contains the function max_fill which calculates the number of times
buckets need to be lowered to empty the wells in a grid.
'''
def max_fill(grid, capacity):
    """
    Calculate the number of times buckets need to be lowered to empty the wells.
    Parameters:
    grid (list of list of int): A rectangular grid of wells where each 1 represents a unit of water.
    capacity (int): The capacity of each bucket.
    Returns:
    int: The number of times buckets need to be lowered.
    """
    total_water_units = 0
    # Count the total number of water units in the grid
    for row in grid:
        total_water_units += sum(row)
    # Calculate the number of bucket operations required
    bucket_operations = total_water_units // capacity
    if total_water_units % capacity != 0:
        bucket_operations += 1
    return bucket_operations