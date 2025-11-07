'''
This module defines the JournalEntry class for managing individual journal entries with encryption capabilities.
'''
from datetime import datetime
from encryption_utils import encrypt_text, decrypt_text
class JournalEntry:
    def __init__(self, content, timestamp=None):
        self.content = content
        self.timestamp = timestamp or datetime.now()
    def encrypt(self, password, salt):
        self.content = encrypt_text(self.content, password, salt)
    def decrypt(self, password, salt):
        self.content = decrypt_text(self.content, password, salt)