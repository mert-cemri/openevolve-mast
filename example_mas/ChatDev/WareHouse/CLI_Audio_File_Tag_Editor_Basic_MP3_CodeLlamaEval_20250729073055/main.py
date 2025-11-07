import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import id3
def main():
    # Create the main window
    root = tk.Tk()
    root.title("MP3 Tag Editor")
    root.geometry("500x300")
    # Create a frame for the file chooser
    file_chooser_frame = ttk.Frame(root)
    file_chooser_frame.pack(fill="both", expand=True)
    # Create a button for choosing the MP3 file
    choose_file_button = ttk.Button(file_chooser_frame, text="Choose MP3 File", command=choose_file)
    choose_file_button.pack(side="left")
    # Create a label for displaying the file name
    file_name_label = ttk.Label(file_chooser_frame, text="No file chosen")
    file_name_label.pack(side="left")
    # Create a frame for the tag editor
    tag_editor_frame = ttk.Frame(root)
    tag_editor_frame.pack(fill="both", expand=True)
    # Create a label for the title tag
    title_label = ttk.Label(tag_editor_frame, text="Title:")
    title_label.pack(side="left")
    # Create an entry for the title tag
    title_entry = ttk.Entry(tag_editor_frame)
    title_entry.pack(side="left")
    # Create a label for the artist tag
    artist_label = ttk.Label(tag_editor_frame, text="Artist:")
    artist_label.pack(side="left")
    # Create an entry for the artist tag
    artist_entry = ttk.Entry(tag_editor_frame)
    artist_entry.pack(side="left")
    # Create a label for the album tag
    album_label = ttk.Label(tag_editor_frame, text="Album:")
    album_label.pack(side="left")
    # Create an entry for the album tag
    album_entry = ttk.Entry(tag_editor_frame)
    album_entry.pack(side="left")
    # Create a label for the year tag
    year_label = ttk.Label(tag_editor_frame, text="Year:")
    year_label.pack(side="left")
    # Create an entry for the year tag
    year_entry = ttk.Entry(tag_editor_frame)
    year_entry.pack(side="left")
    # Create a button for saving the tags
    save_button = ttk.Button(tag_editor_frame, text="Save Tags", command=save_tags)
    save_button.pack(side="left")
    # Create a button for exiting the program
    exit_button = ttk.Button(tag_editor_frame, text="Exit", command=root.destroy)
    exit_button.pack(side="left")
    # Run the main loop
    root.mainloop()
def choose_file():
    # Open a file dialog to choose the MP3 file
    file_path = filedialog.askopenfilename(initialdir="/", title="Select MP3 File", filetypes=(("MP3 files", "*.mp3"),))
    # If a file is chosen, display the file name in the label
    if file_path:
        file_name_label.config(text=file_path)
def save_tags():
    # Get the values of the title, artist, album, and year tags
    title = title_entry.get()
    artist = artist_entry.get()
    album = album_entry.get()
    year = year_entry.get()
    # Create an ID3 tag object
    tag = id3.Tag()
    # Set the title, artist, album, and year tags
    tag.title = title
    tag.artist = artist
    tag.album = album
    tag.year = year
    # Save the tags to the MP3 file
    tag.save(file_path)
    # Display a message box to confirm that the tags were saved
    messagebox.showinfo("Tags Saved", "The tags were saved successfully.")
if __name__ == "__main__":
    main()