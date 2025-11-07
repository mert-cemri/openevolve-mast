'''
Vault manager for handling storage and retrieval of encrypted data.
'''
import os
class VaultManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = self.load_vault()
    def load_vault(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as file:
                return file.readlines()
        return []
    def save_vault(self):
        with open(self.file_path, 'wb') as file:
            file.writelines(self.entries)
    def add_entry(self, encrypted_data):
        self.entries.append(encrypted_data.encode() + b'\n')
        self.save_vault()
    def get_entries(self):
        return [entry.decode().strip() for entry in self.entries]