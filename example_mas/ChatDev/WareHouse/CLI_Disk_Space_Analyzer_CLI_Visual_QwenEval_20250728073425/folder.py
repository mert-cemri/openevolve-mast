'''
Folder class to represent a folder in the directory.
'''
import os
from file import File
class Folder:
    def __init__(self, path, analyzer):
        self.path = path
        self.analyzer = analyzer
    def size(self):
        return self.analyzer._get_folder_size(self.path)
    def files(self):
        return [File(os.path.join(self.path, entry)) for entry in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, entry))]
    def folders(self):
        return [Folder(os.path.join(self.path, entry), self.analyzer) for entry in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, entry))]