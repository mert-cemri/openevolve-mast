'''
Main entry point for the Word Count Tool.
Handles the command-line interface operations.
'''
import sys
from cli_app import CLIApp
def main():
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) > 1:
        # Run the CLI application
        cli_app = CLIApp()
        cli_app.run_cli()
    else:
        # Print usage information if no file path is provided
        print("Usage: python main.py <file_path>")
        sys.exit(1)
if __name__ == "__main__":
    main()