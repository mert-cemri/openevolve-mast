'''
Encryption utility for encrypting and decrypting data.
'''
from cryptography.fernet import Fernet
import base64
import hashlib
class EncryptionUtility:
    def __init__(self):
        pass
    def _generate_key(self, password):
        '''
        Generate a key based on the provided password using SHA-256 and base64 encoding.
        Ensure the key is 32 bytes long for Fernet.
        '''
        # Generate a SHA-256 hash of the password
        hash_digest = hashlib.sha256(password.encode()).digest()
        # Use only the first 32 bytes of the hash for the Fernet key
        return base64.urlsafe_b64encode(hash_digest)
    def encrypt(self, data, password):
        '''
        Encrypt the provided data using the generated key from the password.
        '''
        key = self._generate_key(password)
        fernet = Fernet(key)
        return fernet.encrypt(data.encode()).decode()
    def decrypt(self, encrypted_data, password):
        '''
        Decrypt the provided encrypted data using the generated key from the password.
        '''
        key = self._generate_key(password)
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data.encode()).decode()