'''
File class to represent a file in the directory.
'''
import os
class File:
    def __init__(self, path):
        self.path = path
    def size(self):
        return os.path.getsize(self.path)