'''
Main entry point for the application. It initializes the CLI and GUI interfaces.
'''
import sys
from cli import CLI
from gui import GUI
def main():
    if len(sys.argv) > 1:
        cli = CLI(sys.argv)
        cli.run()
    else:
        gui = GUI()
        gui.run()
if __name__ == "__main__":
    main()