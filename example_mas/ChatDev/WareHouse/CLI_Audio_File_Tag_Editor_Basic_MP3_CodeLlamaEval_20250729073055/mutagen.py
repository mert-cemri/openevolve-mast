import mutagen
class File:
    def __init__(self, file_path, easy=True):
        self.file_path = file_path
        self.easy = easy
    def save(self):
        # Save the changes to the MP3 file
        mutagen.File(self.file_path, easy=self.easy).save()