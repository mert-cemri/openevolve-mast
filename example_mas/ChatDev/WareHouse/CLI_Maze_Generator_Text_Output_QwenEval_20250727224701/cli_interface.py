'''
Handles the command-line interface interactions.
'''
import sys
from maze_generator import MazeGenerator
class CLIInterface:
    def run(self):
        try:
            width = int(input("Enter maze width (odd number): "))
            height = int(input("Enter maze height (odd number): "))
            if width % 2 == 0 or height % 2 == 0:
                raise ValueError("Width and height must be odd numbers.")
            generator = MazeGenerator()
            maze = generator.generate(width, height)
            print(maze)
        except ValueError as e:
            print(f"Invalid input: {e}")
            sys.exit(1)