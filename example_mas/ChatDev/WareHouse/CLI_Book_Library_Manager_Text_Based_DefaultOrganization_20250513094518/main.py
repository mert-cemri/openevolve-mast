'''
Main entry point for the CLI book library manager application.
'''
from library_manager import LibraryManager
def main():
    manager = LibraryManager()
    manager.run()
if __name__ == "__main__":
    main()