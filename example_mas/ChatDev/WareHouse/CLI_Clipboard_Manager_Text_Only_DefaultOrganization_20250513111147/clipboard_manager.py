'''
This module defines the ClipboardManager class, which manages an internal clipboard for text.
'''
import os
import json
class ClipboardManager:
    def __init__(self, file_path='clipboard.json'):
        '''Initialize the clipboard with an empty list or load from file.'''
        self.file_path = file_path
        self.clipboard = self.load_clipboard()
    def load_clipboard(self):
        '''Load clipboard data from a file.'''
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []
    def save_clipboard(self):
        '''Save clipboard data to a file.'''
        with open(self.file_path, 'w') as file:
            json.dump(self.clipboard, file)
    def copy(self, text):
        '''Add text to the clipboard and save.'''
        self.clipboard.append(text)
        self.save_clipboard()
    def paste(self):
        '''Retrieve the most recent text from the clipboard.'''
        if self.clipboard:
            return self.clipboard[-1]
        return ""
    def history(self):
        '''Return the history of copied texts.'''
        return self.clipboard