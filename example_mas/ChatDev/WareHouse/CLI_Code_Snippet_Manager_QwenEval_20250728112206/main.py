'''
Main entry point for the CLI code snippet manager application.
Handles the initialization and interaction with the CLI interface.
'''
from cli_interface import CLIInterface
def main():
    cli = CLIInterface()
    cli.run()
if __name__ == "__main__":
    main()