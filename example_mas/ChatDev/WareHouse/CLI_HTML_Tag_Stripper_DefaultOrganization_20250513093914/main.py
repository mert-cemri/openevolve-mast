'''
Main entry point for the HTML stripping application. Decides whether to run in CLI or GUI mode.
'''
import sys
from cli_handler import CLIHandler
from gui_handler import GUIHandler
def main():
    if len(sys.argv) > 1:
        cli = CLIHandler()
        cli.run()
    else:
        gui = GUIHandler()
        gui.run()
if __name__ == "__main__":
    main()