'''
Main application file for the CLI Disk Space Analyzer.
'''
import argparse
from disk_usage_analyzer import DiskUsageAnalyzer
def main():
    parser = argparse.ArgumentParser(description='Disk Space Analyzer CLI')
    parser.add_argument('directory', type=str, help='Directory to analyze')
    args = parser.parse_args()
    try:
        analyzer = DiskUsageAnalyzer(args.directory)
        result = analyzer.get_disk_usage_report()
        print(result)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()