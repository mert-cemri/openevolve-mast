'''
Main entry point for the Log File Analyzer application.
This script initializes the CLI interface.
'''
import sys
from cli_interface import CLIInterface
def main():
    # Run in CLI mode
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()