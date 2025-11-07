'''
Main module to run the Log Rotator application with a CLI.
'''
import argparse
from log_rotator import LogRotator
def main():
    parser = argparse.ArgumentParser(description='Simple CLI Log Rotator')
    parser.add_argument('--log_file', type=str, default='app.log', help='Log file to rotate')
    parser.add_argument('--compress', action='store_true', help='Compress old logs')
    parser.add_argument('--delete_days', type=int, help='Delete logs older than N days')
    args = parser.parse_args()
    # Initialize the LogRotator
    log_rotator = LogRotator(log_file=args.log_file, compress=args.compress, delete_days=args.delete_days)
    log_rotator.execute()
if __name__ == '__main__':
    main()