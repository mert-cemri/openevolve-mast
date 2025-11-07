'''
This module contains the function max_fill which calculates the number of times
buckets need to be lowered to empty the wells in a grid.
'''
def max_fill(grid, capacity):
    total_water_units = 0
    # Count total number of water units (1s) in the grid
    for row in grid:
        total_water_units += sum(row)
    # Calculate the number of times the bucket needs to be lowered
    bucket_uses = (total_water_units + capacity - 1) // capacity
    return bucket_uses