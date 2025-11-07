'''
Handles file encryption and decryption using AES.
'''
# file_encryptor.py
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os
import base64
class FileEncryptor:
    def __init__(self):
        self.backend = default_backend()
    def _derive_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=self.backend
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    def encrypt_file(self, input_file, output_file, password):
        salt = os.urandom(16)  # Generate a new salt for each encryption
        key = self._derive_key(password, salt)
        iv = os.urandom(12)  # GCM requires a 12-byte IV
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        with open(input_file, 'rb') as f:
            data = f.read()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        with open(output_file, 'wb') as f:
            f.write(salt + iv + encryptor.tag + encrypted_data)  # Write salt, iv, and tag first
    def decrypt_file(self, input_file, output_file, password):
        try:
            with open(input_file, 'rb') as f:
                data = f.read()
            salt = data[:16]  # Read salt from file
            iv = data[16:28]
            tag = data[28:44]
            encrypted_data = data[44:]
            key = self._derive_key(password, salt)
            cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=self.backend)
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
            with open(output_file, 'wb') as f:
                f.write(decrypted_data)
        except Exception as e:
            raise ValueError("Decryption failed. Please check the password and try again.") from e