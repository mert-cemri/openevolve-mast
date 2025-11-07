'''
Main script to run the disk space analyzer.
Usage: python main.py /path/to/directory
'''
import sys
from disk_analyzer import DiskAnalyzer
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py /path/to/directory")
        sys.exit(1)
    directory = sys.argv[1]
    try:
        analyzer = DiskAnalyzer(directory)
        analyzer.analyze()
        analyzer.print_report()
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
        sys.exit(1)
if __name__ == "__main__":
    main()