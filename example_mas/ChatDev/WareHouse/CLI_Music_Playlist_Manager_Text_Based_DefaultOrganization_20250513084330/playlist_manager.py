'''
Handles the creation, deletion, and management of playlists.
'''
from file_handler import FileHandler
from song import Song
class PlaylistManager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.playlists = self.file_handler.load_data()
    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = []
            self.file_handler.save_data(self.playlists)
    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
            self.file_handler.save_data(self.playlists)
    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append(song)
            self.file_handler.save_data(self.playlists)
    def remove_song_from_playlist(self, playlist_name, song_title):
        if playlist_name in self.playlists:
            self.playlists[playlist_name] = [
                song for song in self.playlists[playlist_name] if song.title != song_title
            ]
            self.file_handler.save_data(self.playlists)
    def get_playlists(self):
        return self.playlists
    def get_songs_in_playlist(self, playlist_name):
        return self.playlists.get(playlist_name, [])