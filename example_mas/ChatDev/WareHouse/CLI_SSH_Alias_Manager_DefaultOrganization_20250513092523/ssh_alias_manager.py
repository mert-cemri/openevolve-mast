'''
Handles the management of SSH aliases including adding, listing, and removing aliases.
'''
import json
import os
class SSHAliasManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.aliases = {}
        self.load_aliases()
    def add_alias(self, alias_name, hostname, user, port, key_file):
        self.aliases[alias_name] = {
            'hostname': hostname,
            'user': user,
            'port': port,
            'key_file': key_file
        }
        self.save_aliases()
    def list_aliases(self):
        return self.aliases
    def remove_alias(self, alias_name):
        if alias_name in self.aliases:
            del self.aliases[alias_name]
            self.save_aliases()
            print(f"Alias '{alias_name}' removed successfully.")
        else:
            print(f"Alias '{alias_name}' does not exist.")
    def load_aliases(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.aliases = json.load(file)
        else:
            self.aliases = {}
    def save_aliases(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.aliases, file, indent=4)