'''
Module for managing journal entries.
'''
import datetime
import json
from encryption import Encryption
class JournalEntry:
    def __init__(self, content, encryption=None, salt=None):
        self.timestamp = datetime.datetime.now()
        if encryption:
            self.content = encryption.encrypt(content)
            self.salt = salt
        else:
            self.content = content
            self.salt = None
    def to_dict(self):
        return {
            'timestamp': self.timestamp.isoformat(),
            'content': self.content,
            'salt': self.salt
        }
    @classmethod
    def from_dict(cls, data, encryption=None):
        entry = cls(data['content'], encryption, data['salt'])
        entry.timestamp = datetime.datetime.fromisoformat(data['timestamp'])
        return entry
class Journal:
    def __init__(self, filename, encryption=None):
        self.filename = filename
        self.entries = []
        self.encryption = encryption  # Add this line
    def add_entry(self, entry):
        self.entries.append(entry)
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([entry.to_dict() for entry in self.entries], f)
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.entries = [JournalEntry.from_dict(entry, self.encryption) for entry in data]  # Update this line
        except FileNotFoundError:
            self.entries = []