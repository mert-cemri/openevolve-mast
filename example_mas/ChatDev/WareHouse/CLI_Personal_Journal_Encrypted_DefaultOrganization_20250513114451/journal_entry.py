'''
Module to represent a journal entry with encryption capabilities.
'''
from encryption import Encryption
class JournalEntry:
    def __init__(self, content, timestamp, encrypted=False, salt=None):
        self.content = content
        self.timestamp = timestamp
        self.encrypted = encrypted
        self.salt = salt
    def encrypt(self, password):
        if not self.encrypted:
            self.salt = Encryption.generate_salt()
            self.content = Encryption.encrypt(self.content, password, self.salt)
            self.encrypted = True
    def decrypt(self, password):
        if self.encrypted:
            self.content = Encryption.decrypt(self.content, password, self.salt)
            self.encrypted = False
    def to_dict(self):
        return {
            'content': self.content,
            'timestamp': self.timestamp,
            'encrypted': self.encrypted,
            'salt': self.salt.decode() if self.salt else None
        }
    @staticmethod
    def from_dict(data):
        return JournalEntry(data['content'], data['timestamp'], data['encrypted'], data['salt'].encode() if data['salt'] else None)