'''
This module contains the function max_fill which calculates the number of times
buckets need to be lowered to empty the wells in a grid.
The grid is a list of lists where each sublist represents a row of wells, and
each 1 in a row represents a single unit of water. The function takes into account
the capacity of the buckets used to extract water.
Example usage:
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    result = max_fill(grid, capacity)
    print(result)  # Output: 6
'''
def max_fill(grid, capacity):
    # Count the total number of water units in the grid
    total_water_units = sum(sum(row) for row in grid)
    # Calculate the number of times the bucket needs to be lowered
    bucket_lowerings = -(-total_water_units // capacity)  # Using integer division to avoid import
    return bucket_lowerings