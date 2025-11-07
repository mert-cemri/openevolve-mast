'''
Command Line Interface class to handle user interactions.
'''
class CLI:
    def __init__(self, clipboard_manager):
        self.clipboard_manager = clipboard_manager
    def run(self):
        '''
        Run the CLI loop to accept user commands.
        '''
        print("Welcome to the CLI Clipboard Manager!")
        print("Type 'help' for a list of commands.")
        while True:
            command = input("> ").strip().lower()
            if command == "help":
                self.show_help()
            elif command == "copy":
                self.handle_copy()
            elif command == "paste":
                self.handle_paste()
            elif command == "history":
                self.handle_history()
            elif command == "clear":
                self.handle_clear()
            elif command == "version":
                self.show_version()
            elif command == "exit":
                print("Exiting the CLI Clipboard Manager. Goodbye!")
                break
            else:
                print("Unknown command. Type 'help' for a list of commands.")
    def show_help(self):
        '''
        Display a list of available commands.
        '''
        print("Available commands:")
        print("  copy         - Copy text to the clipboard")
        print("  paste        - Paste text from the clipboard")
        print("  history      - View the history of copied texts")
        print("  clear        - Clear the clipboard and history")
        print("  version      - Show the version of the clipboard manager")
        print("  help         - Show this help message")
        print("  exit         - Exit the application")
    def handle_copy(self):
        '''
        Handle the copy command to copy text to the clipboard.
        '''
        text = input("Enter text to copy: ").strip()
        if not text:
            print("No text entered. Please enter some text to copy.")
            return
        self.clipboard_manager.copy(text)
        print(f"Text copied: {text}")
    def handle_paste(self):
        '''
        Handle the paste command to paste text from the clipboard.
        '''
        text = self.clipboard_manager.paste()
        print(text)
    def handle_history(self):
        '''
        Handle the history command to view the history of copied texts.
        '''
        history = self.clipboard_manager.get_history()
        if history:
            print("Clipboard history:")
            for i, text in enumerate(history, 1):
                print(f"{i}. {text}")
        else:
            print("No history available.")
    def handle_clear(self):
        '''
        Handle the clear command to clear the clipboard and history.
        '''
        print("What would you like to clear?")
        print("  1. Clipboard")
        print("  2. History")
        print("  3. Both")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            self.clipboard_manager.clear(part="clipboard")
            print("Clipboard cleared.")
        elif choice == "2":
            self.clipboard_manager.clear(part="history")
            print("History cleared.")
        elif choice == "3":
            self.clipboard_manager.clear(part="all")
            print("Clipboard and history cleared.")
        else:
            print("Invalid choice. No changes made.")
    def show_version(self):
        '''
        Display the version of the clipboard manager.
        '''
        print(self.clipboard_manager.show_version())