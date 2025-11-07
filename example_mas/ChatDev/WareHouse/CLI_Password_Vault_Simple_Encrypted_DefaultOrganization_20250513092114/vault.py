'''
Handles the storage, encryption, and decryption of password entries.
'''
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import json
import os
class PasswordVault:
    def __init__(self, filename):
        self.filename = filename
        self.entries = {}
        self.key = None
        self.salt = None
    def create_master_key(self, password):
        # Generate a random salt
        self.salt = os.urandom(16)  # 16 bytes is a common length for salts
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    def encrypt_data(self, data):
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode())
    def decrypt_data(self, encrypted_data):
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_data).decode()
    def load_vault(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                # Read the salt and encrypted data
                self.salt = file.read(16)  # Assuming the salt is 16 bytes
                encrypted_data = file.read()
                decrypted_data = self.decrypt_data(encrypted_data)
                self.entries = json.loads(decrypted_data)
    def save_vault(self):
        with open(self.filename, 'wb') as file:
            data = json.dumps(self.entries)
            encrypted_data = self.encrypt_data(data)
            # Save the salt and encrypted data
            file.write(self.salt + encrypted_data)
    def add_entry(self, service, username, password):
        self.entries[service] = {'username': username, 'password': password}
        self.save_vault()
    def get_entries(self):
        return self.entries