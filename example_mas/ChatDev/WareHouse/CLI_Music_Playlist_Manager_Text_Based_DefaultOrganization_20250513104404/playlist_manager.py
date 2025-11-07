'''
PlaylistManager class to manage playlists and songs.
'''
import os
import json
class PlaylistManager:
    def __init__(self):
        self.playlists = {}
        self.file_path = "playlists.txt"
    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = []
    def add_song(self, playlist_name, song_title, artist, album):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append({
                "title": song_title,
                "artist": artist,
                "album": album
            })
    def remove_song(self, playlist_name, song_title):
        if playlist_name in self.playlists:
            self.playlists[playlist_name] = [
                song for song in self.playlists[playlist_name] if song["title"] != song_title
            ]
    def view_playlist(self, playlist_name):
        return self.playlists.get(playlist_name, [])
    def save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.playlists, file)
    def load_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.playlists = json.load(file)