'''
This module contains the function max_fill which calculates the number of times
buckets need to be lowered to empty the wells represented by a grid.
'''
def max_fill(grid, capacity):
    """
    Calculate the number of times buckets need to be lowered to empty the wells.
    Parameters:
    grid (list of list of int): A rectangular grid where each 1 represents a unit of water.
    capacity (int): The capacity of each bucket.
    Returns:
    int: The number of times buckets need to be lowered.
    """
    total_buckets = 0
    for row in grid:
        water_units = sum(row)  # Count the number of 1s in the row
        total_buckets += -(-water_units // capacity)  # Equivalent to math.ceil(water_units / capacity)
    return total_buckets
# Example usage:
# print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))  # Output: 6
# print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))  # Output: 5
# print(max_fill([[0,0,0], [0,0,0]], 5))  # Output: 0