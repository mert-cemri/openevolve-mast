'''
ProcessMonitor class for monitoring CPU usage.
Handles the retrieval and display of CPU usage data.
'''
import psutil
import time
import os
class ProcessMonitor:
    def __init__(self, pid=None, interval=1):
        '''
        Initializes the ProcessMonitor with an optional PID and update interval.
        Raises a ValueError if the interval is less than or equal to 0.
        '''
        self.pid = pid
        self.interval = interval
        if self.interval <= 0:
            raise ValueError("Interval must be greater than 0 seconds.")
    def get_cpu_usage(self):
        '''
        Retrieves the CPU usage percentage for the specified process or all processes.
        Returns a dictionary with PID as the key and CPU usage percentage as the value.
        If a specific PID is provided and the process does not exist, returns 'Process not found'.
        Handles edge cases such as processes terminating during monitoring.
        '''
        if self.pid:
            try:
                process = psutil.Process(self.pid)
                return {self.pid: process.cpu_percent(interval=self.interval)}
            except psutil.NoSuchProcess:
                return {self.pid: 'Process not found'}
            except psutil.AccessDenied:
                return {self.pid: 'Access denied'}
        else:
            cpu_usage = {}
            for p in psutil.process_iter(['pid']):
                try:
                    cpu_usage[p.pid] = p.cpu_percent(interval=self.interval)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            return cpu_usage
    def display_cpu_usage(self, cpu_usage):
        '''
        Displays the CPU usage in a tabular format.
        Clears the terminal before displaying the new data.
        '''
        # Clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{'PID':<10}{'CPU Usage (%)':<20}")
        print("-" * 30)
        for pid, usage in cpu_usage.items():
            print(f"{pid:<10}{usage:<20}")
    def run(self):
        '''
        Continuously monitors and displays the CPU usage at the specified interval.
        Exits gracefully on keyboard interrupt.
        '''
        try:
            while True:
                cpu_usage = self.get_cpu_usage()
                self.display_cpu_usage(cpu_usage)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")