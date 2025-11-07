'''
Main entry point for the QR code generator application.
'''
from cli import CLI
from gui import create_gui
def main():
    # Initialize the CLI
    cli = CLI()
    args = cli.parse_arguments()
    if args.gui:
        # Launch the GUI
        create_gui()
    else:
        # Execute the CLI
        cli.execute()
if __name__ == "__main__":
    main()