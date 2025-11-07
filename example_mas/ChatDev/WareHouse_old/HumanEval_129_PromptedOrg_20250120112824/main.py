'''
Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
each cell of the grid contains a value. Every integer in the range [1, N * N]
inclusive appears exactly once on the cells of the grid.
You have to find the minimum path of length k in the grid. You can start
from any cell, and in each step you can move to any of the neighbor cells,
in other words, you can go to cells which share an edge with you current
cell.
Please note that a path of length k means visiting exactly k cells (not
necessarily distinct).
You CANNOT go off the grid.
A path A (of length k) is considered less than a path B (of length k) if
after making the ordered lists of the values on the cells that A and B go
through (let's call them lst_A and lst_B), lst_A is lexicographically less
than lst_B, in other words, there exist an integer index i (1 <= i <= k)
such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
lst_A[j] = lst_B[j].
It is guaranteed that the answer is unique.
Return an ordered list of the values on the cells that the minimum path go through.
Examples:
    Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
    Output: [1, 2, 1]
    Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
    Output: [1]
'''
def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    memo = {}
    def get_neighbors(x, y):
        # Generate valid neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                yield nx, ny
    def dfs(x, y, path, steps):
        # Base case: if the path length equals k, return the path
        if steps == k:
            return path
        # Check if the result is already computed for the current state
        if (x, y, steps) in memo:
            return memo[(x, y, steps)]
        min_path = None
        # Explore all neighboring cells
        for nx, ny in get_neighbors(x, y):
            new_path = path + [grid[nx][ny]]
            candidate_path = dfs(nx, ny, new_path, steps + 1)
            # Update the minimum path if a better candidate is found
            if min_path is None or candidate_path < min_path:
                min_path = candidate_path
        # Memoize the result for the current state
        memo[(x, y, steps)] = min_path
        return min_path
    min_path = None
    # Try starting from each cell in the grid
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            candidate_path = dfs(i, j, path, 1)
            # Update the minimum path if a better candidate is found
            if min_path is None or candidate_path < min_path:
                min_path = candidate_path
    return min_path