'''
Main entry point for the text difference tool.
Handles command-line interactions.
'''
import sys
from cli_interface import CLIInterface
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <file1_path> <file2_path>")
        sys.exit(1)
    cli = CLIInterface(sys.argv[1], sys.argv[2])
    cli.run()
if __name__ == "__main__":
    main()