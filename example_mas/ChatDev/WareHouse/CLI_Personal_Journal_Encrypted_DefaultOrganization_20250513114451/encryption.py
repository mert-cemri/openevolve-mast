'''
Module to handle encryption and decryption of journal entries.
'''
from cryptography.fernet import Fernet
import base64
import hashlib
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
class Encryption:
    @staticmethod
    def generate_salt():
        return os.urandom(16)  # Generate a secure random salt
    @staticmethod
    def encrypt(content, password, salt):
        key = Encryption._generate_key(password, salt)
        fernet = Fernet(key)
        encrypted_content = fernet.encrypt(content.encode())
        return encrypted_content.decode()
    @staticmethod
    def decrypt(encrypted_content, password, salt):
        key = Encryption._generate_key(password, salt)
        fernet = Fernet(key)
        decrypted_content = fernet.decrypt(encrypted_content.encode())
        return decrypted_content.decode()
    @staticmethod
    def _generate_key(password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Ensure the key length is 32 bytes
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        return base64.urlsafe_b64encode(key)