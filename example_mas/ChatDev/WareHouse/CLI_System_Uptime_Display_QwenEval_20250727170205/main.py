'''
Main entry point for the Uptime Display Tool.
Handles user input and initializes CLI interface.
'''
import sys
from uptime_fetcher import UptimeFetcher
from cli_interface import CLIInterface
def main():
    interface = CLIInterface(UptimeFetcher())
    interface.display_uptime()
if __name__ == "__main__":
    main()