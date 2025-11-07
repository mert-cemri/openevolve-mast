'''
This is the main file that decides whether to run the CLI or GUI version of the unit converter.
'''
import sys
from cli_converter import CLIConverter
def main():
    if len(sys.argv) > 1:
        cli_converter = CLIConverter()
        cli_converter.run()
    else:
        try:
            import tkinter as tk
            from gui_converter import GUIConverter
            root = tk.Tk()
            gui_converter = GUIConverter(root)
            gui_converter.run()
        except ImportError:
            print("tkinter is not available. Please run the CLI version using the command:")
            print("python main.py <value> <source_unit> <target_unit>")
            print("Example: python main.py 10 kg lb")
if __name__ == "__main__":
    main()