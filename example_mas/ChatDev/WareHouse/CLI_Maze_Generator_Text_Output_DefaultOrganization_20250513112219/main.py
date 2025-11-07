'''
This is the main module for running the Maze Generator application as a CLI.
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
        print("Width and height must be integers.")
        return
    generator = MazeGenerator(width, height)
    generator.generate_maze()
    maze = generator.get_maze()
    for line in maze:
        print(line)
if __name__ == "__main__":
    main()