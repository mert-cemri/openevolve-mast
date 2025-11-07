'''
Main entry point for the CLI file archiver application.
Handles command-line arguments and initializes the CLI.
'''
import sys
import argparse
from cli import CLI
def main():
    cli = CLI()
    cli.run()
if __name__ == '__main__':
    main()