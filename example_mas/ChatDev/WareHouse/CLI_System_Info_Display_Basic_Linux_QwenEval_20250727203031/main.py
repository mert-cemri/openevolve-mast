'''
Main entry point for the CLI tool to display system information.
This script initializes the SystemInfoFetcher and CLI classes and displays the system information.
'''
from system_info_fetcher import SystemInfoFetcher
from cli import CLI
def main():
    system_info_fetcher = SystemInfoFetcher()
    cli = CLI(system_info_fetcher)
    cli.display_info()
if __name__ == "__main__":
    main()