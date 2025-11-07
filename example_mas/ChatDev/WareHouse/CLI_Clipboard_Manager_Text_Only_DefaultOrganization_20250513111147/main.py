'''
This module sets up the CLI for the clipboard manager application.
'''
import sys
from clipboard_manager import ClipboardManager
def main():
    '''Main function to handle CLI commands for the clipboard manager.'''
    clipboard_manager = ClipboardManager()
    if len(sys.argv) < 2:
        print("Usage: python main.py [copy|paste|history] [text]")
        return
    command = sys.argv[1]
    if command == "copy":
        if len(sys.argv) < 3:
            print("Please provide text to copy.")
            return
        text = " ".join(sys.argv[2:])  # Allow multi-word text to be copied
        clipboard_manager.copy(text)
        print("Text copied to clipboard!")
    elif command == "paste":
        text = clipboard_manager.paste()
        if text:
            print(f"Pasted text: {text}")
        else:
            print("Clipboard is empty.")
    elif command == "history":
        history = clipboard_manager.history()
        if history:
            print("Clipboard History:")
            for item in history:
                print(item)
        else:
            print("Clipboard history is empty.")
    else:
        print("Unknown command. Use 'copy', 'paste', or 'history'.")
if __name__ == "__main__":
    main()