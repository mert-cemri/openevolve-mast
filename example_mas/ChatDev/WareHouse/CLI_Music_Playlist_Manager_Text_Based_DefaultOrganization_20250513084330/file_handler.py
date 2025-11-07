'''
Handles reading from and writing to text files for storing playlists and songs.
'''
import os
from song import Song
class FileHandler:
    def __init__(self, filename="playlists.txt"):
        self.filename = filename
    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as file:
            data = file.read().strip()
            if not data:
                return {}
            playlists = {}
            for line in data.split("\n"):
                playlist_name, songs_data = line.split(":")
                songs = []
                for song_data in songs_data.split(";"):
                    title, artist, album = song_data.split(",")
                    songs.append(Song(title, artist, album))
                playlists[playlist_name] = songs
            return playlists
    def save_data(self, playlists):
        with open(self.filename, "w") as file:
            for playlist_name, songs in playlists.items():
                songs_data = ";".join([f"{song.title},{song.artist},{song.album}" for song in songs])
                file.write(f"{playlist_name}:{songs_data}\n")