'''
MP3TagEditor class for handling ID3 tag operations on MP3 files.
'''
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC
from mutagen.mp3 import MP3
class MP3TagEditor:
    def __init__(self, file_path):
        '''
        Initialize the MP3TagEditor with the path to the MP3 file.
        '''
        self.file_path = file_path
        self.audio = MP3(file_path, ID3=ID3)
    def view_tags(self):
        '''
        Display the current ID3 tags of the MP3 file.
        '''
        for tag in self.audio.tags.keys():
            print(f"{tag}: {self.audio.tags[tag]}")
    def edit_tag(self, tag, value):
        '''
        Edit a specific ID3 tag with a new value.
        '''
        try:
            if tag == 'title':
                self.audio.tags['TIT2'] = TIT2(encoding=3, text=value)
            elif tag == 'artist':
                self.audio.tags['TPE1'] = TPE1(encoding=3, text=value)
            elif tag == 'album':
                self.audio.tags['TALB'] = TALB(encoding=3, text=value)
            elif tag == 'year':
                if not value.isdigit() or len(value) != 4:
                    print(f"Invalid year format: {value}. Please enter a valid year (e.g., 2023).")
                    return
                self.audio.tags['TDRC'] = TDRC(encoding=3, text=value)
            else:
                print(f"Unsupported tag: {tag}")
                return
            self.audio.save()
            print(f"Updated {tag} to {value}")
        except Exception as e:
            print(f"Error updating tag: {e}")