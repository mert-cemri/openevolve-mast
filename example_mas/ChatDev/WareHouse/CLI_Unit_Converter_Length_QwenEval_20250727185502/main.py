'''
Main file to run the unit converter application.
It can run in either CLI or GUI mode based on user preference.
'''
from cli_converter import CLIConverter
from gui_converter import GUIConverter
def main():
    mode = input("Choose mode (CLI/GUI): ").strip().lower()
    if mode == 'cli':
        cli_converter = CLIConverter()
        cli_converter.run()
    elif mode == 'gui':
        gui_converter = GUIConverter()
        gui_converter.setup_ui()
    else:
        print("Invalid mode. Please choose 'CLI' or 'GUI'.")
if __name__ == "__main__":
    main()