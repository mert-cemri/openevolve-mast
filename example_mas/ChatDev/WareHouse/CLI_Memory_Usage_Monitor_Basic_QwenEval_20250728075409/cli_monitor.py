'''
Handles the command-line interface for the memory usage monitor.
'''
from memory_monitor import MemoryMonitor
class CLIMonitor:
    def __init__(self, top_processes=5):
        '''
        Initializes the CLI monitor.
        Args:
            top_processes (int): The number of top memory-consuming processes to display.
        '''
        self.monitor = MemoryMonitor()
        self.top_processes = top_processes
    def run(self):
        '''
        Runs the CLI memory usage monitor.
        '''
        self.monitor.display_memory_usage()
        self.monitor.display_top_processes(self.top_processes)