'''
This module contains the function max_fill which calculates the number of times
buckets need to be lowered to empty the wells in a grid. Each well is represented
by a row in the grid, and each '1' in a row represents a single unit of water.
The function takes into account the capacity of the bucket used to extract water.
'''
def max_fill(grid, capacity):
    import math
    # Initialize a counter for the total number of water units
    total_water_units = 0
    # Iterate over each row in the grid
    for row in grid:
        # Count the number of 1s in the row and add to the total
        total_water_units += sum(row)
    # Calculate the number of times the bucket needs to be lowered
    # Use math.ceil to ensure any remainder results in an additional lowering
    bucket_lowerings = math.ceil(total_water_units / capacity)
    return bucket_lowerings