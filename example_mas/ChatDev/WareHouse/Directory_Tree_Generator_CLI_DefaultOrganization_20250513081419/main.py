'''
Main entry point for the directory tree generator application.
'''
import sys
from tree_cli import TreeCLI
from tree_gui import TreeGUI
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        # Start the CLI application
        cli = TreeCLI()
        cli.run()
    else:
        # Start the GUI application
        gui = TreeGUI()
        gui.start()
if __name__ == "__main__":
    main()