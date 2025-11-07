'''
This module contains the Encryption class, which handles encryption and decryption of the vault data.
'''
import base64
import json
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
import os
class Encryption:
    def __init__(self):
        pass
    def generate_salt(self):
        return os.urandom(16)
    def derive_key(self, master_password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    def encrypt(self, data, master_password, salt):
        key = self.derive_key(master_password, salt)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(json.dumps(data).encode())
        return encrypted_data
    def decrypt(self, encrypted_data, master_password, salt):
        key = self.derive_key(master_password, salt)
        fernet = Fernet(key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
        except InvalidToken:
            raise ValueError("Invalid master password or corrupted data.")