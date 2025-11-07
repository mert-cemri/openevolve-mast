'''
Main file to initialize the CLI and start the log rotator application.
'''
import argparse
from log_rotator import LogRotator
def main():
    parser = argparse.ArgumentParser(description="CLI Log Rotator")
    parser.add_argument("log_file", help="Path to the log file to rotate")
    parser.add_argument("--compress", action="store_true", help="Compress old logs")
    parser.add_argument("--delete-older-than", type=int, help="Delete logs older than N days")
    args = parser.parse_args()
    if args.delete_older_than is not None and args.delete_older_than < 0:
        print("Error: --delete-older-than must be a non-negative integer.")
        return
    log_rotator = LogRotator(args.log_file, args.compress, args.delete_older_than)
    try:
        log_rotator.rotate_logs()
        print("Logs rotated successfully.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()