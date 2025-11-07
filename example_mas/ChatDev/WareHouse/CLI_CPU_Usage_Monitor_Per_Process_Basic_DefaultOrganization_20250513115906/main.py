'''
Main application file for the CLI CPU usage monitor.
'''
import psutil
import time
import argparse
def get_cpu_usage(pid=None):
    '''Fetches CPU usage for all processes or a specific process if PID is provided.'''
    cpu_usage_data = []
    if pid:
        try:
            proc = psutil.Process(pid)
            # Call cpu_percent twice to get accurate reading
            proc.cpu_percent(interval=None)  # First call to initialize
            cpu_usage_data.append((proc.pid, proc.name(), proc.cpu_percent(interval=0.1)))
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid}")
    else:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                proc.cpu_percent(interval=None)  # First call to initialize
                cpu_usage_data.append((proc.info['pid'], proc.info['name'], proc.cpu_percent(interval=0.1)))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return cpu_usage_data
def display_cpu_usage(cpu_usage_data):
    '''Displays the CPU usage data in a tabular format.'''
    print(f"{'PID':<10}{'Name':<25}{'CPU Usage (%)':<15}")
    print("-" * 50)
    for pid, name, cpu_usage in cpu_usage_data:
        print(f"{pid:<10}{name:<25}{cpu_usage:<15}")
def main():
    '''Main function to parse arguments and initiate the CPU usage monitoring.'''
    parser = argparse.ArgumentParser(description='CLI CPU Usage Monitor')
    parser.add_argument('--pid', type=int, help='Process ID to monitor')
    args = parser.parse_args()
    while True:
        cpu_usage_data = get_cpu_usage(args.pid)
        display_cpu_usage(cpu_usage_data)
        time.sleep(2)  # Update every 2 seconds
if __name__ == '__main__':
    main()