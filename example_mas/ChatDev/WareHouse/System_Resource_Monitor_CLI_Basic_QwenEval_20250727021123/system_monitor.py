'''
Module for monitoring system resources.
'''
import psutil
class SystemMonitor:
    def __init__(self, partition="/"):
        '''
        Initializes the system monitor with a specified partition.
        Validates the partition path.
        '''
        self.partition = partition
        if not any(part.mountpoint == partition for part in psutil.disk_partitions()):
            raise ValueError(f"Invalid partition path: {self.partition}")
    def get_cpu_usage(self):
        '''
        Returns the CPU usage percentage.
        '''
        return psutil.cpu_percent(interval=1)
    def get_memory_usage(self):
        '''
        Returns the total, used, and free memory in bytes.
        '''
        memory = psutil.virtual_memory()
        return memory.total, memory.used, memory.free
    def get_disk_usage(self):
        '''
        Returns the total, used, and free disk space in bytes for the specified partition.
        '''
        disk = psutil.disk_usage(self.partition)
        return disk.total, disk.used, disk.free