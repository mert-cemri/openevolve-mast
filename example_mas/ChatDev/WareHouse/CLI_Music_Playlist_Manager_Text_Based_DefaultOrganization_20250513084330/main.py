'''
Main entry point for the CLI music playlist manager application.
'''
from playlist_manager import PlaylistManager
from song import Song
def main():
    playlist_manager = PlaylistManager()
    while True:
        print("\nMusic Playlist Manager")
        print("1. Create Playlist")
        print("2. Delete Playlist")
        print("3. Add Song to Playlist")
        print("4. Remove Song from Playlist")
        print("5. View Playlists")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter playlist name: ")
            playlist_manager.create_playlist(name)
        elif choice == "2":
            name = input("Enter playlist name to delete: ")
            playlist_manager.delete_playlist(name)
        elif choice == "3":
            playlist_name = input("Enter playlist name: ")
            title = input("Enter song title: ")
            artist = input("Enter song artist: ")
            album = input("Enter song album: ")
            song = Song(title, artist, album)
            playlist_manager.add_song_to_playlist(playlist_name, song)
        elif choice == "4":
            playlist_name = input("Enter playlist name: ")
            song_title = input("Enter song title to remove: ")
            playlist_manager.remove_song_from_playlist(playlist_name, song_title)
        elif choice == "5":
            playlists = playlist_manager.get_playlists()
            for playlist_name, songs in playlists.items():
                print(f"\nPlaylist: {playlist_name}")
                for song in songs:
                    print(f"  {song}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()