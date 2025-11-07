'''
Main file to run the CLI music playlist manager.
'''
from playlist_manager import PlaylistManager
def display_menu():
    print("\nMusic Playlist Manager")
    print("1. Create Playlist")
    print("2. Add Song")
    print("3. Remove Song")
    print("4. View Playlist")
    print("5. Exit")
def main():
    manager = PlaylistManager()
    manager.load_from_file()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            playlist_name = input("Enter playlist name: ")
            manager.create_playlist(playlist_name)
            print(f"Playlist '{playlist_name}' created.")
        elif choice == '2':
            playlist_name = input("Enter playlist name: ")
            song_title = input("Enter song title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            manager.add_song(playlist_name, song_title, artist, album)
            print(f"Song '{song_title}' added to playlist '{playlist_name}'.")
        elif choice == '3':
            playlist_name = input("Enter playlist name: ")
            song_title = input("Enter song title to remove: ")
            manager.remove_song(playlist_name, song_title)
            print(f"Song '{song_title}' removed from playlist '{playlist_name}'.")
        elif choice == '4':
            playlist_name = input("Enter playlist name: ")
            songs = manager.view_playlist(playlist_name)
            if songs:
                print(f"Playlist '{playlist_name}':")
                for song in songs:
                    print(f"- {song['title']} by {song['artist']} ({song['album']})")
            else:
                print(f"No songs found in playlist '{playlist_name}'.")
        elif choice == '5':
            manager.save_to_file()
            print("Exiting Music Playlist Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()