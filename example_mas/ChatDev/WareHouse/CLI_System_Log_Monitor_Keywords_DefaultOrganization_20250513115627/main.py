'''
Main application file for the CLI system log monitor.
'''
import argparse
import sys
from log_tailer import LogTailer
from utils import read_keywords
def highlight_keywords(line, keywords):
    for keyword in keywords:
        if keyword in line:
            line = line.replace(keyword, f"\033[93m{keyword}\033[0m")  # Highlight in yellow
    return line
def display_line(line, keywords):
    highlighted_line = highlight_keywords(line, keywords)
    print(highlighted_line, end='')
def main():
    parser = argparse.ArgumentParser(description='CLI System Log Monitor')
    parser.add_argument('logfile', type=str, help='Path to the log file to monitor')
    parser.add_argument('--keyword-file', type=str, help='Path to a file containing keywords to highlight')
    parser.add_argument('keywords', type=str, nargs='*', help='Keywords to highlight in the log')
    args = parser.parse_args()
    if args.keyword_file:
        keywords = read_keywords(args.keyword_file)
    else:
        keywords = args.keywords
    if not keywords:
        print("No keywords provided. Exiting.")
        sys.exit(1)
    log_tailer = LogTailer(args.logfile, lambda line: display_line(line, keywords))
    try:
        log_tailer.tail()
    except KeyboardInterrupt:
        log_tailer.stop()
        sys.exit(0)
if __name__ == "__main__":
    main()