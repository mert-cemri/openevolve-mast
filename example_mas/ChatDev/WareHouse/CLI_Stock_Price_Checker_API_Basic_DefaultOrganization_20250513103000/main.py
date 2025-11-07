'''
Main entry point for the stock price checker application. Handles both CLI and GUI modes.
'''
import argparse
from cli import CLI
from gui import GUI
def main():
    parser = argparse.ArgumentParser(description='Stock Price Checker')
    parser.add_argument('--gui', action='store_true', help='Run the application with a GUI')
    args = parser.parse_args()
    if args.gui:
        gui = GUI()
        gui.run()
    else:
        cli = CLI()
        cli.run()
if __name__ == '__main__':
    main()