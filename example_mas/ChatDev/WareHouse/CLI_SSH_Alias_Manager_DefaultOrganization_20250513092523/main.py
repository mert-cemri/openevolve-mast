'''
Main entry point for the SSH Alias Manager application.
'''
import argparse
from ssh_alias_manager import SSHAliasManager
def main():
    parser = argparse.ArgumentParser(description='SSH Alias Manager')
    parser.add_argument('action', choices=['add', 'list', 'remove'], help='Action to perform')
    parser.add_argument('--alias', help='Alias name')
    parser.add_argument('--hostname', help='Hostname for the alias')
    parser.add_argument('--user', help='User for the alias')
    parser.add_argument('--port', type=int, help='Port for the alias')
    parser.add_argument('--keyfile', help='Key file for the alias')
    args = parser.parse_args()
    manager = SSHAliasManager('aliases.json')
    if args.action == 'add':
        if not all([args.alias, args.hostname, args.user, args.port, args.keyfile]):
            print("All fields are required for adding an alias.")
            return
        manager.add_alias(args.alias, args.hostname, args.user, args.port, args.keyfile)
        print("Alias added successfully.")
    elif args.action == 'list':
        aliases = manager.list_aliases()
        for alias_name, details in aliases.items():
            print(f"{alias_name}: {details}")
    elif args.action == 'remove':
        if not args.alias:
            print("Alias name is required for removing an alias.")
            return
        manager.remove_alias(args.alias)
if __name__ == '__main__':
    main()