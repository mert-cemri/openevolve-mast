'''
Main entry point for the CSV Unique Values Finder application.
It runs in CLI mode.
'''
import sys
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()