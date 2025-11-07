'''
This module provides utility functions for encrypting and decrypting text.
'''
from cryptography.fernet import Fernet
import base64
import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
def generate_key(password, salt, iterations=100000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
def encrypt_text(text, password, salt):
    key = generate_key(password, salt)
    fernet = Fernet(key)
    return fernet.encrypt(text.encode()).decode()
def decrypt_text(encrypted_text, password, salt):
    key = generate_key(password, salt)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_text.encode()).decode()