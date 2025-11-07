'''
MemoryMonitor class to handle memory monitoring operations.
'''
import os
class MemoryMonitor:
    def get_memory_info(self):
        '''Reads and parses /proc/meminfo to get overall memory usage.'''
        with open('/proc/meminfo', 'r') as file:
            meminfo = file.readlines()
        meminfo_dict = {}
        for line in meminfo:
            key, value = line.split(':')
            meminfo_dict[key.strip()] = int(value.split()[0])
        return meminfo_dict
    def get_top_processes(self, n=5):
        '''Retrieves and sorts processes by memory usage, returning the top n processes.'''
        processes = []
        for pid in os.listdir('/proc'):
            if pid.isdigit():
                try:
                    with open(f'/proc/{pid}/status', 'r') as file:
                        status_info = file.readlines()
                    mem_usage = 0
                    for line in status_info:
                        if line.startswith('VmRSS:'):
                            mem_usage = int(line.split()[1])
                            break
                    processes.append((pid, mem_usage))
                except FileNotFoundError:
                    continue
        processes.sort(key=lambda x: x[1], reverse=True)
        return processes[:n]