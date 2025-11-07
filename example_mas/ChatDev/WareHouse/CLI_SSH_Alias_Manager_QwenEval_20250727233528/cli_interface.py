'''
Handles the command-line interface interactions.
Provides methods to add, list, and remove SSH aliases.
'''
import sys
from ssh_alias_manager import SSHAliasManager, Alias
from config_file import ConfigFile
class CLIInterface:
    def __init__(self):
        self.manager = SSHAliasManager('ssh_aliases.json')
    def run(self):
        while True:
            command = input("Enter command (add, list, remove, exit): ").strip().lower()
            if command == 'add':
                self.add_alias()
            elif command == 'list':
                self.list_aliases()
            elif command == 'remove':
                self.remove_alias()
            elif command == 'exit':
                break
            else:
                print("Invalid command. Please try again.")
    def add_alias(self):
        try:
            hostname = input("Enter hostname: ").strip()
            user = input("Enter user: ").strip()
            port_str = input("Enter port: ").strip()
            key_file = input("Enter key file: ").strip()
            if not hostname or not user or not port_str or not key_file:
                raise ValueError("Hostname, user, port, and key file are required.")
            try:
                port = int(port_str)
            except ValueError:
                raise ValueError("Port must be a number.")
            if not ConfigFile(key_file).exists():
                raise FileNotFoundError(f"Key file {key_file} does not exist.")
            alias = Alias(hostname, user, port, key_file)
            self.manager.add_alias(alias)
            print(f"Alias {hostname} added successfully.")
        except ValueError as ve:
            print(f"Value error: {ve}")
        except FileNotFoundError as fnf:
            print(f"File not found: {fnf}")
        except Exception as e:
            print(f"An error occurred: {e}")
    def list_aliases(self):
        aliases = self.manager.list_aliases()
        if not aliases:
            print("No aliases found.")
        else:
            for alias in aliases:
                print(f"Hostname: {alias.hostname}, User: {alias.user}, Port: {alias.port}, Key File: {alias.key_file}")
    def remove_alias(self):
        hostname = input("Enter hostname to remove: ").strip()
        if not hostname:
            print("Hostname is required.")
            return
        confirm = input(f"Are you sure you want to remove the alias {hostname}? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Operation cancelled.")
            return
        self.manager.remove_alias(hostname)
        print(f"Alias {hostname} removed successfully.")