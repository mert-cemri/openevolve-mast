'''
Main entry point for the XML file pretty printer.
'''
import sys
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()