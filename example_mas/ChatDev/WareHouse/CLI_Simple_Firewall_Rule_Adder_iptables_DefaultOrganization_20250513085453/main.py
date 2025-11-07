'''
Main entry point for the Firewall Manager CLI application. Parses command-line arguments and executes the appropriate actions.
'''
import argparse
from firewall_manager import FirewallManager
def main():
    parser = argparse.ArgumentParser(description="Manage firewall rules using iptables.")
    parser.add_argument("action", choices=["allow", "block", "remove"], help="Action to perform on the firewall rule.")
    parser.add_argument("port", type=int, help="Port number to apply the action to.")
    args = parser.parse_args()
    manager = FirewallManager()
    if args.action == "allow":
        success = manager.allow_port(args.port)
    elif args.action == "block":
        success = manager.block_port(args.port)
    elif args.action == "remove":
        success = manager.remove_rule(args.port, args.action)
    if success:
        print(f"Successfully executed {args.action} action on port {args.port}.")
    else:
        print(f"Failed to execute {args.action} action on port {args.port}.")
if __name__ == "__main__":
    main()