'''
Module containing the core logic for file encryption and decryption using AES.
Uses PBKDF2 for key derivation and AES in GCM mode for encryption/decryption.
'''
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os
def derive_key(password, salt=None):
    '''
    Derives a cryptographic key from a password using PBKDF2.
    If no salt is provided, a new random salt is generated.
    Returns the derived key and the salt.
    '''
    if salt is None:
        salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    return key, salt
def encrypt_file(input_file, output_file, password):
    '''
    Encrypts the contents of the input file and writes the encrypted data to the output file.
    Uses AES in GCM mode for encryption.
    '''
    with open(input_file, 'rb') as f:
        data = f.read()
    key, salt = derive_key(password)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(output_file, 'wb') as f:
        f.write(salt + cipher.nonce + tag + ciphertext)
def decrypt_file(input_file, output_file, password):
    '''
    Decrypts the contents of the input file and writes the decrypted data to the output file.
    Uses AES in GCM mode for decryption.
    '''
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    key, _ = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    with open(output_file, 'wb') as f:
        f.write(data)