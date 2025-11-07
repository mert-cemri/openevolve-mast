'''
Main entry point for the Base64 encoding and decoding CLI tool.
This script initializes and runs the CLI interface.
'''
import sys
from cli_interface import CLIInterface
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <encode|decode> <string>")
        return
    cli = CLIInterface()
    cli.run(sys.argv[1:])
if __name__ == "__main__":
    main()