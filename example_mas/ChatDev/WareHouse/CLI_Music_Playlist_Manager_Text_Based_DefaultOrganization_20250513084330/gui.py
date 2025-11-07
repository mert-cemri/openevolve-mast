'''
Handles the graphical user interface using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from song import Song
class GUI:
    def __init__(self, playlist_manager):
        self.playlist_manager = playlist_manager
        self.root = tk.Tk()
        self.root.title("Music Playlist Manager")
    def setup_gui(self):
        self.playlist_listbox = tk.Listbox(self.root)
        self.playlist_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.song_listbox = tk.Listbox(self.root)
        self.song_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.refresh_playlist_display()
        self.root.mainloop()
    def refresh_playlist_display(self):
        self.playlist_listbox.delete(0, tk.END)
        for playlist_name in self.playlist_manager.get_playlists():
            self.playlist_listbox.insert(tk.END, playlist_name)
        self.song_listbox.delete(0, tk.END)
        selected_playlist = self.playlist_listbox.get(tk.ACTIVE)
        if selected_playlist:
            for song in self.playlist_manager.get_songs_in_playlist(selected_playlist):
                self.song_listbox.insert(tk.END, str(song))