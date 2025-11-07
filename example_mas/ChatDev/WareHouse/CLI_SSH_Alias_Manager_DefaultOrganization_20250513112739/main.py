'''
main.py
Provides a command-line interface for users to interact with the SSH alias manager.
'''
import argparse
from ssh_alias_manager import SSHAliasManager
def main():
    parser = argparse.ArgumentParser(description='Manage SSH aliases.')
    subparsers = parser.add_subparsers(dest='command')
    # Add alias command
    add_parser = subparsers.add_parser('add', help='Add a new SSH alias')
    add_parser.add_argument('alias_name', help='Alias name')
    add_parser.add_argument('hostname', help='Hostname')
    add_parser.add_argument('user', help='User')
    add_parser.add_argument('port', help='Port')
    add_parser.add_argument('key_file', help='Key file')
    # Remove alias command
    remove_parser = subparsers.add_parser('remove', help='Remove an existing SSH alias')
    remove_parser.add_argument('alias_name', help='Alias name to remove')
    # List aliases command
    subparsers.add_parser('list', help='List all SSH aliases')
    args = parser.parse_args()
    manager = SSHAliasManager()
    if args.command == 'add':
        manager.add_alias(args.alias_name, args.hostname, args.user, args.port, args.key_file)
        print("Alias added successfully!")
    elif args.command == 'remove':
        manager.remove_alias(args.alias_name)
        print("Alias removed successfully!")
    elif args.command == 'list':
        aliases = manager.list_aliases()
        if aliases:
            for alias_name, details in aliases.items():
                print(f"{alias_name}: {details}")
        else:
            print("No aliases found.")
if __name__ == "__main__":
    main()