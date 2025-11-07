'''
Main entry point for the duplicate file finder CLI application.
'''
import sys
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run(sys.argv[1:])
if __name__ == "__main__":
    main()