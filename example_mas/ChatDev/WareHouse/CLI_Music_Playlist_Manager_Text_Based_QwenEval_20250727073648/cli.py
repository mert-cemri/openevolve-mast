'''
Handles command-line interactions with the user.
'''
from playlist_manager import PlaylistManager, Song
class CLI:
    def __init__(self):
        self.manager = PlaylistManager()
    def run(self):
        while True:
            command = input("Enter a command (create, delete, add, remove, view, exit): ").strip().lower()
            if command == 'exit':
                self.manager.save_playlists()
                print("Exiting...")
                break
            self.handle_command(command)
    def handle_command(self, command):
        if command == 'create':
            name = input("Enter playlist name: ").strip()
            self.manager.create_playlist(name)
        elif command == 'delete':
            name = input("Enter playlist name: ").strip()
            self.manager.delete_playlist(name)
        elif command == 'add':
            playlist_name = input("Enter playlist name: ").strip()
            title = input("Enter song title: ").strip()
            artist = input("Enter artist: ").strip()
            album = input("Enter album: ").strip()
            song = Song(title, artist, album)
            self.manager.add_song_to_playlist(playlist_name, song)
        elif command == 'remove':
            playlist_name = input("Enter playlist name: ").strip()
            song_title = input("Enter song title to remove: ").strip()
            self.manager.remove_song_from_playlist(playlist_name, song_title)
        elif command == 'view':
            name = input("Enter playlist name: ").strip()
            self.manager.view_playlist(name)
        else:
            print("Invalid command. Please try again.")