'''
This module contains the MazeGenerator class, which is responsible for generating a maze using a randomized depth-first search algorithm.
'''
import random
class MazeGenerator:
    def __init__(self, width, height):
        '''
        Initializes the maze generator with the specified dimensions.
        :param width: The width of the maze.
        :param height: The height of the maze.
        '''
        self.width = width
        self.height = height
        self.maze = [['#'] * (2 * width + 1) for _ in range(2 * height + 1)]
    def generate_maze(self):
        '''
        Generates the maze and returns it as a 2D list of characters.
        :return: A 2D list representing the maze.
        '''
        self._carve_passages(1, 1)
        return self.maze
    def _carve_passages(self, cx, cy):
        '''
        Carves passages in the maze using a randomized depth-first search algorithm.
        :param cx: The current x-coordinate in the maze.
        :param cy: The current y-coordinate in the maze.
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 0 < nx < 2 * self.width and 0 < ny < 2 * self.height and self.maze[ny][nx] == '#':
                self.maze[cy + dy][cx + dx] = ' '
                self.maze[ny][nx] = ' '
                self._carve_passages(nx, ny)