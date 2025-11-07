'''
Main entry point for the application. Initializes and runs the CLI or GUI.
'''
import sys
from cli import CLI
from gui import GUI
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli = CLI()
        cli.run()
    else:
        gui = GUI()
        gui.start()
if __name__ == "__main__":
    main()