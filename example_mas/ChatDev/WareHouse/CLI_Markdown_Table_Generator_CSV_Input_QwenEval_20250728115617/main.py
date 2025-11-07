'''
Main entry point for the CLI tool to generate a Markdown table from a CSV file.
'''
import sys
from cli import CLI
def main():
    if len(sys.argv) > 1:
        # Run CLI tool
        cli = CLI()
        cli.run()
    else:
        print("No arguments provided. Please provide a CSV file and an output Markdown file.")
if __name__ == "__main__":
    main()