'''
Module to manage journal entries and file operations.
'''
import json
from datetime import datetime
from journal_entry import JournalEntry
class Journal:
    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        self.load_entries()
    def add_entry(self, content, password):
        timestamp = datetime.now().isoformat()
        entry = JournalEntry(content, timestamp)
        entry.encrypt(password)
        self.entries.append(entry)
        self.save_entries()
    def save_entries(self):
        with open(self.filename, 'w') as file:
            json.dump([entry.to_dict() for entry in self.entries], file)
    def load_entries(self):
        try:
            with open(self.filename, 'r') as file:
                entries_data = json.load(file)
                self.entries = [JournalEntry.from_dict(data) for data in entries_data]
        except FileNotFoundError:
            self.entries = []