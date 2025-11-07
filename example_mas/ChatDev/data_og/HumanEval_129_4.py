'''
Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
each cell of the grid contains a value. Every integer in the range [1, N * N]
inclusive appears exactly once on the cells of the grid.
You have to find the minimum path of length k in the grid. You can start
from any cell, and in each step you can move to any of the neighbor cells,
in other words, you can go to cells which share an edge with your current
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
'''
def minPath(grid, k):
    def dfs(x, y, path):
        if len(path) == k:
            return path
        path_key = (x, y, tuple(path))
        if path_key in memo:
            return memo[path_key]
        min_path = None
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                new_path = dfs(nx, ny, path + [grid[nx][ny]])
                if min_path is None or new_path < min_path:
                    min_path = new_path
        memo[path_key] = min_path
        return min_path
    memo = {}
    min_path = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = dfs(i, j, [grid[i][j]])
            if min_path is None or path < min_path:
                min_path = path
    return min_path