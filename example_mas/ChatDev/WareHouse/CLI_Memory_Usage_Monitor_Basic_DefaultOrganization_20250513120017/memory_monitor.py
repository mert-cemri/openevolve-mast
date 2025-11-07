'''
Handles fetching and processing of memory data from the system.
'''
import os
class MemoryMonitor:
    def get_memory_info(self):
        '''Fetches overall system memory usage.'''
        with open('/proc/meminfo', 'r') as file:
            meminfo = file.readlines()
        memory_data = {}
        for line in meminfo:
            parts = line.split(':')
            memory_data[parts[0]] = parts[1].strip()
        return memory_data
    def get_top_processes(self, limit=5):
        '''Lists top memory-consuming processes.'''
        processes = []
        for pid in os.listdir('/proc'):
            if pid.isdigit():
                try:
                    with open(f'/proc/{pid}/status', 'r') as file:
                        status_info = file.readlines()
                    process_info = {line.split(':')[0]: line.split(':')[1].strip() for line in status_info}
                    if 'VmRSS' in process_info:
                        try:
                            memory_usage = int(process_info['VmRSS'].split()[0])
                            processes.append((process_info['Name'], memory_usage))
                        except (ValueError, IndexError):
                            continue
                except (FileNotFoundError, KeyError):
                    continue
        processes.sort(key=lambda x: x[1], reverse=True)
        return processes[:limit]