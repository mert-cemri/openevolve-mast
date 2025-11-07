'''
Provides functionality to retrieve system resource usage.
'''
import psutil
class SystemMonitor:
    def get_cpu_usage(self):
        '''Returns the current CPU usage percentage.'''
        return psutil.cpu_percent(interval=1)
    def get_memory_usage(self):
        '''Returns a tuple with total, used, and free memory.'''
        memory = psutil.virtual_memory()
        return memory.total, memory.used, memory.free
    def get_disk_usage(self, partition='/'):
        '''Returns a tuple with total, used, and free disk space for a specified partition.'''
        disk = psutil.disk_usage(partition)
        return disk.total, disk.used, disk.free