'''
Handles the command-line interface for the application.
'''
import argparse
class CLIManager:
    def __init__(self, firewall_manager):
        self.firewall_manager = firewall_manager
    def parse_arguments(self, args):
        parser = argparse.ArgumentParser(description='Firewall CLI Utility')
        subparsers = parser.add_subparsers(dest='command')
        add_parser = subparsers.add_parser('add', help='Add a new rule')
        add_parser.add_argument('action', choices=['allow', 'block'], help='Action to perform')
        add_parser.add_argument('protocol', help='Protocol (e.g., tcp, udp)')
        add_parser.add_argument('port', type=int, help='Port number')
        remove_parser = subparsers.add_parser('remove', help='Remove an existing rule')
        remove_parser.add_argument('protocol', help='Protocol (e.g., tcp, udp)')
        remove_parser.add_argument('port', type=int, help='Port number')
        list_parser = subparsers.add_parser('list', help='List all current rules')
        parsed_args = parser.parse_args(args)
        if parsed_args.command == 'add':
            self.handle_add_rule(parsed_args.action, parsed_args.protocol, parsed_args.port)
        elif parsed_args.command == 'remove':
            self.handle_remove_rule(parsed_args.protocol, parsed_args.port)
        elif parsed_args.command == 'list':
            self.handle_list_rules()
    def handle_add_rule(self, action, protocol, port):
        try:
            self.firewall_manager.add_rule(action, protocol, port)
            print("Rule added successfully.")
        except Exception as e:
            print(f"Error: {e}")
    def handle_remove_rule(self, protocol, port):
        try:
            self.firewall_manager.remove_rule(protocol, port)
            print("Rule removed successfully.")
        except Exception as e:
            print(f"Error: {e}")
    def handle_list_rules(self):
        try:
            rules = self.firewall_manager.list_rules()
            print(rules)
        except Exception as e:
            print(f"Error: {e}")