'''
Module for encrypting and decrypting journal entries.
'''
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os
class Encryption:
    def __init__(self, password, salt=None):
        if salt is None:
            self.salt = self._generate_salt()
        else:
            self.salt = salt
        self.key = self._generate_key(password, self.salt)
        self.cipher = Fernet(self.key)
    def _generate_salt(self):
        return os.urandom(16)
    def _generate_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())
    def decrypt(self, data):
        return self.cipher.decrypt(data).decode()