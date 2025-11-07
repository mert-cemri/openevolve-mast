'''
Represents the maze data structure.
'''
import random
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        self.generate_maze()
    def generate_maze(self):
        '''
        Generates a maze using a depth-first search algorithm.
        The algorithm starts at the top-left corner and carves out paths by randomly
        selecting unvisited neighbors and removing walls between them.
        '''
        stack = [(1, 1)]
        self.grid[1][1] = ' '
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.width - 1 and 0 < ny < self.height - 1 and self.grid[ny][nx] == '#':
                    self.grid[y + dy // 2][x + dx // 2] = ' '
                    self.grid[ny][nx] = ' '
                    stack.append((nx, ny))
                    break
            else:
                stack.pop()
    def __str__(self):
        return '\n'.join([''.join(row) for row in self.grid])