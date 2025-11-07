'''
Main entry point for the file encryption and decryption utility.
'''
# main.py
import sys
from cli_utility import CLIUtility
from gui_utility import GUIUtility
def main():
    if len(sys.argv) > 1:
        # Run in CLI mode
        cli = CLIUtility()
        cli.run()
    else:
        # Run in GUI mode
        gui = GUIUtility()
        gui.create_gui()
if __name__ == "__main__":
    main()