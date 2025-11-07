'''
Handles graphical interactions with the user using tkinter.
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
from playlist_manager import PlaylistManager, Song
class GUI:
    def __init__(self):
        self.manager = PlaylistManager()
        self.root = tk.Tk()
        self.root.title("Music Playlist Manager")
        self.root.geometry("400x300")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Music Playlist Manager", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(self.root, text="Create Playlist", command=self.create_playlist).pack(pady=5)
        tk.Button(self.root, text="Delete Playlist", command=self.delete_playlist).pack(pady=5)
        tk.Button(self.root, text="Add Song", command=self.add_song).pack(pady=5)
        tk.Button(self.root, text="Remove Song", command=self.remove_song).pack(pady=5)
        tk.Button(self.root, text="View Playlist", command=self.view_playlist).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.exit_app).pack(pady=5)
    def create_playlist(self):
        name = simpledialog.askstring("Input", "Enter playlist name:")
        if name:
            self.manager.create_playlist(name)
    def delete_playlist(self):
        name = simpledialog.askstring("Input", "Enter playlist name:")
        if name:
            self.manager.delete_playlist(name)
    def add_song(self):
        playlist_name = simpledialog.askstring("Input", "Enter playlist name:")
        if playlist_name:
            title = simpledialog.askstring("Input", "Enter song title:")
            artist = simpledialog.askstring("Input", "Enter artist:")
            album = simpledialog.askstring("Input", "Enter album:")
            if title and artist and album:
                song = Song(title, artist, album)
                self.manager.add_song_to_playlist(playlist_name, song)
    def remove_song(self):
        playlist_name = simpledialog.askstring("Input", "Enter playlist name:")
        if playlist_name:
            song_title = simpledialog.askstring("Input", "Enter song title to remove:")
            if song_title:
                self.manager.remove_song_from_playlist(playlist_name, song_title)
    def view_playlist(self):
        name = simpledialog.askstring("Input", "Enter playlist name:")
        if name:
            playlist = self.manager.playlists.get(name, [])
            if playlist:
                songs = "\n".join(str(song) for song in playlist)
                messagebox.showinfo(f"Playlist: {name}", songs)
            else:
                messagebox.showinfo(f"Playlist: {name}", "Playlist is empty or does not exist.")
    def exit_app(self):
        self.manager.save_playlists()
        self.root.destroy()
    def run(self):
        self.root.mainloop()