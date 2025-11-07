'''
Handles the logic for generating the maze.
'''
from maze import Maze
class MazeGenerator:
    def generate(self, width, height):
        return Maze(width, height)