'''
CLI class to handle command-line interactions.
'''
from clipboard_manager import ClipboardManager
class CLI:
    def __init__(self):
        '''Initialize the CLI with a ClipboardManager instance.'''
        self.clipboard_manager = ClipboardManager()
    def run(self):
        '''Run the main loop to process user commands.'''
        print("Welcome to the CLI Clipboard Manager!")
        print("Commands: copy <text>, paste, history, exit")
        while True:
            command = input("Enter command: ").strip()
            if command.lower() == 'exit':
                print("Exiting the clipboard manager.")
                break
            self.process_command(command)
    def process_command(self, command):
        '''Parse and execute user commands.'''
        if command.startswith('copy '):
            text = command[5:].strip()
            if text:
                self.clipboard_manager.copy(text)
            else:
                print("No text provided to copy.")
        elif command == 'paste':
            self.clipboard_manager.paste()
        elif command == 'history':
            self.clipboard_manager.show_history()
        else:
            print("Unknown command. Please use: copy <text>, paste, history, exit")
if __name__ == "__main__":
    cli = CLI()
    cli.run()