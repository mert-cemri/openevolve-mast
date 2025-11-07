'''
Main entry point for the Maze Generator application.
Initializes and runs the CLI interface.
'''
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()