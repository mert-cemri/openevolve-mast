'''
Represents a song with a title, artist, and album.
'''
class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album
    def __str__(self):
        return f"{self.title} by {self.artist} from {self.album}"