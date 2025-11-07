'''
Main entry point for the memory usage monitor application.
'''
import sys
from memory_monitor import MemoryMonitor
from cli import CLI
from gui import GUI
def main():
    monitor = MemoryMonitor()
    cli = CLI(monitor)
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        gui = GUI(monitor)
        gui.create_main_window()
    else:
        # Example usage
        cli.display_memory_info()
        cli.display_top_processes(5)
if __name__ == "__main__":
    main()