'''
Main entry point for the SSH alias manager application.
Handles the initialization and interaction between the CLI and GUI interfaces.
The application can be run in either CLI or GUI mode based on command-line arguments.
'''
import sys
from cli_interface import CLIInterface
from gui_interface import GUIInterface
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        gui = GUIInterface()
        gui.run()
    else:
        cli = CLIInterface()
        cli.run()
if __name__ == "__main__":
    main()