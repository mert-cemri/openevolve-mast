'''
Main entry point for the PDF text extractor CLI tool.
'''
import sys
from cli_interface import CLIInterface
if __name__ == "__main__":
    cli = CLIInterface(sys.argv[1:])
    cli.run()