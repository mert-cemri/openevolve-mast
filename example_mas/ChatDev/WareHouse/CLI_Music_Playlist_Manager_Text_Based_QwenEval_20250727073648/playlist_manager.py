'''
Handles the creation, deletion, and management of playlists.
'''
import os
class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album
    def __repr__(self):
        return f"{self.title} by {self.artist} from {self.album}"
class PlaylistManager:
    def __init__(self):
        self.playlists = {}
        self.load_playlists()
    def create_playlist(self, name):
        if name in self.playlists:
            print(f"Playlist '{name}' already exists.")
        else:
            self.playlists[name] = []
            print(f"Playlist '{name}' created.")
    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
            print(f"Playlist '{name}' deleted.")
        else:
            print(f"Playlist '{name}' does not exist.")
    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append(song)
            print(f"Song '{song.title}' added to playlist '{playlist_name}'.")
        else:
            print(f"Playlist '{playlist_name}' does not exist.")
    def remove_song_from_playlist(self, playlist_name, song_title):
        if playlist_name in self.playlists:
            songs = self.playlists[playlist_name]
            self.playlists[playlist_name] = [song for song in songs if song.title != song_title]
            if any(song.title == song_title for song in songs):
                print(f"Song '{song_title}' removed from playlist '{playlist_name}'.")
            else:
                print(f"Song '{song_title}' not found in playlist '{playlist_name}'.")
        else:
            print(f"Playlist '{playlist_name}' does not exist.")
    def view_playlist(self, name):
        if name in self.playlists:
            print(f"Playlist '{name}':")
            for song in self.playlists[name]:
                print(f" - {song}")
        else:
            print(f"Playlist '{name}' does not exist.")
    def load_playlists(self):
        '''
        Loads playlists from a text file named 'playlists.txt'.
        Each playlist is stored in the format:
        Playlist: PlaylistName
        SongTitle - Artist - Album
        '''
        if os.path.exists('playlists.txt'):
            with open('playlists.txt', 'r') as file:
                lines = file.readlines()
                current_playlist = None
                for line in lines:
                    line = line.strip()
                    if line.startswith('Playlist:'):
                        current_playlist = line.split(':')[1].strip()
                        self.playlists[current_playlist] = []
                    elif current_playlist and line:
                        title, artist, album = line.split(' - ')
                        song = Song(title, artist, album)
                        self.playlists[current_playlist].append(song)
            print("Playlists loaded.")
        else:
            print("No playlists found. Starting fresh.")
    def save_playlists(self):
        '''
        Saves playlists to a text file named 'playlists.txt'.
        Each playlist is stored in the format:
        Playlist: PlaylistName
        SongTitle - Artist - Album
        '''
        with open('playlists.txt', 'w') as file:
            for playlist_name, songs in self.playlists.items():
                file.write(f"Playlist: {playlist_name}\n")
                for song in songs:
                    file.write(f"{song.title} - {song.artist} - {song.album}\n")
        print("Playlists saved.")