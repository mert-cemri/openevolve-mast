'''
Main entry point for the File Renamer application.
This script initializes the CLI interface based on user input.
The GUI interface is not included in this version as per the customer's request.
'''
import sys
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()