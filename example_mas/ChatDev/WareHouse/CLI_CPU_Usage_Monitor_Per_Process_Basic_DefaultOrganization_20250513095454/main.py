'''
CLI application for monitoring CPU usage per process, similar to a simplified `top` command.
'''
import time
import argparse
from process_monitor import ProcessMonitor
def display_process_info(process_info):
    '''
    Displays the process information in a tabular format.
    '''
    print(f"{'PID':<10}{'Name':<25}{'CPU Usage (%)':<15}")
    print("="*50)
    for pid, name, cpu in process_info:
        print(f"{pid:<10}{name:<25}{cpu:<15}")
def main():
    parser = argparse.ArgumentParser(description="CLI CPU Usage Monitor")
    parser.add_argument('--pid', type=int, help='Focus on a specific process by PID')
    args = parser.parse_args()
    monitor = ProcessMonitor()
    while True:
        if args.pid:
            process_info = monitor.get_process_info_by_pid(args.pid)
            if process_info:
                display_process_info([process_info])
            else:
                print(f"No process found with PID {args.pid}")
        else:
            process_info = monitor.get_process_info()
            display_process_info(process_info)
        time.sleep(2)
if __name__ == "__main__":
    main()