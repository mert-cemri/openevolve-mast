'''
CLI class to handle command-line interface operations.
'''
class CLI:
    def __init__(self, monitor):
        self.monitor = monitor
    def display_memory_info(self):
        '''Displays overall memory usage.'''
        meminfo = self.monitor.get_memory_info()
        print("Overall Memory Usage:")
        for key, value in meminfo.items():
            print(f"{key}: {value} kB")
    def display_top_processes(self, n=5):
        '''Displays top n memory-consuming processes.'''
        top_processes = self.monitor.get_top_processes(n)
        print(f"Top {n} Memory-Consuming Processes:")
        for pid, mem_usage in top_processes:
            print(f"PID: {pid}, Memory Usage: {mem_usage} kB")