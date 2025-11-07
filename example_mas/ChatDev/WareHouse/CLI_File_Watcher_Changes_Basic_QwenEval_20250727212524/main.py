'''
Main entry point for the CLI file watcher.
This script initializes and runs the CLI or GUI interface based on user input.
'''
import sys
from cli_interface import CLIInterface
from gui_interface import GUIInterface
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <interface> <path>")
        print("Interface options: cli, gui")
        print("Example: python main.py cli /path/to/directory")
        sys.exit(1)
    interface_type = sys.argv[1]
    path = sys.argv[2]
    if interface_type == 'cli':
        cli = CLIInterface(path)
        cli.run()
    elif interface_type == 'gui':
        gui = GUIInterface(path)
        gui.run()
    else:
        print("Invalid interface type. Use 'cli' or 'gui'.")
        sys.exit(1)
if __name__ == "__main__":
    main()