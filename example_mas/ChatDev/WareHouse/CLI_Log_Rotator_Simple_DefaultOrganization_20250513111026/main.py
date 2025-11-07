'''
Main entry point for the log rotator application. Provides both CLI and GUI interfaces.
'''
import argparse
from log_rotator import LogRotator
from gui import create_gui
def main():
    parser = argparse.ArgumentParser(description='Simple CLI Log Rotator')
    parser.add_argument('--file', type=str, help='Log file to rotate', required=True)
    parser.add_argument('--compress', action='store_true', help='Compress old logs')
    parser.add_argument('--delete', type=int, help='Delete logs older than N days')
    parser.add_argument('--gui', action='store_true', help='Launch GUI')
    args = parser.parse_args()
    if args.gui:
        create_gui()
    else:
        rotator = LogRotator(args.file)
        rotator.rotate_log()
        if args.compress:
            rotator.compress_logs()
        if args.delete is not None:
            rotator.delete_old_logs(args.delete)
if __name__ == '__main__':
    main()