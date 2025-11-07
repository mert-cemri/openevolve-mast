'''
Main module to run the CLI file watcher.
'''
import sys
from file_watcher import FileWatcher
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_watch>")
        sys.exit(1)
    path = sys.argv[1]
    file_watcher = FileWatcher(path)
    file_watcher.start()
if __name__ == "__main__":
    main()