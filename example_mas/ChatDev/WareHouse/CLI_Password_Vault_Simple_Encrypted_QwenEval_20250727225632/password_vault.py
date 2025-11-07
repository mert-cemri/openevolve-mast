'''
This module contains the PasswordVault class, which handles the password vault functionality.
'''
from encryption import Encryption
from file_handler import FileHandler
class PasswordVault:
    def __init__(self):
        self.encryption = Encryption()
        self.file_handler = FileHandler()
        self.vault_data = {}
        self.salt = None
    def load_vault(self, master_password):
        encrypted_data = self.file_handler.read_file()
        if encrypted_data:
            self.salt, encrypted_data = encrypted_data[:16], encrypted_data[16:]
            try:
                self.vault_data = self.encryption.decrypt(encrypted_data, master_password, self.salt)
            except ValueError as e:
                print(f"Error decrypting vault: {e}")
                return False
        return True
    def save_vault(self, master_password):
        if not self.salt:
            self.salt = self.encryption.generate_salt()
        encrypted_data = self.encryption.encrypt(self.vault_data, master_password, self.salt)
        self.file_handler.write_file(self.salt + encrypted_data)
    def add_entry(self, service, username, password):
        self.vault_data[service] = {'username': username, 'password': password}
    def get_entry(self, service):
        return self.vault_data.get(service, None)
    def remove_entry(self, service):
        if service in self.vault_data:
            del self.vault_data[service]