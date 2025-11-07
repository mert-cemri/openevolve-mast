'''
CLIInterface class for handling command-line input and output.
'''
import sys
from log_analyzer import LogAnalyzer
class CLIInterface:
    def run(self):
        if len(sys.argv) != 3:
            print("Usage: python main.py <log_file> <pattern>")
            sys.exit(1)
        log_file = sys.argv[1]
        pattern = sys.argv[2]
        analyzer = LogAnalyzer(log_file, pattern)
        count = analyzer.count_pattern()
        print(f"Number of lines containing '{pattern}': {count}")