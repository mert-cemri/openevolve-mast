'''
Main entry point for the Calendar CLI tool.
Handles the command-line arguments and initializes the CalendarCLI class.
'''
import sys
from calendar_cli import CalendarCLI
def main():
    if len(sys.argv) > 1:
        # Run CLI mode
        cli = CalendarCLI()
        try:
            cli.run(sys.argv[1:])
        except ValueError as e:
            print(f"Error: {e}")
            print("Usage: python main.py <month> <year>")
    else:
        print("Usage: python main.py <month> <year>")
if __name__ == "__main__":
    main()