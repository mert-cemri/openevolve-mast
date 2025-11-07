'''
Main entry point for the memory usage monitor application. Decides whether to run the CLI or GUI version.
'''
import sys
from memory_monitor import MemoryMonitor
from cli import run_cli
from gui import create_gui
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        run_cli()
    else:
        create_gui()
if __name__ == '__main__':
    main()