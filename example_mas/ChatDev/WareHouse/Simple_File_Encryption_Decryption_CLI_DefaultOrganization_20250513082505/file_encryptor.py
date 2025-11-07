'''
Handles file encryption and decryption using AES with a user-provided password.
'''
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os
class FileEncryptor:
    def __init__(self):
        self.salt_size = 16
        self.key_size = 32
        self.iterations = 100000
        self.block_size = AES.block_size
    def _derive_key(self, password, salt):
        return PBKDF2(password, salt, dkLen=self.key_size, count=self.iterations)
    def encrypt_file(self, input_file, output_file, password):
        salt = get_random_bytes(self.salt_size)
        key = self._derive_key(password, salt)
        cipher = AES.new(key, AES.MODE_GCM)
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        with open(output_file, 'wb') as f:
            for x in (salt, cipher.nonce, tag, ciphertext):
                f.write(x)
    def decrypt_file(self, input_file, output_file, password):
        with open(input_file, 'rb') as f:
            salt = f.read(self.salt_size)
            nonce = f.read(self.block_size)
            tag = f.read(self.block_size)
            ciphertext = f.read()
        key = self._derive_key(password, salt)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        with open(output_file, 'wb') as f:
            f.write(plaintext)