'''
Main entry point for the system resource monitoring CLI application.
'''
import time
from system_monitor import SystemMonitor
def display_resources(monitor):
    cpu_usage = monitor.get_cpu_usage()
    memory_total, memory_used, memory_free = monitor.get_memory_usage()
    disk_total, disk_used, disk_free = monitor.get_disk_usage()
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: Total: {memory_total} Used: {memory_used} Free: {memory_free}")
    print(f"Disk Usage: Total: {disk_total} Used: {disk_used} Free: {disk_free}")
def main():
    monitor = SystemMonitor()
    while True:
        display_resources(monitor)
        command = input("Press Enter to update or type 'exit' to quit: ")
        if command.lower() == 'exit':
            break
        time.sleep(5)  # Update every 5 seconds
if __name__ == "__main__":
    main()