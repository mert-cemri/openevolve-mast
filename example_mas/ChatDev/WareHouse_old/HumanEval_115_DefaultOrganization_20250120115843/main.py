'''
Calculate the number of times buckets need to be lowered to empty the wells.
Parameters:
grid (list of list of int): A rectangular grid where each 1 represents a unit of water.
capacity (int): The capacity of each bucket.
Returns:
int: The total number of times buckets need to be lowered.
'''
def max_fill(grid, capacity):
    total_lowerings = 0
    for row in grid:
        water_units = sum(row)
        total_lowerings += -(-water_units // capacity)  # Using integer division to replace math.ceil
    return total_lowerings