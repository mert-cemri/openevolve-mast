'''
ssh_alias_manager.py
Manages SSH aliases by adding, listing, and removing them.
'''
import json
import os
class SSHAliasManager:
    def __init__(self, config_file='ssh_aliases.json'):
        self.config_file = config_file
        self.aliases = {}
        self.load_aliases()
    def load_aliases(self):
        '''
        Load aliases from the configuration file.
        '''
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.aliases = json.load(file)
        else:
            self.aliases = {}
    def save_aliases(self):
        '''
        Save aliases to the configuration file.
        '''
        with open(self.config_file, 'w') as file:
            json.dump(self.aliases, file, indent=4)
    def add_alias(self, alias_name, hostname, user, port, key_file):
        '''
        Add a new SSH alias.
        '''
        self.aliases[alias_name] = {
            'hostname': hostname,
            'user': user,
            'port': port,
            'key_file': key_file
        }
        self.save_aliases()
    def remove_alias(self, alias_name):
        '''
        Remove an existing SSH alias.
        '''
        if alias_name in self.aliases:
            del self.aliases[alias_name]
            self.save_aliases()
    def list_aliases(self):
        '''
        List all SSH aliases.
        '''
        return self.aliases