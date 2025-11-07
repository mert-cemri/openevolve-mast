'''
Main entry point for the memory usage monitor tool.
Handles command-line arguments and runs the CLI version.
'''
import argparse
from cli_monitor import CLIMonitor
def main():
    parser = argparse.ArgumentParser(description="Memory Usage Monitor")
    parser.add_argument('--top', type=int, default=5, help='Number of top memory-consuming processes to display')
    args = parser.parse_args()
    cli_monitor = CLIMonitor(top_processes=args.top)
    cli_monitor.run()
if __name__ == "__main__":
    main()