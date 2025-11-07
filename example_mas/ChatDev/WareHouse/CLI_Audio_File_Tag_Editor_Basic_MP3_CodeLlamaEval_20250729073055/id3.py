import mutagen
class Tag:
    def __init__(self):
        self.title = ""
        self.artist = ""
        self.album = ""
        self.year = ""
    def save(self, file_path):
        # Open the MP3 file
        audio = mutagen.File(file_path, easy=True)
        # Set the title, artist, album, and year tags
        audio["TIT2"] = self.title
        audio["TPE1"] = self.artist
        audio["TALB"] = self.album
        audio["TYER"] = self.year
        # Save the changes to the MP3 file
        audio.save()
        # Close the MP3 file
        audio.close()