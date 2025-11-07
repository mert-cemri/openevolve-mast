'''
Main entry point for the system resource monitor CLI tool.
'''
import time
import argparse
from system_monitor import SystemMonitor
from cli_interface import CLIInterface
def main():
    parser = argparse.ArgumentParser(description="System Resource Monitor CLI Tool")
    parser.add_argument("-i", "--interval", type=int, default=5, help="Update interval in seconds (default: 5)")
    parser.add_argument("-p", "--partition", type=str, default="/", help="Disk partition to monitor (default: /)")
    args = parser.parse_args()
    try:
        system_monitor = SystemMonitor(partition=args.partition)
    except ValueError as e:
        print(f"Error initializing system monitor: {e}")
        return
    cli_interface = CLIInterface(system_monitor)
    try:
        while True:
            cli_interface.display_resources()
            print("Press 'u' to update now or wait for the next interval.")
            user_input = input().strip().lower()
            if user_input == 'u':
                continue
            elif user_input != '':
                print("Invalid input. Please press 'u' to update now or wait for the next interval.")
                continue
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nExiting...")
if __name__ == "__main__":
    main()