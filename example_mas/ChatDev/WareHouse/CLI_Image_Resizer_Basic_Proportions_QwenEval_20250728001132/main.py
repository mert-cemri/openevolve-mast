'''
Main entry point for the Image Resizer CLI application.
Handles CLI interactions.
'''
import sys
from cli_handler import CLIHandler
def main():
    if len(sys.argv) > 1:
        cli_handler = CLIHandler(sys.argv)
        cli_handler.run()
    else:
        print("Usage: python main.py <input_path> <output_path> [--width <width> | --height <height>]")
if __name__ == "__main__":
    main()