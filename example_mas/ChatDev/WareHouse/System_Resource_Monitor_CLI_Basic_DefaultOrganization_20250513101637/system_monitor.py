'''
SystemMonitor class for fetching system resource usage data.
'''
import psutil
class SystemMonitor:
    def get_cpu_usage(self):
        '''Returns the current CPU usage percentage.'''
        return psutil.cpu_percent(interval=1)
    def get_memory_usage(self):
        '''Returns a dictionary with total, used, and free memory.'''
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'used': mem.used,
            'free': mem.available
        }
    def get_disk_usage(self, partition='/'):
        '''Returns a dictionary with total, used, and free disk space for a specified partition.'''
        disk = psutil.disk_usage(partition)
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free
        }