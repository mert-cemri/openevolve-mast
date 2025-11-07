'''
Handles the logic for fetching and displaying memory usage using /proc/meminfo and /proc/[pid]/status.
'''
import os
class MemoryMonitor:
    def fetch_system_memory(self):
        '''
        Fetches the total, available, and percentage of system memory usage from /proc/meminfo.
        Returns:
            tuple: A tuple containing total memory, available memory, and memory usage percentage.
        '''
        with open('/proc/meminfo', 'r') as file:
            meminfo = file.readlines()
        meminfo_dict = {}
        for line in meminfo:
            key, value = line.split(':')
            meminfo_dict[key.strip()] = int(value.split()[0])
        total_memory = meminfo_dict['MemTotal']
        available_memory = meminfo_dict['MemAvailable']
        used_memory = total_memory - available_memory
        memory_percent = (used_memory / total_memory) * 100
        return total_memory, available_memory, memory_percent
    def fetch_top_processes(self, num=5):
        '''
        Fetches the top N memory-consuming processes from /proc/[pid]/status.
        Args:
            num (int): The number of top processes to fetch.
        Returns:
            list: A list of tuples containing process ID, process name, and memory usage in bytes.
        '''
        processes = []
        for pid in os.listdir('/proc'):
            if pid.isdigit():
                try:
                    with open(f'/proc/{pid}/status', 'r') as file:
                        status = file.readlines()
                    status_dict = {}
                    for line in status:
                        # Use split(':', 1) to ensure we get at most two parts
                        parts = line.split(':', 1)
                        if len(parts) == 2:
                            key, value = parts
                            status_dict[key.strip()] = value.strip()
                    rss = int(status_dict.get('VmRSS', '0').split()[0]) * 1024  # Convert to bytes
                    processes.append((int(pid), status_dict.get('Name', 'Unknown'), rss))
                except (FileNotFoundError, PermissionError):
                    pass
        processes.sort(key=lambda x: x[2], reverse=True)
        return processes[:num]
    def display_memory_usage(self):
        '''
        Displays the total, available, and percentage of system memory usage.
        '''
        total, available, percent = self.fetch_system_memory()
        print(f"Total Memory: {total / (1024 ** 3):.2f} GB")
        print(f"Available Memory: {available / (1024 ** 3):.2f} GB")
        print(f"Memory Usage: {percent:.2f}%")
    def display_top_processes(self, num=5):
        '''
        Displays the top N memory-consuming processes.
        Args:
            num (int): The number of top processes to display.
        '''
        processes = self.fetch_top_processes(num)
        print("\nTop Memory-Consuming Processes:")
        print(f"{'PID':<10}{'Name':<30}{'Memory (MB)':<15}")
        for pid, name, mem in processes:
            print(f"{pid:<10}{name:<30}{mem / (1024 ** 2):<15.2f}")