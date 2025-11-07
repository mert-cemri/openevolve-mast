'''
Main entry point for the CPU usage monitor CLI application.
Parses command-line arguments and initializes the ProcessMonitor.
'''
import argparse
from process_monitor import ProcessMonitor
def main():
    parser = argparse.ArgumentParser(description='CLI CPU usage monitor')
    parser.add_argument('--pid', type=int, help='Process ID to focus on')
    parser.add_argument('--interval', type=int, default=1, help='Update interval in seconds (default: 1)')
    args = parser.parse_args()
    monitor = ProcessMonitor(pid=args.pid, interval=args.interval)
    monitor.run()
if __name__ == '__main__':
    main()