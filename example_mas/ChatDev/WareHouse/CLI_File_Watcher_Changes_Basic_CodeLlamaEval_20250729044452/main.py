import argparse
import os
import sys
from watcher import FileWatcher
def main():
    parser = argparse.ArgumentParser(description='Monitor a file or directory for changes')
    parser.add_argument('path', help='Path to file or directory to monitor')
    args = parser.parse_args()
    watcher = FileWatcher(args.path)
    watcher.start()
    try:
        while True:
            event = watcher.get_event()
            if event:
                print(f'{event.path} {event.type}')
    except KeyboardInterrupt:
        watcher.stop()
        sys.exit(0)
if __name__ == '__main__':
    main()