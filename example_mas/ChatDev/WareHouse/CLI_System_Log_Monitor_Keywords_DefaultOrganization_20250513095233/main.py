'''
Main application file for the CLI system log monitor.
'''
import argparse
from log_monitor import LogMonitor
def main():
    parser = argparse.ArgumentParser(description='CLI System Log Monitor')
    parser.add_argument('logfile', type=str, help='Path to the log file to monitor')
    parser.add_argument('keywords', type=str, help='Comma-separated list of keywords to highlight')
    args = parser.parse_args()
    keywords = args.keywords.split(',')
    log_monitor = LogMonitor(args.logfile, keywords, lambda line: update_log_display(line, keywords))
    log_monitor.start()
def update_log_display(line, keywords):
    for keyword in keywords:
        line = line.replace(keyword, f'\033[93m{keyword}\033[0m')  # Highlight in yellow
    print(line)
if __name__ == "__main__":
    main()