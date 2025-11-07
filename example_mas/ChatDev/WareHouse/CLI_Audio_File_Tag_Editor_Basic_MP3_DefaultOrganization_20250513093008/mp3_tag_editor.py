'''
This module provides the MP3TagEditor class for viewing and editing ID3 tags of MP3 files using the mutagen library.
'''
import sys
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC
class MP3TagEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.audio = ID3(file_path)
        except Exception as e:
            print(f"Error loading file: {e}")
            sys.exit(1)
    def view_tags(self):
        print("Current Tags:")
        print("Title:", self.audio.get('TIT2', 'Unknown'))
        print("Artist:", self.audio.get('TPE1', 'Unknown'))
        print("Album:", self.audio.get('TALB', 'Unknown'))
        print("Year:", self.audio.get('TDRC', 'Unknown'))
    def edit_tag(self, tag, value):
        if tag == "title":
            self.audio['TIT2'] = TIT2(encoding=3, text=value)
        elif tag == "artist":
            self.audio['TPE1'] = TPE1(encoding=3, text=value)
        elif tag == "album":
            self.audio['TALB'] = TALB(encoding=3, text=value)
        elif tag == "year":
            # Validate and format the year
            if len(value) == 4 and value.isdigit():
                value = f"{value}-01-01"  # Convert to full date format
            self.audio['TDRC'] = TDRC(encoding=3, text=value)
        else:
            print("Unknown tag:", tag)
    def save_changes(self):
        try:
            self.audio.save(self.file_path)
            print("Changes saved.")
        except Exception as e:
            print(f"Error saving changes: {e}")