'''
This module defines the Journal class for managing a collection of journal entries.
'''
import json
import os
import base64
from datetime import datetime
from journal_entry import JournalEntry
class Journal:
    def __init__(self, file_path='journal.json'):
        self.entries = []
        self.file_path = file_path
        self.salt = None
        self.load_salt()
    def load_salt(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.salt = base64.b64decode(data.get('salt', ''))
        else:
            self.salt = os.urandom(16)  # Generate a new salt
            self.save_salt()
    def save_salt(self):
        # Load existing entries if any
        entries_data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                entries_data = data.get('entries', [])
        # Save both salt and entries
        with open(self.file_path, 'w') as file:
            json.dump({
                'salt': base64.b64encode(self.salt).decode(),
                'entries': entries_data
            }, file)
    def add_entry(self, content, password):
        entry = JournalEntry(content)
        entry.encrypt(password, self.salt)
        self.entries.append(entry)
    def save_entries(self):
        with open(self.file_path, 'w') as file:
            json.dump({
                'salt': base64.b64encode(self.salt).decode(),
                'entries': [{'content': entry.content, 'timestamp': entry.timestamp.isoformat()} for entry in self.entries]
            }, file)
    def load_entries(self, password):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.salt = base64.b64decode(data['salt'])
                entries_data = data['entries']
                for entry_data in entries_data:
                    entry = JournalEntry(entry_data['content'], datetime.fromisoformat(entry_data['timestamp']))
                    entry.decrypt(password, self.salt)
                    self.entries.append(entry)
        except FileNotFoundError:
            print("No existing journal file found. Starting a new journal.")