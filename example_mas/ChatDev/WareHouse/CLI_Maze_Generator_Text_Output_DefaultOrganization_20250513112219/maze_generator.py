'''
This module contains the MazeGenerator class which is responsible for generating a maze using the Recursive Backtracking algorithm.
'''
import random
class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['#'] * width for _ in range(height)]
    def generate_maze(self):
        # Start the maze generation from the top-left corner
        self._carve_passage(0, 0)
        # Ensure all cells are visited
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == '#':
                    self._carve_passage(x, y)
    def _carve_passage(self, cx, cy):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == '#':
                self.maze[cy + dy][cx + dx] = ' '
                self.maze[ny][nx] = ' '
                self._carve_passage(nx, ny)
    def get_maze(self):
        return [''.join(row) for row in self.maze]