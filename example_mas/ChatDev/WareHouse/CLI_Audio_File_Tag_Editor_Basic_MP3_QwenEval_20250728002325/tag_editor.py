'''
Module to handle MP3 tag manipulation using the mutagen library.
This module provides a class `TagEditor` that can be used to view and modify
basic ID3 tags of MP3 files.
'''
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER
class TagEditor:
    def __init__(self, file_path):
        '''
        Initialize the TagEditor with the given MP3 file path.
        If the file does not contain an ID3 tag, a new one will be created.
        '''
        self.file_path = file_path
        try:
            self.audio = ID3(self.file_path)
        except Exception:
            # Create a new ID3 tag if the file does not contain one
            self.audio = ID3()
            self.audio.filename = self.file_path
    def get_tags(self):
        '''
        Retrieve the current tags from the MP3 file.
        Returns a dictionary with keys 'title', 'artist', 'album', and 'year'.
        If a tag is not present, the value will be an empty string.
        '''
        return {
            'title': self.audio.get('TIT2', [''])[0],
            'artist': self.audio.get('TPE1', [''])[0],
            'album': self.audio.get('TALB', [''])[0],
            'year': self.audio.get('TYER', [''])[0]
        }
    def set_tags(self, title=None, artist=None, album=None, year=None):
        '''
        Set the specified tags in the MP3 file.
        Only the tags that are provided (not None) will be updated.
        '''
        if title:
            self.audio['TIT2'] = TIT2(encoding=3, text=title)
        if artist:
            self.audio['TPE1'] = TPE1(encoding=3, text=artist)
        if album:
            self.audio['TALB'] = TALB(encoding=3, text=album)
        if year:
            self.audio['TYER'] = TYER(encoding=3, text=year)
    def save_file(self):
        '''
        Save the changes made to the MP3 file's tags.
        '''
        self.audio.save()