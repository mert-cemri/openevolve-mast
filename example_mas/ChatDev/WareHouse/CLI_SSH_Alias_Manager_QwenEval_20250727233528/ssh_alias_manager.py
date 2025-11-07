'''
Handles the core functionality of adding, listing, and removing SSH aliases.
'''
import json
from config_file import ConfigFile
class Alias:
    def __init__(self, hostname, user, port, key_file):
        self.hostname = hostname
        self.user = user
        self.port = port
        self.key_file = key_file
    def to_dict(self):
        return {
            'hostname': self.hostname,
            'user': self.user,
            'port': self.port,
            'key_file': self.key_file
        }
class SSHAliasManager:
    def __init__(self, config_file_path):
        self.config_file = ConfigFile(config_file_path)
        self.aliases = self.load_aliases()
    def load_aliases(self):
        data = self.config_file.read()
        return [Alias(**alias) for alias in data]
    def add_alias(self, alias):
        if any(a.hostname == alias.hostname for a in self.aliases):
            raise ValueError(f"Alias with hostname {alias.hostname} already exists.")
        self.aliases.append(alias)
        self.save_aliases()
    def list_aliases(self):
        return self.aliases
    def remove_alias(self, hostname):
        self.aliases = [alias for alias in self.aliases if alias.hostname != hostname]
        self.save_aliases()
    def save_aliases(self):
        data = [alias.to_dict() for alias in self.aliases]
        self.config_file.write(data)