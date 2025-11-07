'''
Main entry point for the CLI clipboard manager.
'''
import sys
from clipboard_manager import ClipboardManager
from cli import CLI
def main():
    '''
    Main function to initialize the clipboard manager and CLI, then start the CLI.
    '''
    clipboard_manager = ClipboardManager()
    cli = CLI(clipboard_manager)
    cli.run()
if __name__ == "__main__":
    main()