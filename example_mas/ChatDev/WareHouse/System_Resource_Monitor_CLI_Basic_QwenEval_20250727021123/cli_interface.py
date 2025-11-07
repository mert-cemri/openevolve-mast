'''
Module for the CLI interface of the system resource monitor.
'''
class CLIInterface:
    def __init__(self, system_monitor):
        '''
        Initializes the CLI interface with a system monitor instance.
        '''
        self.system_monitor = system_monitor
    def display_resources(self):
        '''
        Displays the current system resource usage in a user-friendly format.
        '''
        cpu_usage = self.system_monitor.get_cpu_usage()
        memory_total, memory_used, memory_free = self.system_monitor.get_memory_usage()
        disk_total, disk_used, disk_free = self.system_monitor.get_disk_usage()
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: Total={memory_total / (1024 ** 3):.2f} GB, Used={memory_used / (1024 ** 3):.2f} GB, Free={memory_free / (1024 ** 3):.2f} GB")
        print(f"Disk Usage: Total={disk_total / (1024 ** 3):.2f} GB, Used={disk_used / (1024 ** 3):.2f} GB, Free={disk_free / (1024 ** 3):.2f} GB")
        print("-" * 40)