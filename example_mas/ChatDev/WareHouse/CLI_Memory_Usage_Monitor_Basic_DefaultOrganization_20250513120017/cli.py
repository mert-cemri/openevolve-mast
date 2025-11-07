'''
Handles the command-line interface for the memory usage monitor.
'''
from memory_monitor import MemoryMonitor
def run_cli():
    '''Executes the CLI version of the memory monitor.'''
    monitor = MemoryMonitor()
    memory_info = monitor.get_memory_info()
    print("Overall Memory Usage:")
    for key, value in memory_info.items():
        print(f"{key}: {value}")
    print("\nTop Memory-Consuming Processes:")
    top_processes = monitor.get_top_processes()
    for name, memory in top_processes:
        print(f"{name}: {memory} KB")