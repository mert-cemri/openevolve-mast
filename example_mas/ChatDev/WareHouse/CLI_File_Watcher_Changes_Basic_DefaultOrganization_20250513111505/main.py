'''
Main entry point for the CLI file watcher application.
'''
import sys
from file_watcher import FileWatcher
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_to_watch>")
        sys.exit(1)
    path = sys.argv[1]
    watcher = FileWatcher(path)
    watcher.start()
if __name__ == "__main__":
    main()