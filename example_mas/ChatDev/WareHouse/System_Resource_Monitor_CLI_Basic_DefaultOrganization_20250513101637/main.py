'''
Main entry point for the system resource monitoring CLI application.
'''
import time
import threading
from system_monitor import SystemMonitor
def display_resources(monitor):
    '''Displays the current system resource usage.'''
    cpu_usage = monitor.get_cpu_usage()
    memory_usage = monitor.get_memory_usage()
    disk_usage = monitor.get_disk_usage()
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage['used'] / (1024**3):.2f} GB used / {memory_usage['total'] / (1024**3):.2f} GB total")
    print(f"Disk Usage: {disk_usage['used'] / (1024**3):.2f} GB used / {disk_usage['total'] / (1024**3):.2f} GB total")
    print("-" * 40)
def auto_update(monitor):
    '''Automatically updates the display every few seconds.'''
    while True:
        display_resources(monitor)
        time.sleep(5)
def main():
    '''Runs the CLI tool that updates the system resource usage display every few seconds or on command.'''
    monitor = SystemMonitor()
    threading.Thread(target=auto_update, args=(monitor,), daemon=True).start()
    while True:
        input("Press Enter to refresh immediately...")
        display_resources(monitor)
if __name__ == "__main__":
    main()