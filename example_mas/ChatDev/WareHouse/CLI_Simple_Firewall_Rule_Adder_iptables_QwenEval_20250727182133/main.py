'''
Main entry point for the Firewall CLI Utility.
This script initializes the application and starts the CLI.
'''
import sys
from cli_manager import CLIManager
from firewall_manager import FirewallManager
def main():
    firewall_manager = FirewallManager()
    cli_manager = CLIManager(firewall_manager)
    cli_manager.parse_arguments(sys.argv[1:])
if __name__ == '__main__':
    main()