'''
This module provides a CLI for generating and displaying mazes.
'''
import sys
from maze_generator import MazeGenerator
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <width> <height>")
        return
    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except ValueError:
        print("Invalid input. Please enter integers for width and height.")
        return
    generator = MazeGenerator(width, height)
    maze = generator.generate_maze()
    display_maze(maze)
def display_maze(maze):
    '''
    Displays the generated maze in the console.
    :param maze: The 2D list representing the maze.
    '''
    for row in maze:
        print(''.join(row))
if __name__ == "__main__":
    main()