'''
Main entry point for the YAML file validator application.
Handles CLI interface.
'''
import sys
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()